# Lambda function Invoke API calls are recorded by CloudTrail

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_invoke_api_operations_cloudtrail_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | low |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Defense Evasion |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

**AWS Lambda** function invocations are recorded as **CloudTrail data events** when trails include `AWS::Lambda::Function` resources. The finding reflects whether a function's `Invoke` activity is being logged by an eligible trail.

## リスク

Without Lambda `Invoke` data events, per-invocation accountability is lost. Adversaries or misused automation can run code without an audit trail, obscuring actor, time, and source. This hinders forensics and enables covert exfiltration or unauthorized changes, impacting **confidentiality** and **integrity**.

## 推奨事項

Enable **CloudTrail data event logging** for `AWS::Lambda::Function` to capture `Invoke` calls across required Regions and accounts. Apply **least privilege** selectors to scope events, centralize logs with strong retention, and integrate alerts for anomalous invokes as part of **defense in depth**.

## 修正手順


### CLI

```text
aws cloudtrail put-event-selectors --trail-name <example_resource_name> --advanced-event-selectors '[{"FieldSelectors":[{"Field":"eventCategory","Equals":["Data"]},{"Field":"resources.type","Equals":["AWS::Lambda::Function"]}]}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: <example_resource_name>
      IsLogging: true
      EventSelectors:
        - DataResources:
            - Type: AWS::Lambda::Function  # Critical: enables Lambda data event logging
              Values:
                - arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function  # Critical: logs Invoke events for all functions in the specified account/region
```

### Terraform

```hcl
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"

  event_selector {
    data_resource {
      type   = "AWS::Lambda::Function"  # Critical: enable Lambda data events
      values = ["arn:aws:lambda:<REGION>:<ACCOUNT_ID>:function"]  # Critical: capture Invoke for all functions in this account/region
    }
  }
}
```

### Other

1. In the AWS Console, go to CloudTrail > Trails
2. Select your trail and click Edit or Event logging
3. Under Data events, choose Add data event selector (or Edit)
4. Select Lambda function and choose to log data events for all functions (or specify functions)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/lambda/latest/dg/logging-using-cloudtrail.html](https://docs.aws.amazon.com/lambda/latest/dg/logging-using-cloudtrail.html)
- [https://support.icompaas.com/support/solutions/articles/62000127055-ensure-lambda-functions-invoke-api-operations-are-being-recorded-by-cloudtrail](https://support.icompaas.com/support/solutions/articles/62000127055-ensure-lambda-functions-invoke-api-operations-are-being-recorded-by-cloudtrail)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/metadata.json](../../sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/metadata.json)
- Source Code：[sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/check.py](../../sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_invoke_api_operations_cloudtrail_logging_enabled/check.py`

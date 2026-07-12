# Lambda function uses a supported runtime

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_using_supported_runtimes` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

**Lambda functions** using **obsolete runtimes**-such as `python3.8`, `nodejs14.x`, `go1.x`, `ruby2.7`-are identified against a curated list of deprecated runtime identifiers.

## リスク

Unmaintained runtimes lack security patches, exposing code and libraries to known CVEs (**confidentiality, integrity**). Deprecation can block create/update and break builds, causing failed deployments or runtime errors (**availability**). Tooling may stop supporting builds, slowing fixes and recovery.

## 推奨事項

Upgrade to **supported LTS runtimes** (AL2/AL2023) and include runtime upgrades in a secure SDLC. Test in staging, deploy via versions/aliases, and keep dependencies current. Monitor deprecation notices. Apply guardrails to block deprecated `runtime` values and allow only approved runtimes, aligning with **defense in depth**.

## 修正手順


### CLI

```text
aws lambda update-function-configuration --function-name <FUNCTION_NAME> --runtime <SUPPORTED_RUNTIME>
```

### Native IaC

```yaml
# CloudFormation: set Lambda to a supported runtime
Resources:
  <example_resource_name>:
    Type: AWS::Lambda::Function
    Properties:
      Role: <example_role_arn>
      Handler: <example_handler>
      Runtime: <SUPPORTED_RUNTIME>  # FIX: change to a supported runtime (e.g., python3.12) to pass the check
      Code:
        S3Bucket: <example_bucket_name>
        S3Key: <example_object_key>
```

### Terraform

```hcl
# Set Lambda to a supported runtime
resource "aws_lambda_function" "<example_resource_name>" {
  function_name = "<example_resource_name>"
  role          = "<example_role_arn>"
  handler       = "<example_handler>"
  runtime       = "<SUPPORTED_RUNTIME>" # FIX: use a supported runtime (e.g., python3.12) to pass the check
  filename      = "<example_package.zip>"
}
```

### Other

1. Open the AWS Lambda console and select the function
2. Go to Configuration > Runtime settings > Edit
3. In Runtime, choose a supported runtime (e.g., python3.12) and click Save

## 参考資料

- [https://aws.amazon.com/blogs/compute/managing-aws-lambda-runtime-upgrades/](https://aws.amazon.com/blogs/compute/managing-aws-lambda-runtime-upgrades/)
- [https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html](https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/supported-runtime-environment.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/supported-runtime-environment.html)
- [https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_using_supported_runtimes/metadata.json](../../sources/aws/awslambda_function_using_supported_runtimes/metadata.json)
- Source Code：[sources/aws/awslambda_function_using_supported_runtimes/check.py](../../sources/aws/awslambda_function_using_supported_runtimes/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_using_supported_runtimes/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_using_supported_runtimes/check.py`

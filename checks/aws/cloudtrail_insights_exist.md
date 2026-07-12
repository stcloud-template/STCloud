# CloudTrail trail has Insights enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_insights_exist` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | low |
| カテゴリ | forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail trails** that are logging are evaluated for **Insights** via `insight selectors`, which enable anomaly detection on management-event patterns (API call and error rates). The finding pinpoints logging trails where these selectors are missing.

## リスク

Without **Insights**, abnormal API call or error rates can go unnoticed, delaying detection of credential abuse, privilege escalation, or runaway automation. Attackers may rapidly alter policies, delete resources, or exfiltrate data before response, impacting confidentiality and availability.

## 推奨事項

Enable **CloudTrail Insights** on all logging trails (ideally all-Region or organization trails). Activate both `ApiCallRateInsight` and `ApiErrorRateInsight`. Integrate alerts with monitoring and review anomalies regularly. Apply **defense in depth** and least privilege to reduce potential blast radius.

## 修正手順


### CLI

```text
aws cloudtrail put-insight-selectors --trail-name <TRAIL_NAME> --insight-selectors '[{"InsightType":"ApiCallRateInsight"}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      TrailName: <example_resource_name>
      S3BucketName: <example_resource_name>
      IsLogging: true
      InsightSelectors:
        - InsightType: ApiCallRateInsight  # Critical fix: enables CloudTrail Insights on the trail
```

### Terraform

```hcl
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"
  enable_logging = true

  insight_selector {
    insight_type = "ApiCallRateInsight"  # Critical fix: enables CloudTrail Insights on the trail
  }
}
```

### Other

1. In the AWS Console, go to CloudTrail > Trails
2. Select the trail that is logging
3. Click Edit on the CloudTrail Insights section
4. Enable Insights and select API call rate (or Error rate)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html)
- [https://awscli.amazonaws.com/v2/documentation/api/2.18.18/reference/cloudtrail/put-insight-selectors.html](https://awscli.amazonaws.com/v2/documentation/api/2.18.18/reference/cloudtrail/put-insight-selectors.html)
- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudtrail](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudtrail)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_insights_exist/metadata.json](../../sources/aws/cloudtrail_insights_exist/metadata.json)
- Source Code：[sources/aws/cloudtrail_insights_exist/check.py](../../sources/aws/cloudtrail_insights_exist/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_insights_exist/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_insights_exist/check.py`

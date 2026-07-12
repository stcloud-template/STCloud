# GuardDuty detector has S3 Protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `guardduty_s3_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | guardduty |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exfiltration |
| リソースタイプ | AwsGuardDutyDetector |
| リソースグループ | security |

## 説明

Amazon GuardDuty detectors are evaluated for **S3 Protection**, which analyzes CloudTrail S3 data events to monitor **object-level API activity** (`GetObject`, `PutObject`, `DeleteObject`) across S3 buckets in the account and Region.

## リスク

Without S3 Protection, **object-level S3 activity** isn't analyzed, enabling: - **Exfiltration** via mass reads/copies - **Destructive deletes** - **Policy/ACL tampering** Undetected actions degrade data confidentiality, integrity, and availability.

## 推奨事項

Enable **S3 Protection** across all accounts and Regions to add **defense in depth** for S3. Apply **least privilege** to IAM and bucket policies, keep **Block Public Access** enforced, integrate findings with alerting, and regularly review anomalies to prevent data loss and tampering.

## 修正手順


### CLI

```text
aws guardduty update-detector --detector-id <detector-id> --data-sources S3Logs={Enable=true}
```

### Native IaC

```yaml
# CloudFormation: Enable S3 Protection on a GuardDuty detector
Resources:
  <example_resource_name>:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true
      DataSources:
        S3Logs:
          Enable: true  # Critical: Enables GuardDuty S3 Protection
```

### Terraform

```hcl
# Enable S3 Protection on a GuardDuty detector
resource "aws_guardduty_detector" "<example_resource_name>" {
  enable = true

  datasources {
    s3_logs {
      enable = true  # Critical: Enables GuardDuty S3 Protection
    }
  }
}
```

### Other

1. Open the AWS Management Console and go to GuardDuty
2. In the left menu, select Settings
3. Find the S3 Protection section and click Enable (or toggle On)
4. Click Save

## 参考資料

- [https://docs.amazonaws.cn/en_us/guardduty/latest/ug/guardduty_finding-types-s3.html](https://docs.amazonaws.cn/en_us/guardduty/latest/ug/guardduty_finding-types-s3.html)
- [https://docs.aws.amazon.com/guardduty/latest/ug/s3_detection.html](https://docs.aws.amazon.com/guardduty/latest/ug/s3_detection.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/enable-s3-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/enable-s3-protection.html)
- [https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-10](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-10)

## 技術情報

- Source Metadata：[sources/aws/guardduty_s3_protection_enabled/metadata.json](../../sources/aws/guardduty_s3_protection_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_s3_protection_enabled/check.py](../../sources/aws/guardduty_s3_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_s3_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_s3_protection_enabled/check.py`

# GuardDuty detector has RDS Protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `guardduty_rds_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | guardduty |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Credential Access |
| リソースタイプ | AwsGuardDutyDetector |
| リソースグループ | security |

## 説明

Active **Amazon GuardDuty detectors** are assessed for **RDS Protection** being enabled, allowing analysis of RDS and Aurora login activity to profile and flag anomalous access patterns.

## リスク

Without **RDS Protection**, anomalous database logins can go unnoticed. Attackers using **stolen** or **brute-forced** credentials may access data, alter schemas, or pivot via the DB, impacting **confidentiality** and **integrity**, and potentially **availability**.

## 推奨事項

Enable **GuardDuty RDS Protection** across all accounts and Regions. - Enforce **least privilege** for DB users and rotate credentials - Restrict network exposure to databases - Integrate findings with alerting and incident response for rapid containment

## 修正手順


### CLI

```text
aws guardduty update-detector --detector-id <detector-id> --features Name=RDS_LOGIN_EVENTS,Status=ENABLED
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true
      Features:
        - Name: RDS_LOGIN_EVENTS  # critical: selects GuardDuty RDS Protection feature
          Status: ENABLED         # critical: turns RDS Protection on
```

### Terraform

```hcl
resource "aws_guardduty_detector" "<example_resource_name>" {
  enable = true
  features {
    name   = "RDS_LOGIN_EVENTS"  # critical: GuardDuty RDS Protection feature
    status = "ENABLED"            # critical: enable the feature
  }
}
```

### Other

1. In the AWS Console, open Amazon GuardDuty
2. Go to Settings (or Protection plans/Features)
3. Find RDS Protection (RDS login events) and click Enable
4. Save changes
5. If using Organizations, perform this in the delegated GuardDuty administrator account

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-9](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-9)
- [https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/guard-duty-rds-protection.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/guard-duty-rds-protection.html)

## 技術情報

- Source Metadata：[sources/aws/guardduty_rds_protection_enabled/metadata.json](../../sources/aws/guardduty_rds_protection_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_rds_protection_enabled/check.py](../../sources/aws/guardduty_rds_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_rds_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_rds_protection_enabled/check.py`

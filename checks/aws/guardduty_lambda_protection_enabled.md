# GuardDuty detector has Lambda Protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `guardduty_lambda_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | guardduty |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsGuardDutyDetector |
| リソースグループ | security |

## 説明

**Amazon GuardDuty detectors** with **Lambda Protection** enabled analyze **Lambda invocation network activity logs** across your account. Evaluation determines whether the detector has `Lambda Protection` turned on.

## リスク

Without **Lambda Protection**, Lambda network traffic is uninspected, enabling: - **C2 callbacks** and data exfiltration (confidentiality) - Malicious code altering data or configs (integrity) - Lateral movement or abuse causing disruption (availability)

## 推奨事項

Enable **Lambda Protection** on all detectors in every active Region and account. Apply **least privilege** to Lambda roles, restrict egress with network controls, and integrate findings with alerting and response for **defense in depth**. *In multi-account setups*, manage centrally for consistent coverage.

## 修正手順


### CLI

```text
aws guardduty update-detector --detector-id <detector-id> --features '[{"Name":"LAMBDA_NETWORK_LOGS","Status":"ENABLED"}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true
      Features:
        - Name: LAMBDA_NETWORK_LOGS  # Critical: selects Lambda Protection feature
          Status: ENABLED            # Critical: enables Lambda Protection
```

### Terraform

```hcl
resource "aws_guardduty_detector" "<example_resource_name>" {
  enable = true
  features {
    name   = "LAMBDA_NETWORK_LOGS"  # Critical: selects Lambda Protection feature
    status = "ENABLED"               # Critical: enables Lambda Protection
  }
}
```

### Other

1. Open the AWS Console and go to GuardDuty
2. In the left pane, select Settings > Lambda Protection
3. Click Enable
4. Click Confirm to save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-6](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-6)
- [https://docs.aws.amazon.com/guardduty/latest/ug/configure-lambda-protection-standalone-acc.html](https://docs.aws.amazon.com/guardduty/latest/ug/configure-lambda-protection-standalone-acc.html)
- [https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html)

## 技術情報

- Source Metadata：[sources/aws/guardduty_lambda_protection_enabled/metadata.json](../../sources/aws/guardduty_lambda_protection_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_lambda_protection_enabled/check.py](../../sources/aws/guardduty_lambda_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_lambda_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_lambda_protection_enabled/check.py`

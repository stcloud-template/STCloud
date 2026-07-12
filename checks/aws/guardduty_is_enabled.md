# GuardDuty detector is enabled and not suspended

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `guardduty_is_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | guardduty |
| 重大度 | high |
| カテゴリ | forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsGuardDutyDetector |
| リソースグループ | security |

## 説明

**Amazon GuardDuty** detector existence and health are evaluated per Region. It identifies where GuardDuty isn't enabled for the account, where a detector has no status, or where a detector is configured but `suspended`.

## リスク

Without active **GuardDuty**, threats in CloudTrail, VPC Flow Logs, DNS, S3, EKS, EBS, and Lambda can go unnoticed. Attackers can exfiltrate data, move laterally, and mine crypto, degrading confidentiality, integrity, and availability-especially in unmonitored Regions.

## 推奨事項

Enable and keep **GuardDuty** active in all supported Regions and accounts under a delegated admin. Turn on relevant protection plans and auto-enroll new accounts. Avoid `suspended` detectors, enforce **least privilege** for admins, and integrate findings into response for **defense in depth**.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Ensure GuardDuty detector is enabled (not suspended) in the Region
Resources:
  ExampleGuardDutyDetector:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true  # Critical: enables the detector so GuardDuty is active (not suspended)
```

### Terraform

```hcl
# Terraform: Ensure GuardDuty detector is enabled (not suspended) in the Region
resource "aws_guardduty_detector" "example_resource_name" {
  enable = true  # Critical: turns GuardDuty on and ensures it is not suspended
}
```

### Other

1. Sign in to the AWS Console and open Amazon GuardDuty
2. Switch to the target AWS Region
3. If prompted with Get started, click Enable GuardDuty
4. If GuardDuty is already configured but suspended, go to Settings and click Enable (or Resume) to activate the detector
5. Repeat in each required Region

## 参考資料

- [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html)
- [https://aws.plainenglish.io/how-to-protect-your-organizations-aws-account-with-aws-guardduty-a1a635c417aa](https://aws.plainenglish.io/how-to-protect-your-organizations-aws-account-with-aws-guardduty-a1a635c417aa)
- [https://medium.com/swlh/aws-cdk-automating-guardduty-event-notifications-in-all-regions-f0bbcec6077d](https://medium.com/swlh/aws-cdk-automating-guardduty-event-notifications-in-all-regions-f0bbcec6077d)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/guardduty-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/GuardDuty/guardduty-enabled.html)
- [https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-terraform-to-automatically-enable-amazon-guardduty-for-an-organization.html)

## 技術情報

- Source Metadata：[sources/aws/guardduty_is_enabled/metadata.json](../../sources/aws/guardduty_is_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_is_enabled/check.py](../../sources/aws/guardduty_is_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_is_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_is_enabled/check.py`

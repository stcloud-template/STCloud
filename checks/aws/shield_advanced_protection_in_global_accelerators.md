# Global Accelerator accelerator is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_global_accelerators` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | security |

## 説明

**AWS Global Accelerator** accelerators are assessed for enrollment in **Shield Advanced** as `protected resources`, indicating whether enhanced DDoS coverage is configured for each accelerator.

## リスク

Without **Shield Advanced**, Global Accelerators are more vulnerable to volumetric and protocol **DDoS** that can exhaust capacity, causing **availability** loss, elevated **latency**, and disrupted failover. Limited visibility and no SRT support prolong incidents and can trigger unexpected **cost** spikes from malicious traffic.

## 推奨事項

Add each Global Accelerator as a `protected resource` in **Shield Advanced**. Apply **defense in depth** with AWS WAF where applicable, enable proactive monitoring and alerting, and use **Firewall Manager** to enforce coverage across accounts. Follow **least privilege** to restrict who can modify protections.

## 修正手順


### CLI

```text
aws shield create-protection --name <example_resource_name> --resource-arn <example_resource_id>
```

### Native IaC

```yaml
# CloudFormation: Add Shield Advanced protection to a Global Accelerator accelerator
Resources:
  ShieldProtection:
    Type: AWS::Shield::Protection
    Properties:
      Name: <example_resource_name>
      ResourceArn: <example_resource_id>  # Critical: ARN of the Global Accelerator accelerator to protect
```

### Terraform

```hcl
# Enable Shield Advanced protection for a Global Accelerator accelerator
resource "aws_shield_protection" "protection" {
  name         = "<example_resource_name>"
  resource_arn = "<example_resource_id>"  # Critical: ARN of the Global Accelerator accelerator to protect
}
```

### Other

1. In the AWS Console, open AWS WAF & Shield
2. Under AWS Shield, select Protected resources
3. Click Add resources to protect
4. Set Scope to Global and select the Global Accelerator resource type
5. Select the target accelerator and click Protect with Shield Advanced

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_global_accelerators/metadata.json](../../sources/aws/shield_advanced_protection_in_global_accelerators/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_global_accelerators/check.py](../../sources/aws/shield_advanced_protection_in_global_accelerators/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_global_accelerators/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_global_accelerators/check.py`

# Internet-facing Application Load Balancer is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_internet_facing_load_balancers` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | internet-exposed, resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**Application Load Balancers** that are **internet-facing** are evaluated for an associated **AWS Shield Advanced** protection. Scope includes ALBs of type application with external exposure.

## リスク

Without enhanced DDoS protection, internet-facing ALBs are exposed to volumetric L3/L4 floods and HTTP L7 floods, compromising **availability** via outages and latency spikes. Sudden scaling can raise **costs**, while reduced visibility and response support extend disruption across dependent services.

## 推奨事項

Register internet-facing ALBs as **Shield Advanced protected resources** to strengthen **availability**. Use defense-in-depth: pair with **AWS WAF** for L7 filtering and rate limits, group related assets, enable health-based detection and proactive engagement, and enforce least-privilege IAM with continuous monitoring.

## 修正手順


### CLI

```text
aws shield create-protection --name <ALB_NAME> --resource-arn <ALB_ARN>
```

### Native IaC

```yaml
Resources:
  ShieldProtection:
    Type: AWS::Shield::Protection
    Properties:
      Name: "<example_resource_name>"
      ResourceArn: "<example_resource_id>" # CRITICAL: Set to the ALB ARN to enable Shield Advanced protection for it
```

### Terraform

```hcl
resource "aws_shield_protection" "protect" {
  name         = "<example_resource_name>"
  resource_arn = "<example_resource_id>" # CRITICAL: ALB ARN; creating this enables Shield Advanced on the ALB
}
```

### Other

1. In the AWS Console, open AWS WAF & Shield
2. Go to Shield > Protected resources
3. Click Add resources to protect
4. Select the Region and resource type Application Load Balancer
5. Select your internet-facing ALB
6. Click Protect with Shield Advanced

## 参考資料

- [https://aws.amazon.com/documentation-overview/shield/](https://aws.amazon.com/documentation-overview/shield/)
- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json](../../sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py](../../sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_internet_facing_load_balancers/check.py`

# Classic Load Balancer is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_classic_load_balancers` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| リソースタイプ | AwsElbLoadBalancer |
| リソースグループ | network |

## 説明

**Classic Load Balancers** are evaluated for association with **AWS Shield Advanced** as a protected resource. Identifies load balancers without an active Shield Advanced protection when the subscription is enabled.

## リスク

Unprotected ELB Classic endpoints are more exposed to large L3/L4 DDoS (e.g., SYN/UDP floods), risking **availability loss** from connection exhaustion and failed health checks, plus operational impact from autoscaling and data transfer surges.

## 推奨事項

Add internet-facing **Classic Load Balancers** as protected resources in **Shield Advanced** to strengthen DDoS resilience and cost protection. Apply defense-in-depth: minimize public exposure, enforce least-privilege network access, enable health-based detection, and use protection groups.

## 修正手順


### CLI

```text
aws shield create-protection --name <PROTECTION_NAME> --resource-arn <ELB_ARN>
```

### Native IaC

```yaml
# CloudFormation: Add Shield Advanced protection to a Classic Load Balancer
Resources:
  <example_resource_name>:
    Type: AWS::Shield::Protection
    Properties:
      Name: <example_resource_name>
      ResourceArn: <example_resource_id>  # Critical: ARN of the Classic Load Balancer to protect
```

### Terraform

```hcl
# Add Shield Advanced protection to a Classic Load Balancer
resource "aws_shield_protection" "<example_resource_name>" {
  name         = "<example_resource_name>"
  resource_arn = "<example_resource_id>" # Critical: ARN of the Classic Load Balancer to protect
}
```

### Other

1. In the AWS Console, open AWS WAF & Shield
2. Go to Shield > Protected resources and click Add resources to protect
3. Select the Region and resource type Classic Load Balancer, then Load resources
4. Select your Classic Load Balancer and click Protect with Shield Advanced
5. Confirm to create the protection

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_classic_load_balancers/metadata.json](../../sources/aws/shield_advanced_protection_in_classic_load_balancers/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_classic_load_balancers/check.py](../../sources/aws/shield_advanced_protection_in_classic_load_balancers/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_classic_load_balancers/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_classic_load_balancers/check.py`

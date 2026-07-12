# Route53 hosted zone is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_route53_hosted_zones` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsRoute53HostedZone |
| リソースグループ | network |

## 説明

**Route 53 hosted zones** have an active **AWS Shield Advanced** protection registered to the zone's `ARN`.

## リスク

Without **Shield Advanced**, authoritative DNS is vulnerable to: - **Volumetric/reflection** floods - **Query/application** layer attacks Effects: disrupted resolution and app outages (**availability**), latency spikes, and unexpected cost from attack traffic.

## 推奨事項

Add critical **Route 53 hosted zones** as **Shield Advanced protected resources** to apply managed DDoS safeguards. Follow **defense in depth**: limit DNS exposure, enforce least-privilege for protection changes, monitor traffic baselines, and prepare incident runbooks with clear escalation to speed response.

## 修正手順


### CLI

```text
aws shield create-protection --name <example_resource_name> --resource-arn arn:aws:route53:::hostedzone/<example_resource_id>
```

### Native IaC

```yaml
# CloudFormation: Add Shield Advanced protection to a Route53 hosted zone
Resources:
  <example_resource_name>:
    Type: AWS::Shield::Protection
    Properties:
      ResourceArn: arn:aws:route53:::hostedzone/<example_resource_id>  # Critical: Protects the hosted zone with Shield Advanced
```

### Terraform

```hcl
# Add Shield Advanced protection to a Route53 hosted zone
resource "aws_shield_protection" "<example_resource_name>" {
  name         = "<example_resource_name>"
  resource_arn = "arn:aws:route53:::hostedzone/<example_resource_id>"  # Critical: Protects the hosted zone with Shield Advanced
}
```

### Other

1. Open the AWS WAF & Shield console
2. Go to AWS Shield > Protected resources
3. Click Add resources to protect
4. Set Scope to Global and select resource type: Amazon Route 53 Hosted Zone
5. Select the hosted zone and click Protect with Shield Advanced

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_route53_hosted_zones/metadata.json](../../sources/aws/shield_advanced_protection_in_route53_hosted_zones/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_route53_hosted_zones/check.py](../../sources/aws/shield_advanced_protection_in_route53_hosted_zones/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_route53_hosted_zones/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_route53_hosted_zones/check.py`

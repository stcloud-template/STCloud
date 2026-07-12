# CloudFront distribution is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_cloudfront_distributions` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** are associated with **AWS Shield Advanced** as protected resources. The assessment identifies distributions that lack this protection mapping.

## リスク

Missing **Shield Advanced** leaves distributions exposed to large **DDoS** that degrade **availability** via L3/L4 floods and L7 request surges. Effects include edge saturation, latency, and outages, plus loss of **cost protection** and expert support, causing unexpected spend and longer recovery.

## 推奨事項

Enroll critical CloudFront distributions in **AWS Shield Advanced** and keep them listed as protected resources. Adopt layered defense: **AWS WAF**, rate limiting, and continuous monitoring. Maintain DDoS runbooks and use DRT support. Apply **least privilege** to who can modify protections.

## 修正手順


### CLI

```text
aws shield create-protection --region us-east-1 --name <example_resource_name> --resource-arn <example_resource_arn>
```

### Native IaC

```yaml
# CloudFormation: Add Shield Advanced protection to a CloudFront distribution
Resources:
  ShieldProtection:
    Type: AWS::Shield::Protection
    Properties:
      Name: <example_resource_name>
      ResourceArn: <example_resource_arn>  # Critical: associates Shield Advanced protection with the CloudFront distribution ARN
```

### Terraform

```hcl
# Add Shield Advanced protection to a CloudFront distribution
resource "aws_shield_protection" "example" {
  name         = "<example_resource_name>"
  resource_arn = "<example_resource_arn>"  # Critical: associates Shield Advanced protection with the CloudFront distribution ARN
}
```

### Other

1. In the AWS Console, open WAF & Shield
2. Go to AWS Shield > Protected resources
3. Click Add resources to protect
4. Set Scope to Global and select CloudFront distributions, then Load resources
5. Select the target distribution
6. Click Protect with Shield Advanced

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_cloudfront_distributions/metadata.json](../../sources/aws/shield_advanced_protection_in_cloudfront_distributions/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_cloudfront_distributions/check.py](../../sources/aws/shield_advanced_protection_in_cloudfront_distributions/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_cloudfront_distributions/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_cloudfront_distributions/check.py`

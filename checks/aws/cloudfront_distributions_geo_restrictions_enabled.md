# CloudFront distribution has Geo restrictions enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_geo_restrictions_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | low |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** have **geographic restrictions** configured to limit access by country using an allowlist or blocklist (`RestrictionType` not `none`).

## リスク

Absent geo restrictions, content is globally reachable, enabling: - Access from sanctioned or unlicensed regions (confidentiality/compliance) - Broader bot abuse, scraping, and DDoS staging (availability) - More credential-stuffing and fraud attempts against apps

## 推奨事項

Apply **least privilege** to distribution scope: enable geo restrictions with a country **allowlist** where feasible, or maintain a precise blocklist aligned to legal, licensing, and threat models. Layer **defense in depth**: use WAF/bot controls, signed URLs or cookies, and monitoring to detect abuse and configuration drift.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add Restrictions.GeoRestriction with RestrictionType: "whitelist" and Locations: ["US"], then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - DomainName: "<example_origin_domain>"
            Id: "<example_origin_id>"
        DefaultCacheBehavior:
          TargetOriginId: "<example_origin_id>"
          ViewerProtocolPolicy: allow-all
          CachePolicyId: "<example_cache_policy_id>"
        Restrictions:
          GeoRestriction:
            RestrictionType: whitelist  # CRITICAL: enables geo restrictions
            Locations:                  # CRITICAL: at least one allowed country
              - US
```

### Terraform

```hcl
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origins {
    domain_name = "<example_origin_domain>"
    origin_id   = "<example_origin_id>"
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "allow-all"
    cache_policy_id        = "<example_cache_policy_id>"
  }

  restrictions {
    geo_restriction {
      restriction_type = "whitelist" # CRITICAL: enables geo restrictions
      locations        = ["US"]      # CRITICAL: at least one allowed country
    }
  }
}
```

### Other

1. In the AWS Console, go to CloudFront > Distributions
2. Select the target distribution
3. Open the Security tab > Geographic restrictions > Edit
4. Choose Allow list (or Block list)
5. Add at least one country to the list
6. Save changes

## 参考資料

- [https://repost.aws/knowledge-center/cloudfront-geo-restriction](https://repost.aws/knowledge-center/cloudfront-geo-restriction)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/geo-restriction.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/geo-restriction.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json](../../sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py](../../sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py`

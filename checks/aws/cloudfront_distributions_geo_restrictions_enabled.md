# CloudFront distribution has Geo restrictions enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudfront_distributions_geo_restrictions_enabled` |
| 云平台 | AWS |
| 服务 | cloudfront |
| 严重等级 | low |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| 资源类型 | AwsCloudFrontDistribution |
| 资源组 | network |

## 描述

**CloudFront distributions** have **geographic restrictions** configured to limit access by country using an allowlist or blocklist (`RestrictionType` not `none`).

## 风险

Absent geo restrictions, content is globally reachable, enabling: - Access from sanctioned or unlicensed regions (confidentiality/compliance) - Broader bot abuse, scraping, and DDoS staging (availability) - More credential-stuffing and fraud attempts against apps

## 推荐措施

Apply **least privilege** to distribution scope: enable geo restrictions with a country **allowlist** where feasible, or maintain a precise blocklist aligned to legal, licensing, and threat models. Layer **defense in depth**: use WAF/bot controls, signed URLs or cookies, and monitoring to detect abuse and configuration drift.

## 修复步骤


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

## 参考资料

- [https://repost.aws/knowledge-center/cloudfront-geo-restriction](https://repost.aws/knowledge-center/cloudfront-geo-restriction)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/geo-restriction.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/geo-restriction.html)

## 技术信息

- Source Metadata：[sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json](../../sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py](../../sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_geo_restrictions_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_geo_restrictions_enabled/check.py`

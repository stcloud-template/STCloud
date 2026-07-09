# CloudFront distribution has origin failover configured with at least two origins

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudfront_distributions_multiple_origin_failover_configured` |
| 云平台 | AWS |
| 服务 | cloudfront |
| 严重等级 | low |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Effects/Denial of Service |
| 资源类型 | AwsCloudFrontDistribution |
| 资源组 | network |

## 描述

**CloudFront distributions** are evaluated for an **origin group** configured with at least `2` origins to support automatic origin failover.

## 风险

Without **origin failover**, the origin becomes a **single point of failure**. Origin outages, regional incidents, or targeted **DoS** can cause **downtime**, elevated error rates, and latency, degrading **availability** and impacting user experience and SLAs.

## 推荐措施

Enable **origin failover** by defining an origin group with primary and secondary origins. Distribute origins across independent zones or providers, set clear failover criteria (e.g., HTTP codes/timeouts), monitor health, and routinely test failover. Align with **resilience** and **defense-in-depth** to protect availability.

## 修复步骤


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add OriginGroups with two origins and FailoverCriteria, then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: Add an origin group with two origins and use it in the default cache behavior
Resources:
  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          Quantity: 2
          Items:
            - Id: primary
              DomainName: <primary_origin_domain>
              S3OriginConfig: {}
            - Id: secondary
              DomainName: <secondary_origin_domain>
              S3OriginConfig: {}
        OriginGroups:
          Quantity: 1
          Items:
            - Id: <example_origin_group_id>  # Critical: define origin group with 2 origins
              FailoverCriteria:
                StatusCodes:
                  Quantity: 1
                  Items: [500]  # Critical: fail over on 500 to enable origin failover
              Members:
                Quantity: 2
                Items:
                  - OriginId: primary
                  - OriginId: secondary
        DefaultCacheBehavior:
          TargetOriginId: <example_origin_group_id>  # Critical: use the origin group for requests
          ViewerProtocolPolicy: allow-all
          ForwardedValues:
            QueryString: false
            Cookies:
              Forward: none
```

### Terraform

```hcl
# Configure an origin group with two origins and use it in the default cache behavior
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<primary_origin_domain>"
    origin_id   = "primary"
    s3_origin_config {}
  }

  origin {
    domain_name = "<secondary_origin_domain>"
    origin_id   = "secondary"
    s3_origin_config {}
  }

  origin_group {
    origin_id = "<example_origin_group_id>"  # Critical: define origin group with 2 origins
    failover_criteria {
      status_codes = [500]  # Critical: fail over on 500 to enable origin failover
    }
    member { origin_id = "primary" }
    member { origin_id = "secondary" }
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_group_id>"  # Critical: use the origin group for requests
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  restrictions {
    geo_restriction { restriction_type = "none" }
  }

  viewer_certificate { cloudfront_default_certificate = true }
}
```

### Other

1. In the AWS Console, go to CloudFront and open your distribution
2. Select the Origins tab and ensure two origins exist; add a second origin if needed
3. In the Origin groups pane, click Create origin group
4. Select the two origins; set one as primary and the other as secondary
5. Choose at least one failover status code (e.g., 500) and create the group
6. Go to Behaviors, edit the relevant cache behavior (or Default behavior)
7. Set Origin to the new origin group and save changes
8. Deploy/confirm the distribution update

## 参考资料

- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-4)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/origin-failover-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/origin-failover-enabled.html)

## 技术信息

- Source Metadata：[sources/aws/cloudfront_distributions_multiple_origin_failover_configured/metadata.json](../../sources/aws/cloudfront_distributions_multiple_origin_failover_configured/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_multiple_origin_failover_configured/check.py](../../sources/aws/cloudfront_distributions_multiple_origin_failover_configured/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_multiple_origin_failover_configured/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_multiple_origin_failover_configured/check.py`

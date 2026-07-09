# CloudFront distribution has a default root object configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudfront_distributions_default_root_object` |
| 云平台 | AWS |
| 服务 | cloudfront |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsCloudFrontDistribution |
| 资源组 | network |

## 描述

CloudFront distributions are evaluated for a configured **default root object** that maps `/` requests to a specific file such as `index.html`, rather than forwarding root requests directly to the origin.

## 风险

Without a **default root object**, root requests can reveal **origin listings** or unintended files, exposing data (**confidentiality**) and aiding reconnaissance. They may also return errors, lowering uptime (**availability**), or route unpredictably, risking wrong content delivery (**integrity**).

## 推荐措施

Set a **default root object** that returns a safe landing page (e.g., `index.html`). Apply **defense in depth**: restrict direct origin access, define explicit error pages, and standardize redirects. Test root and subdirectory requests for predictable responses. Align origin permissions with **least privilege**.

## 修复步骤


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add DefaultRootObject: "index.html", then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: Set a default root object on a CloudFront distribution
Resources:
  CloudFrontDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        DefaultRootObject: index.html  # CRITICAL: ensures a default root object is configured
        Origins:
          - Id: <example_origin_id>
            DomainName: <example_origin_domain>
            S3OriginConfig: {}
        DefaultCacheBehavior:
          TargetOriginId: <example_origin_id>
          ViewerProtocolPolicy: allow-all
          ForwardedValues:
            QueryString: false
```

### Terraform

```hcl
# Terraform: Set a default root object on a CloudFront distribution
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled             = true
  default_root_object = "index.html" # CRITICAL: ensures a default root object is configured

  origin {
    domain_name = "<example_origin_domain>"
    origin_id   = "<example_origin_id>"

    s3_origin_config {}
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false
    }
  }
}
```

### Other

1. Open the AWS Console and go to CloudFront
2. Select the target distribution and choose Settings > General > Edit
3. In Default root object, enter index.html (do not start with a /)
4. Save changes and wait for deployment to complete

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-1)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-default-object.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-default-object.html)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html)

## 技术信息

- Source Metadata：[sources/aws/cloudfront_distributions_default_root_object/metadata.json](../../sources/aws/cloudfront_distributions_default_root_object/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_default_root_object/check.py](../../sources/aws/cloudfront_distributions_default_root_object/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_default_root_object/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_default_root_object/check.py`

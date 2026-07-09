# CloudFront distribution does not use SSLv3, TLSv1, or TLSv1.1 for origin connections

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudfront_distributions_using_deprecated_ssl_protocols` |
| 云平台 | AWS |
| 服务 | cloudfront |
| 严重等级 | low |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsCloudFrontDistribution |
| 资源组 | network |

## 描述

CloudFront distributions have origins whose `OriginSslProtocols` allow **deprecated SSL/TLS versions** (`SSLv3`, `TLSv1`, `TLSv1.1`) for CloudFront-to-origin HTTPS connections.

## 风险

Weak protocols between CloudFront and the origin allow downgrades and known exploits (e.g., POODLE/BEAST), enabling eavesdropping or content tampering. This compromises the **confidentiality** and **integrity** of data in transit, exposing cookies, credentials, and responses served to viewers.

## 推荐措施

Enforce **TLS 1.2+** for CloudFront-to-origin traffic. Remove `SSLv3`, `TLSv1`, `TLSv1.1` from allowed protocols and prefer modern cipher suites. Verify origin compatibility, update certificates and libraries, and periodically review policies as part of **defense in depth** and **least privilege**.

## 修复步骤


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to change Origins[].CustomOriginConfig.OriginSslProtocols to [TLSv1.2], then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: set origin to allow only TLSv1.2 when connecting to the origin
Resources:
  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - Id: <example_origin_id>
            DomainName: <origin.example.com>
            CustomOriginConfig:
              OriginProtocolPolicy: https-only
              OriginSslProtocols:
                - TLSv1.2  # CRITICAL: restrict origin SSL protocols to TLSv1.2 to remove SSLv3/TLSv1/TLSv1.1
        DefaultCacheBehavior:
          TargetOriginId: <example_origin_id>
          ViewerProtocolPolicy: redirect-to-https
```

### Terraform

```hcl
# Terraform: set origin to allow only TLSv1.2 when connecting to the origin
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<origin.example.com>"
    origin_id   = "<example_origin_id>"

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]  # CRITICAL: restrict origin SSL protocols to TLSv1.2
    }
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    forwarded_values { query_string = false }
  }
}
```

### Other

1. Open the AWS Console and go to CloudFront
2. Select the distribution and open the Origins tab
3. Select the custom origin and click Edit
4. Under Origin SSL protocols, select only TLSv1.2
5. Save changes
6. Repeat for any other custom origins in the distribution

## 参考资料

- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-insecure-origin-ssl-protocols.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-insecure-origin-ssl-protocols.html)
- [https://support.icompaas.com/support/solutions/articles/62000223404-ensure-cloudfront-distributions-are-not-using-deprecated-ssl-protocols](https://support.icompaas.com/support/solutions/articles/62000223404-ensure-cloudfront-distributions-are-not-using-deprecated-ssl-protocols)

## 技术信息

- Source Metadata：[sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/metadata.json](../../sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/check.py](../../sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_using_deprecated_ssl_protocols/check.py`

# CloudFront distribution encrypts traffic to custom origins

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_origin_traffic_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Security, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** are evaluated for **TLS to origins**. The check ensures custom origins use `origin_protocol_policy`=`https-only`, or `match-viewer` only when the viewer protocol policy disallows HTTP. For S3 origins, it inspects the viewer protocol policy and flags `allow-all` as permitting non-encrypted paths.

## リスク

Unencrypted origin links enable on-path interception and manipulation. Secrets, cookies, and PII can be exposed, and responses altered, undermining **confidentiality** and **integrity**. This increases chances of session hijacking, cache poisoning, and malicious content injection.

## 推奨事項

Enforce end-to-end HTTPS. Set `origin_protocol_policy` to `https-only` and viewer policy to `https-only` or `redirect-to-https`. Use trusted certificates and modern TLS (`TLSv1.2+`), disabling weak protocols. Apply **least privilege** and **defense in depth** by restricting direct origin access and preferring private connectivity.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to change Origins[].CustomOriginConfig.OriginProtocolPolicy to https-only', then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: set CloudFront origin to use HTTPS only
Resources:
  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - Id: <example_origin_id>
            DomainName: <example_origin_domain>
            CustomOriginConfig:
              OriginProtocolPolicy: https-only  # FIX: Force CloudFront-to-origin over HTTPS only
        DefaultCacheBehavior:
          TargetOriginId: <example_origin_id>
          ViewerProtocolPolicy: allow-all
          ForwardedValues:
            QueryString: false
```

### Terraform

```hcl
# Terraform: set CloudFront origin to use HTTPS only
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<example_origin_domain>"
    origin_id   = "<example_origin_id>"

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "https-only"   # FIX: Force CloudFront-to-origin over HTTPS only
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
  }

  restrictions { geo_restriction { restriction_type = "none" } }
  viewer_certificate { cloudfront_default_certificate = true }
}
```

### Other

1. In the AWS Console, open CloudFront and select your distribution
2. Go to the Origins tab, select the custom origin, and click Edit
3. Set Protocol to HTTPS only (Origin protocol policy = HTTPS Only)
4. Click Save changes and wait for the distribution to deploy

## 参考資料

- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-traffic-to-origin-unencrypted.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-traffic-to-origin-unencrypted.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-9](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-9)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html)
- [https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/custom-origin-with-cloudfront.html](https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/custom-origin-with-cloudfront.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_origin_traffic_encrypted/metadata.json](../../sources/aws/cloudfront_distributions_origin_traffic_encrypted/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_origin_traffic_encrypted/check.py](../../sources/aws/cloudfront_distributions_origin_traffic_encrypted/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_origin_traffic_encrypted/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_origin_traffic_encrypted/check.py`

# CloudFront distribution serves HTTPS requests using SNI

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_https_sni_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | low |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** that use **custom SSL/TLS certificates** are configured to serve **HTTPS** using **Server Name Indication** (`ssl_support_method: sni-only`). It evaluates SNI use rather than dedicated IP during the TLS handshake.

## リスク

Without **SNI**, distributions use dedicated IP SSL, driving higher costs and inefficient IP usage. Dedicated IPs can strain quotas and hinder scaling, reducing **availability**. Managing IP-bound certificates adds **operational risk** during rotations and expansions.

## 推奨事項

Use **SNI** (`sni-only`) for **HTTPS** with custom certificates; avoid dedicated IP unless a critical, non-SNI client requires it. Document and periodically review exceptions, plan client upgrades, and adopt the latest **TLS security policy** to standardize secure, modern configurations.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to change ViewerCertificate.SslSupportMethod to sni-only', then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
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
          - Id: <example_origin_id>
            DomainName: <example_origin_domain>
            S3OriginConfig:
              OriginAccessIdentity: ''
        DefaultCacheBehavior:
          TargetOriginId: <example_origin_id>
          ViewerProtocolPolicy: allow-all
          ForwardedValues:
            QueryString: false
            Cookies:
              Forward: none
          MinTTL: 0
        ViewerCertificate:
          AcmCertificateArn: <example_certificate_arn>
          SslSupportMethod: sni-only  # Critical: enable SNI for HTTPS
          MinimumProtocolVersion: TLSv1  # Required when using SNI with a custom cert
```

### Terraform

```hcl
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<example_origin_domain>"
    origin_id   = "<example_origin_id>"
  }

  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "allow-all"
    forwarded_values {
      query_string = false
      cookies { forward = "none" }
    }
    min_ttl = 0
  }

  viewer_certificate {
    acm_certificate_arn      = "<example_certificate_arn>"
    ssl_support_method       = "sni-only"  # Critical: enable SNI for HTTPS
    minimum_protocol_version = "TLSv1"     # Required with SNI
  }
}
```

### Other

1. In the AWS Console, go to CloudFront and open your distribution
2. Select the Settings/General tab and click Edit
3. Under SSL certificate, ensure your custom certificate is selected
4. Set Client support to SNI only
5. Click Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-sni.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-sni.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-8](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-8)
- [https://support.icompaas.com/support/solutions/articles/62000223557-ensure-cloudfront-sni-enabled](https://support.icompaas.com/support/solutions/articles/62000223557-ensure-cloudfront-sni-enabled)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.html#cnames-https-sni](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-https-dedicated-ip-or-sni.html#cnames-https-sni)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_https_sni_enabled/metadata.json](../../sources/aws/cloudfront_distributions_https_sni_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_https_sni_enabled/check.py](../../sources/aws/cloudfront_distributions_https_sni_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_https_sni_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_https_sni_enabled/check.py`

# CloudFront distribution uses a custom SSL/TLS certificate

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_custom_ssl_certificate` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

CloudFront distributions are configured with a **custom SSL/TLS certificate** rather than the default `*.cloudfront.net` certificate for viewer connections.

## リスク

Using the default certificate prevents HTTPS on your own hostnames, breaking hostname validation. Clients may face errors or avoid TLS, impacting **authentication** and **availability**. Control over TLS posture and domain-bound security headers is reduced, weakening **confidentiality** and user trust.

## 推奨事項

- Use a **custom SSL/TLS certificate** covering your domains and configure aliases. - Enforce modern TLS policy, **SNI**, and **HSTS**; disable legacy protocols. - Apply **least privilege** to certificate lifecycle and rotate/monitor keys.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add Aliases and ViewerCertificate fields, then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
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
          - Id: origin1
            DomainName: <example_origin_domain>
            S3OriginConfig: {}
        DefaultCacheBehavior:
          TargetOriginId: origin1
          ViewerProtocolPolicy: redirect-to-https
          ForwardedValues:
            QueryString: false
        Aliases:
          - <example_domain>  # CRITICAL: add an alternate domain name (CNAME) covered by the certificate
        ViewerCertificate:
          AcmCertificateArn: <example_certificate_arn>  # CRITICAL: attach custom ACM cert (must be in us-east-1)
          SslSupportMethod: sni-only  # CRITICAL: required when using ACM cert
```

### Terraform

```hcl
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<example_origin_domain>"
    origin_id   = "origin1"
    s3_origin_config {}
  }

  default_cache_behavior {
    target_origin_id       = "origin1"
    viewer_protocol_policy = "redirect-to-https"
    forwarded_values { query_string = false }
  }

  aliases = ["<example_domain>"]  # CRITICAL: add CNAME covered by the cert

  viewer_certificate {
    acm_certificate_arn = "<example_certificate_arn>"  # CRITICAL: custom ACM cert (in us-east-1)
    ssl_support_method  = "sni-only"                    # CRITICAL: required with ACM cert
  }
}
```

### Other

1. Open the CloudFront console and select your distribution
2. Go to the Settings/General tab and click Edit
3. In Alternate domain name (CNAME), add <example_domain>
4. In SSL certificate, choose Custom SSL certificate and select your ACM certificate (issued in us-east-1 and covering <example_domain>)
5. Click Save/Yes, Edit and wait for the distribution to deploy

## 参考資料

- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-distro-custom-tls.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-distro-custom-tls.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-7)
- [https://support.icompaas.com/support/solutions/articles/62000233491-ensure-cloudfront-distributions-use-custom-ssl-tls-certificates](https://support.icompaas.com/support/solutions/articles/62000233491-ensure-cloudfront-distributions-use-custom-ssl-tls-certificates)
- [https://reintech.io/blog/configure-https-ssl-certificates-cloudfront-distributions](https://reintech.io/blog/configure-https-ssl-certificates-cloudfront-distributions)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_custom_ssl_certificate/metadata.json](../../sources/aws/cloudfront_distributions_custom_ssl_certificate/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_custom_ssl_certificate/check.py](../../sources/aws/cloudfront_distributions_custom_ssl_certificate/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_custom_ssl_certificate/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_custom_ssl_certificate/check.py`

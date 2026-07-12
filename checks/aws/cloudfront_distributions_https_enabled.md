# CloudFront distribution has viewer protocol policy set to HTTPS only or redirect to HTTPS

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_https_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

CloudFront distributions require viewer connections over **HTTPS** when the default cache behavior `viewer_protocol_policy` is `https-only` or `redirect-to-https`. Configurations that use `allow-all` permit HTTP.

## リスク

Allowing HTTP exposes traffic to **man-in-the-middle** interception and **session hijacking**, enabling theft of cookies, tokens, or PII. Attackers can **tamper** with responses, inject malware, or perform **downgrade/strip** attacks, undermining confidentiality and integrity.

## 推奨事項

Enforce **HTTPS-only** access for viewers by setting `viewer_protocol_policy` to `https-only` or `redirect-to-https`; avoid `allow-all`. Extend encryption end-to-end to origins, enable **HSTS**, prefer modern TLS and ciphers, and mark cookies `Secure`. This supports **defense in depth** and prevents downgrade.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to change DefaultCacheBehavior.ViewerProtocolPolicy to "redirect-to-https" or "https-only", then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: set ViewerProtocolPolicy to require HTTPS
Resources:
  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        DefaultCacheBehavior:
          ViewerProtocolPolicy: https-only  # Critical: requires HTTPS for viewers
```

### Terraform

```hcl
# Terraform: set viewer_protocol_policy to force HTTPS
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  default_cache_behavior {
    target_origin_id       = "<example_origin_id>"
    viewer_protocol_policy = "redirect-to-https" # Critical: forces HTTP to HTTPS
  }
}
```

### Other

1. In the AWS Console, go to CloudFront > Distributions
2. Select the target distribution and open the Behaviors tab
3. Select the Default (*) behavior and click Edit
4. Set Viewer protocol policy to Redirect HTTP to HTTPS (or HTTPS Only)
5. Save changes and deploy

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/security-policy.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/security-policy.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_https_enabled/metadata.json](../../sources/aws/cloudfront_distributions_https_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_https_enabled/check.py](../../sources/aws/cloudfront_distributions_https_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_https_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_https_enabled/check.py`

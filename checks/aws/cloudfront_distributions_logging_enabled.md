# CloudFront distribution has logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** record viewer requests using either **standard access logs** or an attached **real-time log configuration**. The finding evaluates whether logging is configured so request metadata is captured for each distribution.

## リスク

Missing **CloudFront logs** blinds monitoring of edge requests, impeding detection of bot abuse, credential stuffing, origin probing, and cache-bypass attempts. This delays incident response and weakens evidence for forensics, impacting **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Enable **standard access logs** or **real-time logs** for all distributions. Apply **least privilege** to log storage, enforce retention and immutability, and centralize ingestion with alerts. Use **defense-in-depth**: correlate with WAF metrics, sample real-time when needed, and audit new distributions for logging.

## 修正手順


### CLI

```text
aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add Logging.Bucket: <example_bucket>.s3.amazonaws.com', then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: enable CloudFront standard access logging
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
          ViewerProtocolPolicy: allow-all
        Logging:
          Bucket: <example_bucket>.s3.amazonaws.com  # CRITICAL: enables standard access logs to S3 for this distribution
          # The presence of Logging with Bucket turns on access logging
```

### Terraform

```hcl
# Add this block to your existing CloudFront distribution to enable access logging
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  # ... existing required config ...
  logging_config {
    bucket = "<example_bucket>.s3.amazonaws.com"  # CRITICAL: enables standard access logs to S3
  }
}
```

### Other

1. In the AWS Console, go to CloudFront and select your distribution
2. Open the General tab and click Edit
3. In Standard logging, set to On
4. Select the S3 bucket to receive logs
5. Ensure the S3 bucket has Object Ownership set to ACLs enabled (Bucket owner preferred/ObjectWriter)
6. Save changes

## 参考資料

- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)
- [https://repost.aws/knowledge-center/cloudfront-logging-requests](https://repost.aws/knowledge-center/cloudfront-logging-requests)
- [https://aws.amazon.com/awstv/watch/e895e7811ac/](https://aws.amazon.com/awstv/watch/e895e7811ac/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/enable-real-time-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/enable-real-time-logging.html)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_logging_enabled/metadata.json](../../sources/aws/cloudfront_distributions_logging_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_logging_enabled/check.py](../../sources/aws/cloudfront_distributions_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_logging_enabled/check.py`

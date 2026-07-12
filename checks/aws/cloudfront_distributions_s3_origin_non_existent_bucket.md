# CloudFront distribution S3 origins reference existing buckets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_s3_origin_non_existent_bucket` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | high |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

**CloudFront distributions** with `S3OriginConfig` should reference existing **S3 bucket origins** (excluding static website hosting). Identifies origins where the configured bucket name does not exist.

## リスク

**Dangling S3 origins** allow potential **bucket takeover**: an attacker could create the missing bucket and have CloudFront retrieve attacker-controlled objects *if access isn't restricted*. This threatens **integrity** (content spoofing, cache poisoning) and **availability** (errors/timeouts), undermining user trust.

## 推奨事項

Ensure origins reference valid, owned buckets; delete or update stale references. Enforce **origin access control** (or OAI) and tight bucket policies so only the distribution can access objects. Apply **least privilege**, manage bucket names, and monitor origin health to prevent misrouting.

## 修正手順


### Native IaC

```yaml
# CloudFormation: ensure the S3 bucket referenced by the CloudFront S3 origin exists
Resources:
  <example_resource_name>:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: <example_resource_name>  # Critical: must exactly match the bucket name used in the CloudFront origin's domain (before ".s3") to make it exist
```

### Terraform

```hcl
# Ensure the S3 bucket referenced by the CloudFront S3 origin exists
resource "aws_s3_bucket" "<example_resource_name>" {
  bucket = "<example_resource_name>"  # Critical: must exactly match the bucket name used in the CloudFront origin's domain (before ".s3")
}
```

### Other

1. In the AWS console, open CloudFront and select the distribution
2. Go to Origins, select the S3 origin, and note the Domain Name (the bucket name is the text before ".s3")
3. Open the S3 console, click Create bucket, enter the exact bucket name from step 2, and create the bucket
4. Re-run the check

## 参考資料

- [https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/s3-origin-with-cloudfront.html](https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/s3-origin-with-cloudfront.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-12](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-12)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-existing-s3-bucket.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-existing-s3-bucket.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/metadata.json](../../sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/check.py](../../sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_s3_origin_non_existent_bucket/check.py`

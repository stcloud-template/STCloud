# CloudFront distribution has Field Level Encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudfront_distributions_field_level_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudfront |
| 重大度 | low |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsCloudFrontDistribution |
| リソースグループ | network |

## 説明

CloudFront distributions have the default cache behavior associated with **Field-Level Encryption** via `field_level_encryption_id`, targeting specified request fields for edge encryption.

## リスク

Absent **field-level encryption**, sensitive inputs (PII, payment data, credentials) may surface in origin paths, logs, or middleware in plaintext. This undermines **confidentiality**, enables data exfiltration and insider misuse, and can lead to session or account compromise if tokens are captured.

## 推奨事項

Enable **Field-Level Encryption** for sensitive request fields and bind it to relevant cache behaviors. Apply **least privilege** to decryption keys, rotate and monitor keys, and separate duties. As **defense in depth**, minimize data collection, avoid logging secrets, require HTTPS end-to-end, and validate inputs.

## 修正手順


### CLI

```text
aws cloudfront create-field-level-encryption-config --field-level-encryption-config file://fle-config.json && aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --output json > current-config.json && echo 'Manually edit current-config.json to add FieldLevelEncryptionId to DefaultCacheBehavior, then run:' && echo 'aws cloudfront update-distribution --id <DISTRIBUTION_ID> --distribution-config file://current-config.json --if-match $(aws cloudfront get-distribution-config --id <DISTRIBUTION_ID> --query "ETag" --output text)'
```

### Native IaC

```yaml
# CloudFormation: Enable Field Level Encryption on Default Cache Behavior
Resources:
  FLEConfig:
    Type: AWS::CloudFront::FieldLevelEncryptionConfig
    Properties:
      FieldLevelEncryptionConfig:
        CallerReference: !Ref AWS::StackName
        ContentTypeProfileConfig:
          ForwardWhenContentTypeIsUnknown: true
          ContentTypeProfiles:
            Quantity: 0

  <example_resource_name>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - DomainName: "<example_resource_name>.s3.amazonaws.com"
            Id: "<example_resource_id>"
            S3OriginConfig: {}
        DefaultCacheBehavior:
          TargetOriginId: "<example_resource_id>"
          ViewerProtocolPolicy: redirect-to-https
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6
          FieldLevelEncryptionId: !Ref FLEConfig  # Critical: enables FLE on the default cache behavior
```

### Terraform

```hcl
# Enable Field Level Encryption on Default Cache Behavior
resource "aws_cloudfront_field_level_encryption_config" "fle" {
  content_type_profile_config {
    forward_when_content_type_is_unknown = true
  }
}

resource "aws_cloudfront_distribution" "<example_resource_name>" {
  enabled = true

  origin {
    domain_name = "<example_resource_name>.s3.amazonaws.com"
    origin_id   = "<example_resource_id>"
  }

  default_cache_behavior {
    target_origin_id       = "<example_resource_id>"
    viewer_protocol_policy = "redirect-to-https"
    cache_policy_id        = "658327ea-f89d-4fab-a63d-7e88639e58f6"
    field_level_encryption_id = aws_cloudfront_field_level_encryption_config.fle.id # Critical: enables FLE
  }
}
```

### Other

1. In the AWS Console, go to CloudFront
2. If you don't have a Field-level encryption configuration:
   - In the left menu, click Public keys > Add public key (paste your RSA public key)
   - Click Field-level encryption > Create profile (choose the public key and add fields to encrypt)
   - Click Field-level encryption > Create configuration (set the profile as Default profile)
3. Attach it to your distribution:
   - Go to Distributions > select <example_resource_id>
   - Choose Behaviors > select Default (*) > Edit
   - Set Field-level encryption configuration to your created configuration
   - Click Save changes and wait for deployment

## 参考資料

- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/field-level-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/field-level-encryption-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/cloudfront_distributions_field_level_encryption_enabled/metadata.json](../../sources/aws/cloudfront_distributions_field_level_encryption_enabled/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_field_level_encryption_enabled/check.py](../../sources/aws/cloudfront_distributions_field_level_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_field_level_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_field_level_encryption_enabled/check.py`

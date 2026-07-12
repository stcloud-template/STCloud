# Kinesis Data Firehose delivery stream is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `firehose_stream_encrypted_at_rest` |
| クラウドプラットフォーム | AWS |
| サービス | firehose |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA) |
| リソースタイプ | AwsKinesisStream |
| リソースグループ | messaging |

## 説明

**Amazon Data Firehose** delivery streams must enable **server-side encryption at rest** with AWS KMS regardless of the source type. Encryption of upstream sources such as **Kinesis Data Streams** or **MSK** does not replace the need to protect the delivery stream itself.

## リスク

Unencrypted Firehose data at rest can be read if storage or backups are accessed, harming **confidentiality** and **integrity**. Disk-level access, snapshots, or misconfigured destinations enable data exfiltration or tampering. Lacking KMS-backed controls also reduces key rotation, segregation of duties, and auditability.

## 推奨事項

Enable **server-side encryption** for Firehose with AWS KMS. Prefer **customer managed keys** (`CMEK`) to enforce **least privilege**, rotation, and auditing. Ensure upstream **Kinesis** sources are encrypted and confirm MSK defaults meet policy. Monitor KMS health signals and deny writes without encryption. Apply **defense in depth** at destinations.

## 修正手順


### CLI

```text
aws firehose start-delivery-stream-encryption --delivery-stream-name <delivery-stream-name> --delivery-stream-encryption-configuration-input KeyType=AWS_OWNED_CMK
```

### Native IaC

```yaml
# CloudFormation: Enable at-rest encryption for a Firehose delivery stream
Resources:
  <example_resource_name>:
    Type: AWS::KinesisFirehose::DeliveryStream
    Properties:
      DeliveryStreamEncryptionConfigurationInput:
        KeyType: AWS_OWNED_CMK  # critical: enables SSE at rest using AWS owned KMS key
      ExtendedS3DestinationConfiguration:
        BucketARN: arn:aws:s3:::<example_resource_name>
        RoleARN: arn:aws:iam::<example_account_id>:role/<example_resource_name>
```

### Terraform

```hcl
# Terraform: Enable at-rest encryption for a Firehose delivery stream
resource "aws_kinesis_firehose_delivery_stream" "<example_resource_name>" {
  name        = "<example_resource_name>"
  destination = "extended_s3"

  server_side_encryption {
    enabled = true  # critical: turns on SSE at rest (uses AWS owned KMS key by default)
  }

  extended_s3_configuration {
    role_arn   = "arn:aws:iam::<example_account_id>:role/<example_resource_name>"
    bucket_arn = "arn:aws:s3:::<example_resource_name>"
  }
}
```

### Other

1. In the AWS Console, go to Amazon Data Firehose
2. Select the affected delivery stream and click Edit
3. Under Server-side encryption, set to Enabled (choose AWS owned key)
4. Click Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Firehose/delivery-stream-encrypted-with-kms-customer-master-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Firehose/delivery-stream-encrypted-with-kms-customer-master-keys.html)
- [https://docs.aws.amazon.com/firehose/latest/dev/encryption.html](https://docs.aws.amazon.com/firehose/latest/dev/encryption.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/datafirehose-controls.html#datafirehose-1](https://docs.aws.amazon.com/securityhub/latest/userguide/datafirehose-controls.html#datafirehose-1)

## 技術情報

- Source Metadata：[sources/aws/firehose_stream_encrypted_at_rest/metadata.json](../../sources/aws/firehose_stream_encrypted_at_rest/metadata.json)
- Source Code：[sources/aws/firehose_stream_encrypted_at_rest/check.py](../../sources/aws/firehose_stream_encrypted_at_rest/check.py)
- Source Metadata Path：`sources/aws/firehose_stream_encrypted_at_rest/metadata.json`
- Source Code Path：`sources/aws/firehose_stream_encrypted_at_rest/check.py`

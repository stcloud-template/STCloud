# Kinesis stream is encrypted at rest with KMS

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kinesis_stream_encrypted_at_rest` |
| クラウドプラットフォーム | AWS |
| サービス | kinesis |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsKinesisStream |
| リソースグループ | messaging |

## 説明

**Amazon Kinesis Data Streams** with **server-side encryption** use **AWS KMS** to protect records at rest. The evaluation determines whether a stream has `SSE-KMS` configured with a KMS key; streams lacking KMS-based at rest encryption are identified.

## リスク

Without **SSE-KMS**, records in shards may be exposed in plaintext if storage, backups, or analytics exports are accessed, undermining **confidentiality**. Absence of KMS controls also reduces **integrity** and oversight by removing key policies, rotation, and audit trails-enabling covert data exfiltration or insider misuse.

## 推奨事項

Enable **SSE-KMS** on all streams. - Use **customer-managed keys** for rotation and ownership - Enforce **least privilege** on KMS grants; limit cross-account use - Monitor key usage and require encryption in CI/CD

## 修正手順


### CLI

```text
aws kinesis start-stream-encryption --stream-name <KINESIS_STREAM_NAME> --encryption-type KMS --key-id alias/aws/kinesis
```

### Native IaC

```yaml
# CloudFormation: enable KMS encryption on a Kinesis stream
Resources:
  <example_resource_name>:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
      StreamEncryption:
        EncryptionType: KMS  # Critical: enables KMS encryption at rest
        KeyId: alias/aws/kinesis  # Critical: uses AWS managed Kinesis KMS key
```

### Terraform

```hcl
# Enable KMS encryption on a Kinesis stream
resource "aws_kinesis_stream" "<example_resource_name>" {
  name            = "<example_resource_name>"
  shard_count     = 1
  encryption_type = "KMS"            # Critical: enables KMS encryption at rest
  kms_key_id      = "alias/aws/kinesis" # Critical: uses AWS managed Kinesis KMS key
}
```

### Other

1. Open the AWS Console and go to Amazon Kinesis > Data streams
2. Select the stream
3. On the Details tab, click Edit in Server-side encryption
4. Select Enabled
5. Choose the (Default) aws/kinesis KMS key
6. Click Save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/kinesis-controls.html#kinesis-1](https://docs.aws.amazon.com/securityhub/latest/userguide/kinesis-controls.html#kinesis-1)
- [https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html](https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Kinesis/server-side-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Kinesis/server-side-encryption.html)

## 技術情報

- Source Metadata：[sources/aws/kinesis_stream_encrypted_at_rest/metadata.json](../../sources/aws/kinesis_stream_encrypted_at_rest/metadata.json)
- Source Code：[sources/aws/kinesis_stream_encrypted_at_rest/check.py](../../sources/aws/kinesis_stream_encrypted_at_rest/check.py)
- Source Metadata Path：`sources/aws/kinesis_stream_encrypted_at_rest/metadata.json`
- Source Code Path：`sources/aws/kinesis_stream_encrypted_at_rest/check.py`

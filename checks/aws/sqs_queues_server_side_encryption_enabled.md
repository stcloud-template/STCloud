# SQS queue has server-side encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqs_queues_server_side_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | sqs |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsSqsQueue |
| リソースグループ | messaging |

## 説明

**Amazon SQS queues** are evaluated for **server-side encryption** configured with a **KMS key** (`SSE-KMS`) protecting message bodies at rest. Queues without an associated KMS key are identified.

## リスク

Without **KMS-backed SSE**, message bodies lack tenant-controlled keys and detailed audit. Secrets, tokens, or PII in messages become easier to access through **privilege misuse**, misconfiguration, or unintended integrations, reducing **confidentiality** and limiting containment since you cannot revoke access via key disable/rotation.

## 推奨事項

Enable **SSE-KMS** on all queues using a **customer-managed KMS key**. - Apply **least privilege** to key and queue policies; restrict `Encrypt/Decrypt` - Enforce key rotation and separation of duties - Tune data key reuse for security vs. cost - Monitor key and queue access to support **defense in depth**

## 修正手順


### CLI

```text
aws sqs set-queue-attributes --queue-url <QUEUE_URL> --attributes KmsMasterKeyId=<KMS_KEY_ID_OR_ALIAS>
```

### Native IaC

```yaml
# CloudFormation: Enable SSE-KMS for an SQS queue
Resources:
  <example_resource_name>:
    Type: AWS::SQS::Queue
    Properties:
      KmsMasterKeyId: alias/aws/sqs  # Critical: sets a KMS key, enabling SSE-KMS so the queue reports a kms_key_id
```

### Terraform

```hcl
# Enable SSE-KMS for an SQS queue
resource "aws_sqs_queue" "<example_resource_name>" {
  kms_master_key_id = "alias/aws/sqs"  # Critical: sets a KMS key, enabling SSE-KMS so the queue reports a kms_key_id
}
```

### Other

1. In the AWS Console, go to Amazon SQS > Queues
2. Select the queue and click Edit
3. Expand Encryption
4. Set Server-side encryption to Enabled
5. For AWS KMS key, select alias/aws/sqs (or choose a specific KMS key)
6. Click Save

## 参考資料

- [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SQS/queue-encrypted-with-kms-customer-master-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SQS/queue-encrypted-with-kms-customer-master-keys.html)
- [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html)

## 技術情報

- Source Metadata：[sources/aws/sqs_queues_server_side_encryption_enabled/metadata.json](../../sources/aws/sqs_queues_server_side_encryption_enabled/metadata.json)
- Source Code：[sources/aws/sqs_queues_server_side_encryption_enabled/check.py](../../sources/aws/sqs_queues_server_side_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/sqs_queues_server_side_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/sqs_queues_server_side_encryption_enabled/check.py`

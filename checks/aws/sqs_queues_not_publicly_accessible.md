# SQS queue policy does not allow public access

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqs_queues_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | sqs |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsSqsQueue |
| リソースグループ | messaging |

## 説明

Amazon SQS queue policies are assessed for **public access**. The finding highlights queues with `Allow` statements using a wildcard `Principal` without restrictive conditions, compared to queues that only grant access to the owning account or explicitly trusted principals.

## リスク

**Public SQS access** can expose message data (**confidentiality**), enable unauthorized send/receive or tampering (**integrity**), and allow purge/delete operations that disrupt processing (**availability**). It may also trigger unbounded message ingestion, causing cost spikes and consumer overload.

## 推奨事項

Apply **least privilege** on SQS resource policies: - Avoid `Principal: *`; grant access only to specific accounts, roles, or services - Add restrictive conditions to tightly scope access - Prefer private connectivity and defense-in-depth controls - Review policies and audit activity regularly to prevent drift

## 修正手順


### CLI

```text
aws sqs set-queue-attributes --queue-url <example_queue_url> --attributes Policy='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"<example_account_id>"},"Action":"sqs:*","Resource":"<example_queue_arn>"}]}'
```

### Native IaC

```yaml
# CloudFormation: Restrict SQS policy to a specific principal (not public)
Resources:
  QueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      Queues:
        - "<example_queue_url>"
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS: "<example_account_id>" # CRITICAL: restrict access to a specific account (removes public "*")
            Action: "sqs:*"
            Resource: "<example_queue_arn>"
```

### Terraform

```hcl
# Restrict SQS policy to a specific principal (not public)
resource "aws_sqs_queue_policy" "<example_resource_name>" {
  queue_url = "<example_queue_url>"
  policy    = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "<example_account_id>" } # CRITICAL: restrict to a specific principal (removes public "*")
      Action    = "sqs:*"
      Resource  = "<example_queue_arn>"
    }]
  })
}
```

### Other

1. Open the Amazon SQS console and select the queue
2. Go to Permissions (Access policy) and click Edit
3. In the JSON policy, replace any "Principal": "*" with "Principal": { "AWS": "<your_account_id>" } or remove those public statements
4. Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SQS/sqs-queue-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SQS/sqs-queue-exposed.html)
- [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-examples-of-sqs-policies.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-examples-of-sqs-policies.html)

## 技術情報

- Source Metadata：[sources/aws/sqs_queues_not_publicly_accessible/metadata.json](../../sources/aws/sqs_queues_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/sqs_queues_not_publicly_accessible/check.py](../../sources/aws/sqs_queues_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/sqs_queues_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/sqs_queues_not_publicly_accessible/check.py`

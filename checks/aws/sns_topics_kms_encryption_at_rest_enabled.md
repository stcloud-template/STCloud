# SNS topic is encrypted at rest with KMS

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sns_topics_kms_encryption_at_rest_enabled` |
| 云平台 | AWS |
| 服务 | sns |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls |
| 资源类型 | AwsSnsTopic |
| 资源组 | messaging |

## 描述

**Amazon SNS topics** are assessed for **server-side encryption** with **AWS KMS**. Topics lacking a configured KMS key (e.g., missing `kms_master_key_id`) are identified as unencrypted at rest.

## 风险

Without KMS-backed SSE, SNS stores message bodies unencrypted at rest, undermining **confidentiality**. Privileged insiders or compromised service components could access plaintext during persistence windows, causing data exposure. You also lose KMS controls such as key policies, rotation, and detailed audit trails.

## 推荐措施

Enable **server-side encryption** on all SNS topics with **AWS KMS**; prefer **customer-managed keys** for control. Apply **least privilege** on key use, enforce rotation, and monitor key/access logs. Minimize sensitive data in messages and use end-to-end encryption *where feasible* to add defense in depth.

## 修复步骤


### CLI

```text
aws sns set-topic-attributes --topic-arn <TOPIC_ARN> --attribute-name KmsMasterKeyId --attribute-value alias/aws/sns
```

### Native IaC

```yaml
# CloudFormation: Enable SSE for an SNS topic
Resources:
  <example_resource_name>:
    Type: AWS::SNS::Topic
    Properties:
      KmsMasterKeyId: alias/aws/sns  # Critical: Enables encryption at rest with AWS managed KMS key
```

### Terraform

```hcl
# Enable SSE for an SNS topic
resource "aws_sns_topic" "<example_resource_name>" {
  name               = "<example_resource_name>"
  kms_master_key_id  = "alias/aws/sns" # Critical: Enables encryption at rest
}
```

### Other

1. Open the AWS Console and go to Amazon SNS > Topics
2. Select the topic and click Edit
3. Under Encryption, enable encryption and choose the AWS managed key for SNS (alias/aws/sns)
4. Click Save changes

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SNS/topic-encrypted-with-kms-customer-master-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SNS/topic-encrypted-with-kms-customer-master-keys.html)
- [https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html)

## 技术信息

- Source Metadata：[sources/aws/sns_topics_kms_encryption_at_rest_enabled/metadata.json](../../sources/aws/sns_topics_kms_encryption_at_rest_enabled/metadata.json)
- Source Code：[sources/aws/sns_topics_kms_encryption_at_rest_enabled/check.py](../../sources/aws/sns_topics_kms_encryption_at_rest_enabled/check.py)
- Source Metadata Path：`sources/aws/sns_topics_kms_encryption_at_rest_enabled/metadata.json`
- Source Code Path：`sources/aws/sns_topics_kms_encryption_at_rest_enabled/check.py`

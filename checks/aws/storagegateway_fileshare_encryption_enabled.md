# Storage Gateway file share is encrypted with KMS CMK

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storagegateway_fileshare_encryption_enabled` |
| 云平台 | AWS |
| 服务 | storagegateway |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Software and Configuration Checks/Industry and Regulatory Standards/SOC 2, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA), Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | storage |

## 描述

Storage Gateway file shares configured with **customer-managed KMS keys (CMKs)** for server-side encryption of objects written to S3. File shares without an explicit KMS key (e.g., `SSE-KMS` or `DSSE-KMS`) are identified.

## 风险

Without **CMEK**, encryption relies on provider-managed keys, reducing control over who can decrypt and when. This weakens confidentiality by limiting key-policy enforcement, revocation, and auditable key use, increasing exposure from stolen S3 credentials or overly permissive roles.

## 推荐措施

Use a **customer-managed KMS key** for each file share's server-side encryption (`SSE-KMS`; *consider* `DSSE-KMS` for multilayer needs). Apply **least privilege** and **separation of duties** to key access, rotate keys, monitor key usage, and restrict scope to necessary principals and regions.

## 修复步骤


### CLI

```text
aws storagegateway update-nfs-file-share --file-share-arn <example_resource_arn> --kms-encrypted --kms-key <example_kms_key_arn>
```

### Native IaC

```yaml
# CloudFormation: enable KMS CMK encryption for a Storage Gateway NFS file share
Resources:
  <example_resource_name>:
    Type: AWS::StorageGateway::NFSFileShare
    Properties:
      ClientToken: "<example_resource_id>"
      GatewayARN: "<example_resource_arn>"
      LocationARN: "<example_resource_arn>"
      Role: "<example_resource_arn>"
      KMSEncrypted: true  # Critical: enables KMS CMK encryption for the file share
      KMSKey: "<example_kms_key_arn>"  # Critical: CMK ARN used for encryption
```

### Terraform

```hcl
# Enable KMS CMK encryption for a Storage Gateway NFS file share
resource "aws_storagegateway_nfs_file_share" "<example_resource_name>" {
  client_list  = ["<example_cidr_block>"]
  gateway_arn  = "<example_resource_arn>"
  location_arn = "<example_resource_arn>"
  role_arn     = "<example_resource_arn>"

  kms_encrypted = true              # Critical: enables KMS CMK encryption
  kms_key_arn   = "<example_kms_key_arn>"  # Critical: CMK ARN used for encryption
}
```

### Other

1. In the AWS Console, go to Storage Gateway > File shares
2. Select the affected file share and click Edit
3. Under Encryption, choose AWS KMS key
4. Select the CMK to use (or paste its ARN)
5. Save changes

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/StorageGateway/file-shares-encrypted-with-cmk.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/StorageGateway/file-shares-encrypted-with-cmk.html#)
- [https://docs.aws.amazon.com/filegateway/latest/files3/encrypt-objects-stored-by-file-gateway-in-amazon-s3.html](https://docs.aws.amazon.com/filegateway/latest/files3/encrypt-objects-stored-by-file-gateway-in-amazon-s3.html)

## 技术信息

- Source Metadata：[sources/aws/storagegateway_fileshare_encryption_enabled/metadata.json](../../sources/aws/storagegateway_fileshare_encryption_enabled/metadata.json)
- Source Code：[sources/aws/storagegateway_fileshare_encryption_enabled/check.py](../../sources/aws/storagegateway_fileshare_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/storagegateway_fileshare_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/storagegateway_fileshare_encryption_enabled/check.py`

# EFS file system has encryption at rest enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `efs_encryption_at_rest_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | efs |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Effects/Data Exposure |
| リソースタイプ | AwsEfsFileSystem |
| リソースグループ | storage |

## 説明

**Amazon EFS file system** has **encryption at rest** enabled using AWS KMS to protect file data and metadata stored on the service

## リスク

Without encryption at rest, EFS contents can be read from storage media, backups, or compromised hosts, eroding **confidentiality** and enabling offline exfiltration. Privileged compromise also allows covert data harvesting or manipulation, threatening **integrity** of files.

## 推奨事項

Enable **encryption at rest** for all EFS file systems and prefer **customer-managed KMS keys** for control, rotation, and audit. Apply **least privilege** to key policies and separate key management duties. *For existing unencrypted data*, migrate to a new encrypted file system. Enforce creation policies (IAM/SCP) to prevent non-encrypted deployments.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create an EFS file system with encryption at rest enabled
Resources:
  <example_resource_name>:
    Type: AWS::EFS::FileSystem
    Properties:
      Encrypted: true  # Critical: enables encryption at rest so the check passes
```

### Terraform

```hcl
# Terraform: Create an EFS file system with encryption at rest enabled
resource "aws_efs_file_system" "<example_resource_name>" {
  encrypted = true  # Critical: enables encryption at rest so the check passes
}
```

### Other

1. In the AWS Console, go to Amazon EFS
2. Click Create file system
3. Check Enable encryption (leave default key or choose a KMS key if required)
4. Click Create
5. Migrate data from the unencrypted file system to the new encrypted one
6. Delete the unencrypted file system to clear the failing finding

## 参考資料

- [https://repost.aws/knowledge-center/efs-turn-on-encryption-at-rest](https://repost.aws/knowledge-center/efs-turn-on-encryption-at-rest)
- [https://docs.aws.amazon.com/efs/latest/ug/EFSKMS.html](https://docs.aws.amazon.com/efs/latest/ug/EFSKMS.html)
- [https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html](https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html)

## 技術情報

- Source Metadata：[sources/aws/efs_encryption_at_rest_enabled/metadata.json](../../sources/aws/efs_encryption_at_rest_enabled/metadata.json)
- Source Code：[sources/aws/efs_encryption_at_rest_enabled/check.py](../../sources/aws/efs_encryption_at_rest_enabled/check.py)
- Source Metadata Path：`sources/aws/efs_encryption_at_rest_enabled/metadata.json`
- Source Code Path：`sources/aws/efs_encryption_at_rest_enabled/check.py`

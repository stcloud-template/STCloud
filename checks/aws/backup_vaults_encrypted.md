# AWS Backup vault is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `backup_vaults_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | backup |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA) |
| リソースタイプ | AwsBackupBackupVault |
| リソースグループ | storage |

## 説明

**AWS Backup vaults** are evaluated for **encryption at rest** with **AWS KMS**. The finding highlights vaults without a configured KMS key protecting stored recovery points.

## リスク

Unencrypted vaults allow recovery points to be read if storage or credentials are compromised, undermining **confidentiality** and enabling data exfiltration. Missing KMS controls also weaken **integrity** guarantees and impede forensic **auditability** during investigations.

## 推奨事項

Encrypt every backup vault with **customer-managed KMS keys** (`CMK`). Enforce **least privilege** in key policies, enable rotation, and separate key admins from backup operators. Add **defense-in-depth** with vault lock and logging. *For copies*, ensure destination vaults use appropriate KMS keys.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Encrypted AWS Backup Vault
Resources:
  <example_resource_name>:
    Type: AWS::Backup::BackupVault
    Properties:
      BackupVaultName: <example_resource_name>
      EncryptionKeyArn: <kms_key_arn>  # CRITICAL: sets KMS key to encrypt the vault at rest
```

### Terraform

```hcl
# Encrypted AWS Backup Vault
resource "aws_backup_vault" "<example_resource_name>" {
  name        = "<example_resource_name>"
  kms_key_arn = "<kms_key_arn>"  # CRITICAL: enables encryption at rest for the vault
}
```

### Other

1. In the AWS Console, go to AWS Backup > Backup vaults
2. Click Create backup vault
3. Set Name to <example_resource_name>
4. Under Encryption key, select a customer managed KMS key (<kms_key_arn>)
5. Click Create backup vault
6. Update any Backup plans to use the new vault (Plans > select plan > Edit > change Target vault name)
7. Delete the old unencrypted vault after it is empty (select vault > Delete backup vault)

## 参考資料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Athena/encrypted-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Athena/encrypted-with-cmk.html)

## 技術情報

- Source Metadata：[sources/aws/backup_vaults_encrypted/metadata.json](../../sources/aws/backup_vaults_encrypted/metadata.json)
- Source Code：[sources/aws/backup_vaults_encrypted/check.py](../../sources/aws/backup_vaults_encrypted/check.py)
- Source Metadata Path：`sources/aws/backup_vaults_encrypted/metadata.json`
- Source Code Path：`sources/aws/backup_vaults_encrypted/check.py`

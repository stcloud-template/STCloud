# At least one AWS Backup vault exists

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `backup_vaults_exist` |
| クラウドプラットフォーム | AWS |
| サービス | backup |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsBackupBackupVault |
| リソースグループ | storage |

## 説明

**AWS Backup** in the account/region includes at least one **backup vault** that stores and organizes recovery points for use by backup plans and copies.

## リスク

Without a vault, recovery points cannot be created or retained in AWS Backup, degrading **availability** and **integrity**. Data may be irrecoverable after deletion, ransomware, or misconfiguration, and RPO/RTO targets may be missed during incidents.

## 推奨事項

Create and maintain a **backup vault** in each required region. Enforce **least privilege** access, encrypt with **KMS CMKs**, and enable **Vault Lock** to prevent tampering. Use lifecycle rules and cross-region/cross-account copies, and regularly test restores for **defense in depth**.

## 修正手順


### CLI

```text
aws backup create-backup-vault --backup-vault-name <example_resource_name>
```

### Native IaC

```yaml
# CloudFormation: create a Backup Vault
Resources:
  BackupVault:
    Type: AWS::Backup::BackupVault
    Properties:
      VaultName: <example_resource_name>  # Critical: creates a backup vault to satisfy the check
```

### Terraform

```hcl
# Create a Backup Vault
resource "aws_backup_vault" "<example_resource_name>" {
  name = "<example_resource_name>" # Critical: ensures at least one backup vault exists
}
```

### Other

1. Sign in to the AWS Management Console and open the AWS Backup console
2. In the left navigation pane, select Backup vaults
3. Click Create backup vault
4. Enter a name (e.g., <example_resource_name>)
5. Click Create backup vault

## 参考資料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/vaults.html)

## 技術情報

- Source Metadata：[sources/aws/backup_vaults_exist/metadata.json](../../sources/aws/backup_vaults_exist/metadata.json)
- Source Code：[sources/aws/backup_vaults_exist/check.py](../../sources/aws/backup_vaults_exist/check.py)
- Source Metadata Path：`sources/aws/backup_vaults_exist/metadata.json`
- Source Code Path：`sources/aws/backup_vaults_exist/check.py`

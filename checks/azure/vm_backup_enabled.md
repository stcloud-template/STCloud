# Ensure Backups are enabled for Azure Virtual Machines

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_backup_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure that Microsoft Azure Backup service is in use for your Azure virtual machines (VMs) to protect against accidental deletion or corruption.

## リスク

Without Azure Backup enabled, VMs are at risk of data loss due to accidental deletion, corruption, or other failures, and recovery options are limited.

## 推奨事項

Enable Azure Backup for each VM by associating it with a Recovery Services vault and a backup policy.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 修正手順


### CLI

```text
az backup protection enable-for-vm --resource-group <resource-group> --vm <vm-name> --vault-name <vault-name> --policy-name DefaultPolicy
```

### Other

[https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/backup/backup-overview](https://docs.microsoft.com/en-us/azure/backup/backup-overview)
- [https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 技術情報

- Source Metadata：[sources/azure/vm_backup_enabled/metadata.json](../../sources/azure/vm_backup_enabled/metadata.json)
- Source Code：[sources/azure/vm_backup_enabled/check.py](../../sources/azure/vm_backup_enabled/check.py)
- Source Metadata Path：`sources/azure/vm_backup_enabled/metadata.json`
- Source Code Path：`sources/azure/vm_backup_enabled/check.py`

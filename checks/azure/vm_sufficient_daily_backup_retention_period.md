# Ensure there is a sufficient daily backup retention period configured for Azure virtual machines.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_sufficient_daily_backup_retention_period` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure there is a sufficient daily backup retention period configured for Azure virtual machines.

## リスク

Having an optimal daily backup retention period for your Azure virtual machines will enforce your backup strategy to follow the best practices as specified in the compliance regulations promoted by your organization. Retaining VM backups for a longer period of time will allow you to handle more efficiently your data restoration process in the event of a failure.

## 推奨事項

Set the daily backup retention period for each VM's backup policy to meet or exceed your organization's minimum requirement.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction](https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sufficient-backup-retention-period.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sufficient-backup-retention-period.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction](https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)

## 技術情報

- Source Metadata：[sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json](../../sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json)
- Source Code：[sources/azure/vm_sufficient_daily_backup_retention_period/check.py](../../sources/azure/vm_sufficient_daily_backup_retention_period/check.py)
- Source Metadata Path：`sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json`
- Source Code Path：`sources/azure/vm_sufficient_daily_backup_retention_period/check.py`

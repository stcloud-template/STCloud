# Ensure Backups are enabled for Azure Virtual Machines

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_backup_enabled` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure that Microsoft Azure Backup service is in use for your Azure virtual machines (VMs) to protect against accidental deletion or corruption.

## 风险

Without Azure Backup enabled, VMs are at risk of data loss due to accidental deletion, corruption, or other failures, and recovery options are limited.

## 推荐措施

Enable Azure Backup for each VM by associating it with a Recovery Services vault and a backup policy.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 修复步骤


### CLI

```text
az backup protection enable-for-vm --resource-group <resource-group> --vm <vm-name> --vault-name <vault-name> --policy-name DefaultPolicy
```

### Other

[https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://learn.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/backup/backup-overview](https://docs.microsoft.com/en-us/azure/backup/backup-overview)
- [https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal](https://docs.microsoft.com/en-us/azure/backup/quick-backup-vm-portal)

## 技术信息

- Source Metadata：[sources/azure/vm_backup_enabled/metadata.json](../../sources/azure/vm_backup_enabled/metadata.json)
- Source Code：[sources/azure/vm_backup_enabled/check.py](../../sources/azure/vm_backup_enabled/check.py)
- Source Metadata Path：`sources/azure/vm_backup_enabled/metadata.json`
- Source Code Path：`sources/azure/vm_backup_enabled/check.py`

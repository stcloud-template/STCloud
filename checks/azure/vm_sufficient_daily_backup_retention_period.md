# Ensure there is a sufficient daily backup retention period configured for Azure virtual machines.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_sufficient_daily_backup_retention_period` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure there is a sufficient daily backup retention period configured for Azure virtual machines.

## 风险

Having an optimal daily backup retention period for your Azure virtual machines will enforce your backup strategy to follow the best practices as specified in the compliance regulations promoted by your organization. Retaining VM backups for a longer period of time will allow you to handle more efficiently your data restoration process in the event of a failure.

## 推荐措施

Set the daily backup retention period for each VM's backup policy to meet or exceed your organization's minimum requirement.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction](https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sufficient-backup-retention-period.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sufficient-backup-retention-period.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction](https://docs.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)

## 技术信息

- Source Metadata：[sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json](../../sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json)
- Source Code：[sources/azure/vm_sufficient_daily_backup_retention_period/check.py](../../sources/azure/vm_sufficient_daily_backup_retention_period/check.py)
- Source Metadata Path：`sources/azure/vm_sufficient_daily_backup_retention_period/metadata.json`
- Source Code Path：`sources/azure/vm_sufficient_daily_backup_retention_period/check.py`

# Ensure that Network Security Group Flow Log retention period is 0, 90 days or greater

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_flow_log_more_than_90_days` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Network Security Group Flow Logs should be enabled and the retention period set to greater than or equal to 90 days.

## 风险

Flow logs enable capturing information about IP traffic flowing in and out of network security groups. Logs can be used to check for anomalies and give insight into suspected breaches.

## 推荐措施

From Azure Portal 1. Go to Network Watcher 2. Select NSG flow logs blade in the Logs section 3. Select each Network Security Group from the list 4. Ensure Status is set to On 5. Ensure Retention (days) setting greater than 90 days 6. Select your storage account in the Storage account field 7. Select Save From Azure CLI Enable the NSG flow logs and set the Retention (days) to greater than or equal to 90 days. az network watcher flow-log configure --nsg <NameorID of the Network Security Group> --enabled true --resource-group <resourceGroupName> --retention 91 --storage-account <NameorID of the storage account to save flow logs>

- 推荐链接：[https://docs.microsoft.com/en-us/cli/azure/network/watcher/flow-log?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/network/watcher/flow-log?view=azure-cli-latest)

## 修复步骤


### CLI

```text
az network watcher flow-log configure --nsg <NameorID of the Network Security Group> --enabled true --resource-group <resourceGroupName> --retention 91 -- storage-account <NameorID of the storage account to save flow logs>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_1#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/sufficient-nsg-flow-log-retention-period.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/sufficient-nsg-flow-log-retention-period.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-overview)
- [https://docs.microsoft.com/en-us/cli/azure/network/watcher/flow-log?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/network/watcher/flow-log?view=azure-cli-latest)

## 技术信息

- Source Metadata：[sources/azure/network_flow_log_more_than_90_days/metadata.json](../../sources/azure/network_flow_log_more_than_90_days/metadata.json)
- Source Code：[sources/azure/network_flow_log_more_than_90_days/check.py](../../sources/azure/network_flow_log_more_than_90_days/check.py)
- Source Metadata Path：`sources/azure/network_flow_log_more_than_90_days/metadata.json`
- Source Code Path：`sources/azure/network_flow_log_more_than_90_days/check.py`

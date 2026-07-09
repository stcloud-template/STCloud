# Ensure that logging for Azure Key Vault is 'Enabled'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `keyvault_logging_enabled` |
| 云平台 | Azure |
| 服务 | keyvault |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | KeyVault |
| 资源组 | security |

## 描述

Enable AuditEvent logging for key vault instances to ensure interactions with key vaults are logged and available.

## 风险

Monitoring how and when key vaults are accessed, and by whom, enables an audit trail of interactions with confidential information, keys, and certificates managed by Azure Keyvault. Enabling logging for Key Vault saves information in an Azure storage account which the user provides. This creates a new container named insights-logs-auditevent automatically for the specified storage account. This same storage account can be used for collecting logs for multiple key vaults.

## 推荐措施

1. Go to Key vaults 2. For each Key vault 3. Go to Diagnostic settings 4. Click on Edit Settings 5. Ensure that Archive to a storage account is Enabled 6. Ensure that AuditEvent is checked, and the retention days is set to 180 days or as appropriate

- 推荐链接：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-8-ensure-security-of-key-and-certificate-repository](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-8-ensure-security-of-key-and-certificate-repository)

## 修复步骤


### CLI

```text
az monitor diagnostic-settings create --name <diagnostic settings name> --resource <key vault resource ID> --logs'[{category:AuditEvents,enabled:true,retention-policy:{enabled:true,days:180}}]' --metrics'[{category:AllMetrics,enabled:true,retention-policy:{enabled:true,days:180}}]' <[--event-hub <event hub ID> --event-hub-rule <event hub auth rule ID> | --storage-account <storage account ID> |--workspace <log analytics workspace ID> | --marketplace-partner-id <full resource ID of third-party solution>]>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/KeyVault/enable-audit-event-logging-for-azure-key-vaults.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/KeyVault/enable-audit-event-logging-for-azure-key-vaults.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/key-vault/key-vault-logging](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-logging)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-8-ensure-security-of-key-and-certificate-repository](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-8-ensure-security-of-key-and-certificate-repository)

## 技术信息

- Source Metadata：[sources/azure/keyvault_logging_enabled/metadata.json](../../sources/azure/keyvault_logging_enabled/metadata.json)
- Source Code：[sources/azure/keyvault_logging_enabled/check.py](../../sources/azure/keyvault_logging_enabled/check.py)
- Source Metadata Path：`sources/azure/keyvault_logging_enabled/metadata.json`
- Source Code Path：`sources/azure/keyvault_logging_enabled/check.py`

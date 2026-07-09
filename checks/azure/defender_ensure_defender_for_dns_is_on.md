# Ensure That Microsoft Defender for DNS Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_dns_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for DNS Is Set To 'On'

## 风险

DNS lookups within a subscription are scanned and compared to a dynamic list of websites that might be potential security threats. These threats could be a result of a security breach within your services, thus scanning for them could prevent a potential security threat from being introduced.

## 推荐措施

By default, Microsoft Defender for Cloud is not enabled for your App Service instances. Enabling the Defender security service for App Service instances allows for advanced security defense using threat detection capabilities provided by Microsoft Security Response Center.

## 修复步骤

No remediation steps available.

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_dns_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_dns_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_dns_is_on/check.py](../../sources/azure/defender_ensure_defender_for_dns_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_dns_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_dns_is_on/check.py`

# Ensure that Endpoint Protection for all Virtual Machines is installed

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_assessments_vm_endpoint_protection_installed` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Security/assessments |
| 资源组 | security |

## 描述

Install endpoint protection for all virtual machines.

## 风险

Installing endpoint protection systems (like anti-malware for Azure) provides for real-time protection capability that helps identify and remove viruses, spyware, and other malicious software. These also offer configurable alerts when known-malicious or unwanted software attempts to install itself or run on Azure systems.

## 推荐措施

Follow Microsoft Azure documentation to install endpoint protection from the security center. Alternatively, you can employ your own endpoint protection tool for your OS.

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/install-endpoint-protection.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/install-endpoint-protection.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/security/fundamentals/antimalware](https://learn.microsoft.com/en-us/azure/security/fundamentals/antimalware)

## 技术信息

- Source Metadata：[sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json](../../sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json)
- Source Code：[sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py](../../sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py)
- Source Metadata Path：`sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json`
- Source Code Path：`sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py`

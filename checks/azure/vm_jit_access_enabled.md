# Enable Just-In-Time Access for Virtual Machines

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_jit_access_enabled` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure that Microsoft Azure virtual machines are configured to use Just-in-Time (JIT) access.

## 风险

Without JIT access, management ports such as 22 (SSH) and 3389 (RDP) may be exposed, increasing the risk of brute-force and DDoS attacks.

## 推荐措施

Enable Just-in-Time (JIT) network access for your Microsoft Azure virtual machines using the Azure Portal under Security Center > Just-in-time VM access.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc](https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc)

## 修复步骤


### CLI

```text
az security jit-policy list --query '[*].virtualMachines[*].id | []'
```

## 参考资料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc](https://docs.microsoft.com/en-us/azure/security-center/security-center-just-in-time?tabs=jit-config-asc%2Cjit-request-asc)

## 技术信息

- Source Metadata：[sources/azure/vm_jit_access_enabled/metadata.json](../../sources/azure/vm_jit_access_enabled/metadata.json)
- Source Code：[sources/azure/vm_jit_access_enabled/check.py](../../sources/azure/vm_jit_access_enabled/check.py)
- Source Metadata Path：`sources/azure/vm_jit_access_enabled/metadata.json`
- Source Code Path：`sources/azure/vm_jit_access_enabled/check.py`

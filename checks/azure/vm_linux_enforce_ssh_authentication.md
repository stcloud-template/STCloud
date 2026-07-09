# Ensure SSH key authentication is enforced on Linux-based Virtual Machines

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_linux_enforce_ssh_authentication` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure that Azure Linux-based virtual machines are configured to use SSH keys by disabling password authentication.

## 风险

Allowing password-based SSH authentication increases the risk of brute-force attacks and unauthorized access. Enforcing SSH key authentication ensures only users with the private key can access the VM.

## 推荐措施

Recreate Linux VMs with SSH key authentication enabled and password authentication disabled.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/ssh-authentication-type.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/ssh-authentication-type.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

## 技术信息

- Source Metadata：[sources/azure/vm_linux_enforce_ssh_authentication/metadata.json](../../sources/azure/vm_linux_enforce_ssh_authentication/metadata.json)
- Source Code：[sources/azure/vm_linux_enforce_ssh_authentication/check.py](../../sources/azure/vm_linux_enforce_ssh_authentication/check.py)
- Source Metadata Path：`sources/azure/vm_linux_enforce_ssh_authentication/metadata.json`
- Source Code Path：`sources/azure/vm_linux_enforce_ssh_authentication/check.py`

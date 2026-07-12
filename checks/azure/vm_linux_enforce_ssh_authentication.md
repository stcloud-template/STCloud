# Ensure SSH key authentication is enforced on Linux-based Virtual Machines

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_linux_enforce_ssh_authentication` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure that Azure Linux-based virtual machines are configured to use SSH keys by disabling password authentication.

## リスク

Allowing password-based SSH authentication increases the risk of brute-force attacks and unauthorized access. Enforcing SSH key authentication ensures only users with the private key can access the VM.

## 推奨事項

Recreate Linux VMs with SSH key authentication enabled and password authentication disabled.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/ssh-authentication-type.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/ssh-authentication-type.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

## 技術情報

- Source Metadata：[sources/azure/vm_linux_enforce_ssh_authentication/metadata.json](../../sources/azure/vm_linux_enforce_ssh_authentication/metadata.json)
- Source Code：[sources/azure/vm_linux_enforce_ssh_authentication/check.py](../../sources/azure/vm_linux_enforce_ssh_authentication/check.py)
- Source Metadata Path：`sources/azure/vm_linux_enforce_ssh_authentication/metadata.json`
- Source Code Path：`sources/azure/vm_linux_enforce_ssh_authentication/check.py`

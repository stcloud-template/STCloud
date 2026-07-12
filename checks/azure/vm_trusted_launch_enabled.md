# Ensure Trusted Launch is enabled on Virtual Machines

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_trusted_launch_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

When Secure Boot and vTPM are enabled together, they provide a strong foundation for protecting your VM from boot attacks. For example, if an attacker attempts to replace the bootloader with a malicious version, Secure Boot will prevent the VM from booting. If the attacker is able to bypass Secure Boot and install a malicious bootloader, vTPM can be used to detect the intrusion and alert you.

## リスク

Secure Boot and vTPM work together to protect your VM from a variety of boot attacks, including bootkits, rootkits, and firmware rootkits. Not enabling Trusted Launch in Azure VM can lead to increased vulnerability to rootkits and boot-level malware, reduced ability to detect and prevent unauthorized changes to the boot process, and a potential compromise of system integrity and data security.

## 推奨事項

1. Go to Virtual Machines 2. For each VM, under Settings, click on Configuration on the left blade 3. Under Security Type, select 'Trusted Launch Virtual Machines' 4. Make sure Enable Secure Boot & Enable vTPM are checked 5. Click on Apply.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal#enable-trusted-launch-on-existing-vm](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal#enable-trusted-launch-on-existing-vm)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal)
- [https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal#enable-trusted-launch-on-existing-vm](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch-existing-vm?tabs=portal#enable-trusted-launch-on-existing-vm)

## 技術情報

- Source Metadata：[sources/azure/vm_trusted_launch_enabled/metadata.json](../../sources/azure/vm_trusted_launch_enabled/metadata.json)
- Source Code：[sources/azure/vm_trusted_launch_enabled/check.py](../../sources/azure/vm_trusted_launch_enabled/check.py)
- Source Metadata Path：`sources/azure/vm_trusted_launch_enabled/metadata.json`
- Source Code Path：`sources/azure/vm_trusted_launch_enabled/check.py`

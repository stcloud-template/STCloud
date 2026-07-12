# Ensure that Endpoint Protection for all Virtual Machines is installed

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_assessments_vm_endpoint_protection_installed` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Security/assessments |
| リソースグループ | security |

## 説明

Install endpoint protection for all virtual machines.

## リスク

Installing endpoint protection systems (like anti-malware for Azure) provides for real-time protection capability that helps identify and remove viruses, spyware, and other malicious software. These also offer configurable alerts when known-malicious or unwanted software attempts to install itself or run on Azure systems.

## 推奨事項

Follow Microsoft Azure documentation to install endpoint protection from the security center. Alternatively, you can employ your own endpoint protection tool for your OS.

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/install-endpoint-protection.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/install-endpoint-protection.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/security/fundamentals/antimalware](https://learn.microsoft.com/en-us/azure/security/fundamentals/antimalware)

## 技術情報

- Source Metadata：[sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json](../../sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json)
- Source Code：[sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py](../../sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py)
- Source Metadata Path：`sources/azure/defender_assessments_vm_endpoint_protection_installed/metadata.json`
- Source Code Path：`sources/azure/defender_assessments_vm_endpoint_protection_installed/check.py`

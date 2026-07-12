# Ensure That Microsoft Defender for Storage Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_storage_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for Storage Is Set To 'On'

## リスク

Ensure that Microsoft Defender for Cloud is enabled for your Microsoft Azure storage accounts. Defender for storage accounts is an Azure-native layer of security intelligence that detects unusual and potentially harmful attempts to access or exploit your Azure cloud storage accounts.

## 推奨事項

By default, Microsoft Defender for Cloud is disabled for your storage accounts. Enabling the Defender security service for Azure storage accounts allows for advanced security defense using threat detection capabilities provided by the Microsoft Security Response Center (MSRC). MSRC investigates all reports of security vulnerabilities affecting Microsoft products and services, including Azure cloud services.

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-storage#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-storage#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-storage.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-storage.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_storage_is_on/check.py](../../sources/azure/defender_ensure_defender_for_storage_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_storage_is_on/check.py`

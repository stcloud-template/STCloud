# Ensure that 'Enable Infrastructure Encryption' for Each Storage Account in Azure Storage is Set to 'enabled'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_infrastructure_encryption_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | low |
| カテゴリ | encryption |
| リソースタイプ | AzureRole |
| リソースグループ | IAM |

## 説明

Ensure that 'Enable Infrastructure Encryption' for Each Storage Account in Azure Storage is Set to 'enabled'

## リスク

Double encryption of Azure Storage data protects against a scenario where one of the encryption algorithms or keys may be compromised

## 推奨事項

Enabling double encryption at the hardware level on top of the default software encryption for Storage Accounts accessing Azure storage solutions.

## 修正手順

No remediation steps available.

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json](../../sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_infrastructure_encryption_is_enabled/check.py](../../sources/azure/storage_infrastructure_encryption_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_infrastructure_encryption_is_enabled/check.py`

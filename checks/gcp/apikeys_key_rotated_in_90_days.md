# Ensure API Keys Are Rotated Every 90 Days

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apikeys_key_rotated_in_90_days` |
| クラウドプラットフォーム | GCP |
| サービス | apikeys |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | API Key |
| リソースグループ | IAM |

## 説明

API Keys should only be used for services in cases where other authentication methods are unavailable. If they are in use it is recommended to rotate API keys every 90 days.

## リスク

Once a Google Cloud API key is compromised, it can be used indefinitely unless the project owner revokes or regenerates that key.

## 推奨事項

Ensure that all your Google Cloud API keys are regularly regenerated (rotated) in order to meet security and compliance requirements. By default, it is recommended to rotate keys every 90 days. Google Cloud Platform (GCP) API keys are simple, encrypted strings that can be used when calling specific APIs that don't need to access private user data. API keys are typically used to track API requests associated with your GCP project for quota and billing. Rotating GCP API keys will substantially reduce the window of opportunity for exploits and ensure that data can't be accessed with an outdated key that might have been lost, cracked, or stolen.

- 推奨リンク：[https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/rotate-api-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/rotate-api-keys.html)

## 参考資料

- [https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 技術情報

- Source Metadata：[sources/gcp/apikeys_key_rotated_in_90_days/metadata.json](../../sources/gcp/apikeys_key_rotated_in_90_days/metadata.json)
- Source Code：[sources/gcp/apikeys_key_rotated_in_90_days/check.py](../../sources/gcp/apikeys_key_rotated_in_90_days/check.py)
- Source Metadata Path：`sources/gcp/apikeys_key_rotated_in_90_days/metadata.json`
- Source Code Path：`sources/gcp/apikeys_key_rotated_in_90_days/check.py`

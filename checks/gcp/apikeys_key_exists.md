# Ensure API Keys Only Exist for Active Services

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apikeys_key_exists` |
| クラウドプラットフォーム | GCP |
| サービス | apikeys |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | API Key |
| リソースグループ | IAM |

## 説明

API Keys should only be used for services in cases where other authentication methods are unavailable. Unused keys with their permissions in tact may still exist within a project. Keys are insecure because they can be viewed publicly, such as from within a browser, or they can be accessed on a device where the key resides. It is recommended to use standard authentication flow instead.

## リスク

Security risks involved in using API-Keys appear below: API keys are simple encrypted strings, API keys do not identify the user or the application making the API request, API keys are typically accessible to clients, making it easy to discover and steal an API key.

## 推奨事項

To avoid the security risk in using API keys, it is recommended to use standard authentication flow instead.

- 推奨リンク：[https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 修正手順


### CLI

```text
gcloud alpha services api-keys delete
```

## 参考資料

- [https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 技術情報

- Source Metadata：[sources/gcp/apikeys_key_exists/metadata.json](../../sources/gcp/apikeys_key_exists/metadata.json)
- Source Code：[sources/gcp/apikeys_key_exists/check.py](../../sources/gcp/apikeys_key_exists/check.py)
- Source Metadata Path：`sources/gcp/apikeys_key_exists/metadata.json`
- Source Code Path：`sources/gcp/apikeys_key_exists/check.py`

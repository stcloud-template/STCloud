# Ensure User-Managed/External Keys for Service Accounts Are Rotated Every 90 Days

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_sa_user_managed_key_rotate_90_days` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | ServiceAccountKey |
| リソースグループ | IAM |

## 説明

Ensure User-Managed/External Keys for Service Accounts Are Rotated Every 90 Days

## リスク

Service Account keys should be rotated to ensure that data cannot be accessed with an old key that might have been lost, cracked, or stolen.

## 推奨事項

It is recommended that all Service Account keys are regularly rotated.

- 推奨リンク：[https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/rotate-service-account-user-managed-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/rotate-service-account-user-managed-keys.html)

## 参考資料

- [https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 技術情報

- Source Metadata：[sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json](../../sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json)
- Source Code：[sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py](../../sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py)
- Source Metadata Path：`sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json`
- Source Code Path：`sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py`

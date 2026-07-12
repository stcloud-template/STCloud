# Ensure That There Are Only GCP-Managed Service Account Keys for Each Service Account

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_sa_no_user_managed_keys` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | ServiceAccountKey |
| リソースグループ | IAM |

## 説明

Ensure That There Are Only GCP-Managed Service Account Keys for Each Service Account

## リスク

Anyone who has access to the keys will be able to access resources through the service account. GCP-managed keys are used by Cloud Platform services such as App Engine and Compute Engine. These keys cannot be downloaded. Google will keep the keys and automatically rotate them on an approximately weekly basis. User-managed keys are created, downloadable, and managed by users.

## 推奨事項

It is recommended to prevent user-managed service account keys.

- 推奨リンク：[https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/delete-user-managed-service-account-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/delete-user-managed-service-account-keys.html)

## 参考資料

- [https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 技術情報

- Source Metadata：[sources/gcp/iam_sa_no_user_managed_keys/metadata.json](../../sources/gcp/iam_sa_no_user_managed_keys/metadata.json)
- Source Code：[sources/gcp/iam_sa_no_user_managed_keys/check.py](../../sources/gcp/iam_sa_no_user_managed_keys/check.py)
- Source Metadata Path：`sources/gcp/iam_sa_no_user_managed_keys/metadata.json`
- Source Code Path：`sources/gcp/iam_sa_no_user_managed_keys/check.py`

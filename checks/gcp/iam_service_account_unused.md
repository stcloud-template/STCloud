# Ensure That There Are No Unused Service Accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_service_account_unused` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | ServiceAccount |
| リソースグループ | IAM |

## 説明

Ensure That There Are No Unused Service Accounts.

## リスク

A malicious actor could make use of privilege escalation or impersonation to access an unused Service Account that is over-privileged.

## 推奨事項

It is recommended to disable or remove unused Service Accounts.

- 推奨リンク：[https://cloud.google.com/iam/docs/service-account-overview#identify-unused](https://cloud.google.com/iam/docs/service-account-overview#identify-unused)

## 修正手順

No remediation steps available.

## 参考資料

- [https://cloud.google.com/iam/docs/service-account-overview#identify-unused](https://cloud.google.com/iam/docs/service-account-overview#identify-unused)

## 技術情報

- Source Metadata：[sources/gcp/iam_service_account_unused/metadata.json](../../sources/gcp/iam_service_account_unused/metadata.json)
- Source Code：[sources/gcp/iam_service_account_unused/check.py](../../sources/gcp/iam_service_account_unused/check.py)
- Source Metadata Path：`sources/gcp/iam_service_account_unused/metadata.json`
- Source Code Path：`sources/gcp/iam_service_account_unused/check.py`

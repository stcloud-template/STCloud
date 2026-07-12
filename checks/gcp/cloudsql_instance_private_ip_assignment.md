# Ensure Instance IP assignment is set to private

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_private_ip_assignment` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure Instance IP assignment is set to private

## リスク

Instance addresses can be public IP or private IP. Public IP means that the instance is accessible through the public internet. In contrast, instances using only private IP are not accessible through the public internet, but are accessible through a Virtual Private Cloud (VPC). Limiting network access to your database will limit potential attacks.

## 推奨事項

Setting databases access only to private will reduce attack surface.

- 推奨リンク：[https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 修正手順

No remediation steps available.

## 参考資料

- [https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json](../../sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_private_ip_assignment/check.py](../../sources/gcp/cloudsql_instance_private_ip_assignment/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_private_ip_assignment/check.py`

# Ensure That the Local_infile Database Flag for a Cloud SQL MySQL Instance Is Set to Off

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_mysql_local_infile_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That the Local_infile Database Flag for a Cloud SQL MySQL Instance Is Set to Off

## リスク

The local_infile flag controls the server-side LOCAL capability for LOAD DATA statements. Depending on the local_infile setting, the server refuses or permits local data loading by clients that have LOCAL enabled on the client side.

## 推奨事項

It is recommended to set the local_infile database flag for a Cloud SQL MySQL instance to off.

- 推奨リンク：[https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags local_infile=off
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_1#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-local-infile-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-local-infile-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_mysql_local_infile_flag/metadata.json](../../sources/gcp/cloudsql_instance_mysql_local_infile_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_mysql_local_infile_flag/check.py](../../sources/gcp/cloudsql_instance_mysql_local_infile_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_mysql_local_infile_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_mysql_local_infile_flag/check.py`

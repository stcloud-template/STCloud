# Check for Cloud SQL Database Instances with Public IPs

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_public_ip` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Check for Cloud SQL Database Instances with Public IPs

## リスク

To lower the organization's attack surface, Cloud SQL databases should not have public IPs. Private IPs provide improved network security and lower latency for your application.

## 推奨事項

To lower the organization's attack surface, Cloud SQL databases should not have public IPs. Private IPs provide improved network security and lower latency for your application.

- 推奨リンク：[https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 修正手順


### CLI

```text
gcloud sql instances patch <MYSQL_INSTANCE> --project <PROJECT_ID> --network=<NETWORK_ID> --no-assign-ip
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/sql-database-instances-with-public-ips.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/sql-database-instances-with-public-ips.html)
- [https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_public_ip/metadata.json](../../sources/gcp/cloudsql_instance_public_ip/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_public_ip/check.py](../../sources/gcp/cloudsql_instance_public_ip/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_public_ip/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_public_ip/check.py`

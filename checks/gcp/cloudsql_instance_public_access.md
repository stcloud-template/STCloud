# Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_public_access` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | high |
| カテゴリ | internet-exposed |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses

## リスク

To minimize attack surface on a Database server instance, only trusted/known and required IP(s) should be white-listed to connect to it. An authorized network should not have IPs/networks configured to 0.0.0.0/0 which will allow access to the instance from anywhere in the world. Note that authorized networks apply only to instances with public IPs.

## 推奨事項

Database Server should accept connections only from trusted Network(s)/IP(s) and restrict access from public IP addresses.

- 推奨リンク：[https://cloud.google.com/sql/docs/mysql/connection-org-policy](https://cloud.google.com/sql/docs/mysql/connection-org-policy)

## 修正手順


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --authorized-networks=IP_ADDR1,IP_ADDR2...
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/publicly-accessible-cloud-sql-instances.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/publicly-accessible-cloud-sql-instances.html)

## 参考資料

- [https://cloud.google.com/sql/docs/mysql/connection-org-policy](https://cloud.google.com/sql/docs/mysql/connection-org-policy)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_public_access/metadata.json](../../sources/gcp/cloudsql_instance_public_access/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_public_access/check.py](../../sources/gcp/cloudsql_instance_public_access/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_public_access/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_public_access/check.py`

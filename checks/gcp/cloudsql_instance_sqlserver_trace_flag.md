# Ensure '3625 (trace flag)' database flag for all Cloud SQL Server instances is set to 'on'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_trace_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure '3625 (trace flag)' database flag for all Cloud SQL Server instances is set to 'on'

## リスク

Microsoft SQL Trace Flags are frequently used to diagnose performance issues or to debug stored procedures or complex computer systems, but they may also be recommended by Microsoft Support to address behavior that is negatively impacting a specific workload. All documented trace flags and those recommended by Microsoft Support are fully supported in a production environment when used as directed. 3625(trace log) Limits the amount of information returned to users who are not members of the sysadmin fixed server role, by masking the parameters of some error messages using '******'. Setting this in a Google Cloud flag for the instance allows for security through obscurity and prevents the disclosure of sensitive information, hence this is recommended to set this flag globally to on to prevent the flag having been left off, or changed by bad actors. This recommendation is applicable to SQL Server database instances.

## 推奨事項

It is recommended to set 3625 (trace flag) database flag for Cloud SQL SQL Server instance to on.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --database-flags 3625=on
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-3625-trace-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-3625-trace-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py`

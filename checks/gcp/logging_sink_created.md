# Ensure there is at least one sink used to export copies of all the log entries.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_sink_created` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Sink |
| リソースグループ | monitoring |

## 説明

Ensure there is at least one sink used to export copies of all the log entries.

## リスク

If sinks are not created, logs would be deleted after the configured retention period, and would not be backed up.

## 推奨事項

It is recommended to create a sink that will export copies of all the log entries. This can help aggregate logs from multiple projects and export them to a Security Information and Event Management (SIEM).

- 推奨リンク：[https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)

## 修正手順


### CLI

```text
gcloud logging sinks create <project_id> <destination_bucket>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/export-all-log-entries.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/export-all-log-entries.html)

## 参考資料

- [https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)

## 技術情報

- Source Metadata：[sources/gcp/logging_sink_created/metadata.json](../../sources/gcp/logging_sink_created/metadata.json)
- Source Code：[sources/gcp/logging_sink_created/check.py](../../sources/gcp/logging_sink_created/check.py)
- Source Metadata Path：`sources/gcp/logging_sink_created/metadata.json`
- Source Code Path：`sources/gcp/logging_sink_created/check.py`

# Ensure there is at least one sink used to export copies of all the log entries.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `logging_sink_created` |
| 云平台 | GCP |
| 服务 | logging |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Sink |
| 资源组 | monitoring |

## 描述

Ensure there is at least one sink used to export copies of all the log entries.

## 风险

If sinks are not created, logs would be deleted after the configured retention period, and would not be backed up.

## 推荐措施

It is recommended to create a sink that will export copies of all the log entries. This can help aggregate logs from multiple projects and export them to a Security Information and Event Management (SIEM).

- 推荐链接：[https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)

## 修复步骤


### CLI

```text
gcloud logging sinks create <project_id> <destination_bucket>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/export-all-log-entries.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/export-all-log-entries.html)

## 参考资料

- [https://cloud.google.com/logging/docs/export](https://cloud.google.com/logging/docs/export)

## 技术信息

- Source Metadata：[sources/gcp/logging_sink_created/metadata.json](../../sources/gcp/logging_sink_created/metadata.json)
- Source Code：[sources/gcp/logging_sink_created/check.py](../../sources/gcp/logging_sink_created/check.py)
- Source Metadata Path：`sources/gcp/logging_sink_created/metadata.json`
- Source Code Path：`sources/gcp/logging_sink_created/check.py`

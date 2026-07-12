# DataSync tasks should have logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `datasync_task_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | datasync |
| 重大度 | high |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsDataSyncTask |
| リソースグループ | storage |

## 説明

This control checks if AWS DataSync tasks have logging enabled. The control fails if the task doesn't have the CloudWatchLogGroupArn property defined.

## リスク

Without logging enabled, important operational data may be lost, making it difficult to troubleshoot issues, monitor performance, and ensure compliance with auditing requirements.

## 推奨事項

Configure logging for your DataSync tasks to ensure that operational data is captured and available for debugging, monitoring, and auditing purposes.

- 推奨リンク：[https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 修正手順


### CLI

```text
aws datasync update-task --task-arn <task-arn> --cloud-watch-log-group-arn <log-group-arn>
```

### Other

[https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 参考資料

- [https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 技術情報

- Source Metadata：[sources/aws/datasync_task_logging_enabled/metadata.json](../../sources/aws/datasync_task_logging_enabled/metadata.json)
- Source Code：[sources/aws/datasync_task_logging_enabled/check.py](../../sources/aws/datasync_task_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/datasync_task_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/datasync_task_logging_enabled/check.py`

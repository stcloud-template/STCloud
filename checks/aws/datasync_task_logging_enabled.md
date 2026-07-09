# DataSync tasks should have logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `datasync_task_logging_enabled` |
| 云平台 | AWS |
| 服务 | datasync |
| 严重等级 | high |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsDataSyncTask |
| 资源组 | storage |

## 描述

This control checks if AWS DataSync tasks have logging enabled. The control fails if the task doesn't have the CloudWatchLogGroupArn property defined.

## 风险

Without logging enabled, important operational data may be lost, making it difficult to troubleshoot issues, monitor performance, and ensure compliance with auditing requirements.

## 推荐措施

Configure logging for your DataSync tasks to ensure that operational data is captured and available for debugging, monitoring, and auditing purposes.

- 推荐链接：[https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 修复步骤


### CLI

```text
aws datasync update-task --task-arn <task-arn> --cloud-watch-log-group-arn <log-group-arn>
```

### Other

[https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 参考资料

- [https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html#enable-logging)

## 技术信息

- Source Metadata：[sources/aws/datasync_task_logging_enabled/metadata.json](../../sources/aws/datasync_task_logging_enabled/metadata.json)
- Source Code：[sources/aws/datasync_task_logging_enabled/check.py](../../sources/aws/datasync_task_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/datasync_task_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/datasync_task_logging_enabled/check.py`

# Check if S3 buckets have event notifications enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_event_notifications_enabled` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Ensure whether S3 buckets have event notifications enabled.

## 风险

Without event notifications, important actions on S3 buckets may go unnoticed, leading to missed opportunities for timely response to critical changes, such as object creation, deletion, or updates that could impact data security and availability.

## 推荐措施

Enable event notifications for all S3 general-purpose buckets to monitor important events such as object creation, deletion, tagging, and lifecycle events, ensuring visibility and quick action on relevant changes.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-11](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-11)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-event-types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-event-types)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_event_notifications_enabled/metadata.json](../../sources/aws/s3_bucket_event_notifications_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_event_notifications_enabled/check.py](../../sources/aws/s3_bucket_event_notifications_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_event_notifications_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_event_notifications_enabled/check.py`

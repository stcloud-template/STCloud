# Check if S3 buckets have event notifications enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_event_notifications_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Ensure whether S3 buckets have event notifications enabled.

## リスク

Without event notifications, important actions on S3 buckets may go unnoticed, leading to missed opportunities for timely response to critical changes, such as object creation, deletion, or updates that could impact data security and availability.

## 推奨事項

Enable event notifications for all S3 general-purpose buckets to monitor important events such as object creation, deletion, tagging, and lifecycle events, ensuring visibility and quick action on relevant changes.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-11](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-11)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-event-types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html#supported-notification-event-types)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_event_notifications_enabled/metadata.json](../../sources/aws/s3_bucket_event_notifications_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_event_notifications_enabled/check.py](../../sources/aws/s3_bucket_event_notifications_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_event_notifications_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_event_notifications_enabled/check.py`

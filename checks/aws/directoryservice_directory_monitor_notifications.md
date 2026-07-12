# Directory Service directory has SNS notifications enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `directoryservice_directory_monitor_notifications` |
| クラウドプラットフォーム | AWS |
| サービス | directoryservice |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

**AWS Directory Service** directories are associated with **Amazon SNS topics** to send status change notifications (e.g., `Active` `Impaired`). The evaluation looks for directories that have SNS event topics configured for monitoring alerts.

## リスク

Missing directory notifications reduces visibility into health changes, causing delayed response to `Impaired` states. This threatens availability of authentication, Kerberos/LDAP lookups, and domain joins; increases MTTR; and can enable silent replication or trust failures that impact integrity across dependent workloads.

## 推奨事項

Configure **AWS Directory Service** to publish directory status changes to an **SNS topic**, and subscribe your operations channels for timely alerts. Apply **least privilege** on topic permissions, integrate alerts with incident response, and use **defense in depth** by pairing notifications with logs and dashboards.

## 修正手順


### CLI

```text
aws ds register-event-topic --directory-id <DIRECTORY_ID> --topic-name <SNS_TOPIC_NAME>
```

### Other

1. Open AWS Console > Directory Service > Directories and select your directory
2. Go to the Maintenance or Monitoring/Notifications section
3. Click Actions > Create notification (or Set up notifications)
4. Select an existing SNS topic (or create one) and Save

## 参考資料

- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html)
- [https://support.icompaas.com/support/solutions/articles/62000233533-ensure-directory-service-has-sns-notifications-enabled](https://support.icompaas.com/support/solutions/articles/62000233533-ensure-directory-service-has-sns-notifications-enabled)

## 技術情報

- Source Metadata：[sources/aws/directoryservice_directory_monitor_notifications/metadata.json](../../sources/aws/directoryservice_directory_monitor_notifications/metadata.json)
- Source Code：[sources/aws/directoryservice_directory_monitor_notifications/check.py](../../sources/aws/directoryservice_directory_monitor_notifications/check.py)
- Source Metadata Path：`sources/aws/directoryservice_directory_monitor_notifications/metadata.json`
- Source Code Path：`sources/aws/directoryservice_directory_monitor_notifications/check.py`

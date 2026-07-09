# Directory Service directory has SNS notifications enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `directoryservice_directory_monitor_notifications` |
| 云平台 | AWS |
| 服务 | directoryservice |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | Other |
| 资源组 | IAM |

## 描述

**AWS Directory Service** directories are associated with **Amazon SNS topics** to send status change notifications (e.g., `Active` `Impaired`). The evaluation looks for directories that have SNS event topics configured for monitoring alerts.

## 风险

Missing directory notifications reduces visibility into health changes, causing delayed response to `Impaired` states. This threatens availability of authentication, Kerberos/LDAP lookups, and domain joins; increases MTTR; and can enable silent replication or trust failures that impact integrity across dependent workloads.

## 推荐措施

Configure **AWS Directory Service** to publish directory status changes to an **SNS topic**, and subscribe your operations channels for timely alerts. Apply **least privilege** on topic permissions, integrate alerts with incident response, and use **defense in depth** by pairing notifications with logs and dashboards.

## 修复步骤


### CLI

```text
aws ds register-event-topic --directory-id <DIRECTORY_ID> --topic-name <SNS_TOPIC_NAME>
```

### Other

1. Open AWS Console > Directory Service > Directories and select your directory
2. Go to the Maintenance or Monitoring/Notifications section
3. Click Actions > Create notification (or Set up notifications)
4. Select an existing SNS topic (or create one) and Save

## 参考资料

- [https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html)
- [https://support.icompaas.com/support/solutions/articles/62000233533-ensure-directory-service-has-sns-notifications-enabled](https://support.icompaas.com/support/solutions/articles/62000233533-ensure-directory-service-has-sns-notifications-enabled)

## 技术信息

- Source Metadata：[sources/aws/directoryservice_directory_monitor_notifications/metadata.json](../../sources/aws/directoryservice_directory_monitor_notifications/metadata.json)
- Source Code：[sources/aws/directoryservice_directory_monitor_notifications/check.py](../../sources/aws/directoryservice_directory_monitor_notifications/check.py)
- Source Metadata Path：`sources/aws/directoryservice_directory_monitor_notifications/metadata.json`
- Source Code Path：`sources/aws/directoryservice_directory_monitor_notifications/check.py`

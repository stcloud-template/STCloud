# AWS KMS customer managed key is not scheduled for deletion

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kms_cmk_not_deleted_unintentionally` |
| 云平台 | AWS |
| 服务 | kms |
| 严重等级 | critical |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | AwsKmsKey |
| 资源组 | security |

## 描述

**Customer-managed KMS keys** are evaluated for the `PendingDeletion` state, indicating a scheduled deletion during the mandatory waiting period.

## 风险

A key scheduled for deletion can lead to **permanent loss of decryption capability**, degrading **availability** and **integrity** of data and workloads. Accidental or malicious scheduling enables **cryptographic erasure**, causing outages, failed restores, and broken integrations during and after the wait window.

## 推荐措施

Prevent unintended deletion: - Enforce **least privilege** and **separation of duties** for key admins - Require change approvals and alerts on deletion events - Prefer **disabling** unused keys over deleting - Set sufficient waiting periods and review keys in `PendingDeletion` to verify authorization

## 修复步骤


### CLI

```text
aws kms cancel-key-deletion --key-id <KEY_ID>
```

### Other

1. Sign in to the AWS Management Console and open AWS KMS
2. Go to Customer managed keys and select the key with status "Pending deletion"
3. Click Key actions > Cancel key deletion
4. Confirm to cancel; the key status will change from Pending deletion

## 参考资料

- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html)
- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console)

## 技术信息

- Source Metadata：[sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json](../../sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json)
- Source Code：[sources/aws/kms_cmk_not_deleted_unintentionally/check.py](../../sources/aws/kms_cmk_not_deleted_unintentionally/check.py)
- Source Metadata Path：`sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json`
- Source Code Path：`sources/aws/kms_cmk_not_deleted_unintentionally/check.py`

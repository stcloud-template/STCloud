# AWS KMS customer managed key is not scheduled for deletion

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kms_cmk_not_deleted_unintentionally` |
| クラウドプラットフォーム | AWS |
| サービス | kms |
| 重大度 | critical |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| リソースタイプ | AwsKmsKey |
| リソースグループ | security |

## 説明

**Customer-managed KMS keys** are evaluated for the `PendingDeletion` state, indicating a scheduled deletion during the mandatory waiting period.

## リスク

A key scheduled for deletion can lead to **permanent loss of decryption capability**, degrading **availability** and **integrity** of data and workloads. Accidental or malicious scheduling enables **cryptographic erasure**, causing outages, failed restores, and broken integrations during and after the wait window.

## 推奨事項

Prevent unintended deletion: - Enforce **least privilege** and **separation of duties** for key admins - Require change approvals and alerts on deletion events - Prefer **disabling** unused keys over deleting - Set sufficient waiting periods and review keys in `PendingDeletion` to verify authorization

## 修正手順


### CLI

```text
aws kms cancel-key-deletion --key-id <KEY_ID>
```

### Other

1. Sign in to the AWS Management Console and open AWS KMS
2. Go to Customer managed keys and select the key with status "Pending deletion"
3. Click Key actions > Cancel key deletion
4. Confirm to cancel; the key status will change from Pending deletion

## 参考資料

- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html)
- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console)

## 技術情報

- Source Metadata：[sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json](../../sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json)
- Source Code：[sources/aws/kms_cmk_not_deleted_unintentionally/check.py](../../sources/aws/kms_cmk_not_deleted_unintentionally/check.py)
- Source Metadata Path：`sources/aws/kms_cmk_not_deleted_unintentionally/metadata.json`
- Source Code Path：`sources/aws/kms_cmk_not_deleted_unintentionally/check.py`

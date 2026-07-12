# Check if IAM identities (users,groups,roles) have the AWSCloudShellFullAccess policy attached.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_policy_cloudshell_admin_not_attached` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

This control checks whether an IAM identity (user, role, or group) has the AWS managed policy AWSCloudShellFullAccess attached. The control fails if an IAM identity has the AWSCloudShellFullAccess policy attached.

## リスク

Attaching the AWSCloudShellFullAccess policy to IAM identities grants broad permissions, including internet access and file transfer capabilities, which can lead to security risks such as data exfiltration. The principle of least privilege should be followed to avoid excessive permissions.

## 推奨事項

Detach the AWSCloudShellFullAccess policy from the IAM identity to restrict excessive permissions and adhere to the principle of least privilege.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)

## 修正手順


### CLI

```text
aws iam detach-user/role/group-policy --user/role/group-name <user/role/group-name> --policy-arn arn:aws:iam::aws:policy/AWSCloudShellFullAccess
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-27](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-27)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html](https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)

## 技術情報

- Source Metadata：[sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json](../../sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json)
- Source Code：[sources/aws/iam_policy_cloudshell_admin_not_attached/check.py](../../sources/aws/iam_policy_cloudshell_admin_not_attached/check.py)
- Source Metadata Path：`sources/aws/iam_policy_cloudshell_admin_not_attached/metadata.json`
- Source Code Path：`sources/aws/iam_policy_cloudshell_admin_not_attached/check.py`

# Ensure IAM Roles do not have ReadOnlyAccess access for external AWS accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_role_cross_account_readonlyaccess_policy` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

Ensure IAM Roles do not have ReadOnlyAccess access for external AWS accounts

## リスク

The AWS-managed ReadOnlyAccess policy is highly potent and exposes the customer to a significant data leakage threat. It should be granted very conservatively. For granting access to 3rd party vendors, consider using alternative managed policies, such as ViewOnlyAccess or SecurityAudit.

## 推奨事項

Remove the AWS-managed ReadOnlyAccess policy from all roles that have a trust policy, including third-party cloud accounts, or remove third-party cloud accounts from the trust policy of all roles that need the ReadOnlyAccess policy.

- 推奨リンク：[https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy](https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess)
- [https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy](https://docs.securestate.vmware.com/rule-docs/aws-iam-role-cross-account-readonlyaccess-policy)

## 技術情報

- Source Metadata：[sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json](../../sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json)
- Source Code：[sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py](../../sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py)
- Source Metadata Path：`sources/aws/iam_role_cross_account_readonlyaccess_policy/metadata.json`
- Source Code Path：`sources/aws/iam_role_cross_account_readonlyaccess_policy/check.py`

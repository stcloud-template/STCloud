# Ensure IAM Roles do not have AdministratorAccess policy attached

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_role_administratoraccess_policy` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| リソースタイプ | AwsIamRole |
| リソースグループ | IAM |

## 説明

Ensure IAM Roles do not have AdministratorAccess policy attached

## リスク

The AWS-managed AdministratorAccess policy grants all actions for all AWS services and for all resources in the account and as such exposes the customer to a significant data leakage threat. It should be granted very conservatively. For granting access to 3rd party vendors, consider using alternative managed policies, such as ViewOnlyAccess or SecurityAudit.

## 推奨事項

Apply the principle of least privilege. Instead of AdministratorAccess, assign only the permissions necessary for specific roles and tasks. Create custom IAM policies with minimal permissions based on the principle of least privilege.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 技術情報

- Source Metadata：[sources/aws/iam_role_administratoraccess_policy/metadata.json](../../sources/aws/iam_role_administratoraccess_policy/metadata.json)
- Source Code：[sources/aws/iam_role_administratoraccess_policy/check.py](../../sources/aws/iam_role_administratoraccess_policy/check.py)
- Source Metadata Path：`sources/aws/iam_role_administratoraccess_policy/metadata.json`
- Source Code Path：`sources/aws/iam_role_administratoraccess_policy/check.py`

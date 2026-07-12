# Ensure IAM policies are attached only to groups or roles

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_policy_attached_only_to_group_or_roles` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

Ensure IAM policies are attached only to groups or roles

## リスク

By default IAM users, groups, and roles have no access to AWS resources. IAM policies are the means by which privileges are granted to users, groups, or roles. It is recommended that IAM policies be applied directly to groups and roles but not users. Assigning privileges at the group or role level reduces the complexity of access management as the number of users grow. Reducing access management complexity may in-turn reduce opportunity for a principal to inadvertently receive or retain excessive privileges.

## 推奨事項

Remove any policy attached directly to the user. Use groups or roles instead.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json](../../sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json)
- Source Code：[sources/aws/iam_policy_attached_only_to_group_or_roles/check.py](../../sources/aws/iam_policy_attached_only_to_group_or_roles/check.py)
- Source Metadata Path：`sources/aws/iam_policy_attached_only_to_group_or_roles/metadata.json`
- Source Code Path：`sources/aws/iam_policy_attached_only_to_group_or_roles/check.py`

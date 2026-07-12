# Ensure that no custom IAM policies exist which allow permissive role assumption (e.g. sts:AssumeRole on *)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_no_custom_policy_permissive_role_assumption` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks |
| リソースタイプ | AwsIamPolicy |
| リソースグループ | IAM |

## 説明

Ensure that no custom IAM policies exist which allow permissive role assumption (e.g. sts:AssumeRole on *)

## リスク

If not restricted unintended access could happen.

## 推奨事項

Use the least privilege principle when granting permissions.

- 推奨リンク：[https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html#roles-usingrole-createpolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html#roles-usingrole-createpolicy)
- [https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

## 技術情報

- Source Metadata：[sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json](../../sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json)
- Source Code：[sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py](../../sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py)
- Source Metadata Path：`sources/aws/iam_no_custom_policy_permissive_role_assumption/metadata.json`
- Source Code Path：`sources/aws/iam_no_custom_policy_permissive_role_assumption/check.py`

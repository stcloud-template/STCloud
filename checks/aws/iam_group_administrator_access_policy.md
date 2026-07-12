# Ensure No IAM Groups Have Administrator Access Policy

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_group_administrator_access_policy` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsIamGroup |
| リソースグループ | IAM |

## 説明

This check ensures that no IAM groups in your AWS account have the 'AdministratorAccess' policy attached. IAM users with this policy have unrestricted access to all AWS services and resources, which poses a significant security risk if misused.

## リスク

IAM groups with administrator-level permissions can perform any action on any resource in your AWS environment. If these permissions are granted to users unnecessarily or to individuals without sufficient knowledge, it can lead to security vulnerabilities, data leaks, data loss, or unexpected charges.

## 推奨事項

Replace the 'AdministratorAccess' policy with more specific permissions that follow the Principle of Least Privilege. Consider implementing IAM roles such as 'IAM Master' and 'IAM Manager' to manage permissions more securely.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修正手順


### CLI

```text
aws iam detach-group-policy --group-name <groupname> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/group-with-privileged-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/group-with-privileged-access.html)

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/iam_group_administrator_access_policy/metadata.json](../../sources/aws/iam_group_administrator_access_policy/metadata.json)
- Source Code：[sources/aws/iam_group_administrator_access_policy/check.py](../../sources/aws/iam_group_administrator_access_policy/check.py)
- Source Metadata Path：`sources/aws/iam_group_administrator_access_policy/metadata.json`
- Source Code Path：`sources/aws/iam_group_administrator_access_policy/check.py`

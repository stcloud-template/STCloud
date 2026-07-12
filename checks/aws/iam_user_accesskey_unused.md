# Ensure unused User Access Keys are disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_accesskey_unused` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Ensure unused User Access Keys are disabled

## リスク

To increase the security of your AWS account, remove IAM user credentials (that is, passwords and access keys) that are not needed. For example, when users leave your organization or no longer need AWS access.

## 推奨事項

Find the credentials that they were using and ensure that they are no longer operational. Ideally, you delete credentials if they are no longer needed. You can always recreate them at a later date if the need arises. At the very least, you should change the password or deactivate the access keys so that the former users no longer have access.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_accesskey_unused/metadata.json](../../sources/aws/iam_user_accesskey_unused/metadata.json)
- Source Code：[sources/aws/iam_user_accesskey_unused/check.py](../../sources/aws/iam_user_accesskey_unused/check.py)
- Source Metadata Path：`sources/aws/iam_user_accesskey_unused/metadata.json`
- Source Code Path：`sources/aws/iam_user_accesskey_unused/check.py`

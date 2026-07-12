# Ensure users make use of temporary credentials assuming IAM roles

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_with_temporary_credentials` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Ensure users make use of temporary credentials assuming IAM roles

## リスク

As a best practice, use temporary security credentials (IAM roles) instead of creating long-term credentials like access keys, and don't create AWS account root user access keys.

## 推奨事項

As a best practice, use temporary security credentials (IAM roles) instead of creating long-term credentials like access keys, and don't create AWS account root user access keys.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_with_temporary_credentials/metadata.json](../../sources/aws/iam_user_with_temporary_credentials/metadata.json)
- Source Code：[sources/aws/iam_user_with_temporary_credentials/check.py](../../sources/aws/iam_user_with_temporary_credentials/check.py)
- Source Metadata Path：`sources/aws/iam_user_with_temporary_credentials/metadata.json`
- Source Code Path：`sources/aws/iam_user_with_temporary_credentials/check.py`

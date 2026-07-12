# Check if IAM users have two active access keys

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_two_active_access_key` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Check if IAM users have two active access keys

## リスク

Access Keys could be lost or stolen. It creates a critical risk.

## 推奨事項

Avoid using long lived access keys.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_two_active_access_key/metadata.json](../../sources/aws/iam_user_two_active_access_key/metadata.json)
- Source Code：[sources/aws/iam_user_two_active_access_key/check.py](../../sources/aws/iam_user_two_active_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_user_two_active_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_user_two_active_access_key/check.py`

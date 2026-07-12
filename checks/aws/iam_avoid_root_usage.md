# Avoid the use of the root accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_avoid_root_usage` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Avoid the use of the root account

## リスク

The root account has unrestricted access to all resources in the AWS account. It is highly recommended that the use of this account be avoided.

## 推奨事項

Follow the remediation instructions of the Ensure IAM policies are attached only to groups or roles recommendation.

- 推奨リンク：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修正手順

No remediation steps available.

## 参考資料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/iam_avoid_root_usage/metadata.json](../../sources/aws/iam_avoid_root_usage/metadata.json)
- Source Code：[sources/aws/iam_avoid_root_usage/check.py](../../sources/aws/iam_avoid_root_usage/check.py)
- Source Metadata Path：`sources/aws/iam_avoid_root_usage/metadata.json`
- Source Code Path：`sources/aws/iam_avoid_root_usage/check.py`

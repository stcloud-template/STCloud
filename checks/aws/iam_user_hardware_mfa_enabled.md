# Check if IAM users have Hardware MFA enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_hardware_mfa_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Check if IAM users have Hardware MFA enabled.

## リスク

Hardware MFA is preferred over virtual MFA.

## 推奨事項

Enable hardware MFA device for an IAM user from the AWS Management Console, the command line, or the IAM API.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_hardware_mfa_enabled/metadata.json](../../sources/aws/iam_user_hardware_mfa_enabled/metadata.json)
- Source Code：[sources/aws/iam_user_hardware_mfa_enabled/check.py](../../sources/aws/iam_user_hardware_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_user_hardware_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_user_hardware_mfa_enabled/check.py`

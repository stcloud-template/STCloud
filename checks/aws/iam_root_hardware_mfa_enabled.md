# Ensure only hardware MFA is enabled for the root account

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_root_hardware_mfa_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | critical |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Ensure only hardware MFA is enabled for the root account

## リスク

The root account is the most privileged user in an AWS account. MFA adds an extra layer of protection on top of a user name and password. With MFA enabled when a user signs in to an AWS website they will be prompted for their user name and password as well as for an authentication code from their AWS MFA device. For Level 2 it is recommended that the root account be protected with only a hardware MFA.

## 推奨事項

Using IAM console navigate to Dashboard and expand Activate MFA on your root account. If using AWS Organizations, consider enabling Centralized Root Management and removing individual root credentials.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa)

## 技術情報

- Source Metadata：[sources/aws/iam_root_hardware_mfa_enabled/metadata.json](../../sources/aws/iam_root_hardware_mfa_enabled/metadata.json)
- Source Code：[sources/aws/iam_root_hardware_mfa_enabled/check.py](../../sources/aws/iam_root_hardware_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_root_hardware_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_root_hardware_mfa_enabled/check.py`

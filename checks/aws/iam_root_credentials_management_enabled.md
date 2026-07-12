# Ensure centralized root credentials management is enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_root_credentials_management_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Checks if centralized management of root credentials for member accounts in AWS Organizations is enabled. This ensures that root credentials are managed centrally, reducing the risk of unauthorized access or mismanagement.

## リスク

Without centralized root credentials management, member accounts retain full control over their root user credentials, increasing the risk of credential misuse, mismanagement, or compromise.

## 推奨事項

Enable centralized management of root access for member accounts using the CLI or IAM console.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)

## 修正手順


### CLI

```text
aws iam enable-organizations-root-credentials-management
```

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)

## 技術情報

- Source Metadata：[sources/aws/iam_root_credentials_management_enabled/metadata.json](../../sources/aws/iam_root_credentials_management_enabled/metadata.json)
- Source Code：[sources/aws/iam_root_credentials_management_enabled/check.py](../../sources/aws/iam_root_credentials_management_enabled/check.py)
- Source Metadata Path：`sources/aws/iam_root_credentials_management_enabled/metadata.json`
- Source Code Path：`sources/aws/iam_root_credentials_management_enabled/check.py`

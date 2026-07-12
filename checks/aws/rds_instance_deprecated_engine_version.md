# Check if RDS instance is using a supported engine version

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_deprecated_engine_version` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS is using a supported engine version for MariaDB, MySQL and PostgreSQL

## リスク

If not enabled RDS instances may be vulnerable to security issues

## 推奨事項

Ensure all the RDS instances are using a supported engine version

- 推奨リンク：[https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html)

## 修正手順


### CLI

```text
aws rds describe-db-engine-versions --engine <my_engine>'
```

## 参考資料

- [https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_deprecated_engine_version/metadata.json](../../sources/aws/rds_instance_deprecated_engine_version/metadata.json)
- Source Code：[sources/aws/rds_instance_deprecated_engine_version/check.py](../../sources/aws/rds_instance_deprecated_engine_version/check.py)
- Source Metadata Path：`sources/aws/rds_instance_deprecated_engine_version/metadata.json`
- Source Code Path：`sources/aws/rds_instance_deprecated_engine_version/check.py`

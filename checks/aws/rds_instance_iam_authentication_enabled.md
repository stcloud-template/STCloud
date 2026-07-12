# Check if RDS instances have IAM authentication enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_iam_authentication_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances have IAM authentication enabled.

## リスク

Ensure that the IAM Database Authentication feature is enabled for your RDS database instances in order to use the Identity and Access Management (IAM) service to manage database access to your MySQL and PostgreSQL database instances. With this feature enabled, you don't have to use a password when you connect to your MySQL/PostgreSQL database, instead you can use an authentication token. An authentication token is a unique string of characters with a lifetime of 15 minutes that Amazon RDS generates on your request. IAM Database Authentication removes the need of storing user credentials within the database configuration, because authentication is managed externally using Amazon IAM.

## 推奨事項

Enable IAM authentication for supported RDS instances.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --region <REGION> --db-instance-identifier <DB_INSTANCE_ID> --enable-iam-database-authentication --apply-immediately
```

### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/iam-database-authentication.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/iam-database-authentication.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/iam-database-authentication.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/iam-database-authentication.html#)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-10](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-10)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_iam_authentication_enabled/metadata.json](../../sources/aws/rds_instance_iam_authentication_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_iam_authentication_enabled/check.py](../../sources/aws/rds_instance_iam_authentication_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_iam_authentication_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_iam_authentication_enabled/check.py`

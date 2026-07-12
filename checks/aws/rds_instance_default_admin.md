# Ensure that your Amazon RDS instances are not using the default master username.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_default_admin` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Ensure that your Amazon RDS instances are not using the default master username.

## リスク

Since admin is the Amazon's example for the RDS database master username and postgres is the default PostgreSQL master username. Many AWS customers will use this username for their RDS database instances in production. Malicious users can use this information to their advantage and frequently try to use default master username during brute-force attacks.

## 推奨事項

To change the master username configured for your Amazon RDS database instances you must re-create them and migrate the existing data.

- 推奨リンク：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-25](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-25)

## 修正手順


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-25](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-25)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_default_admin/metadata.json](../../sources/aws/rds_instance_default_admin/metadata.json)
- Source Code：[sources/aws/rds_instance_default_admin/check.py](../../sources/aws/rds_instance_default_admin/check.py)
- Source Metadata Path：`sources/aws/rds_instance_default_admin/metadata.json`
- Source Code Path：`sources/aws/rds_instance_default_admin/check.py`

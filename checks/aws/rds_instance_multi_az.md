# Check if RDS instances have multi-AZ enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | redundancy |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances have multi-AZ enabled.

## リスク

In case of failure, with a single-AZ deployment configuration, should an availability zone specific database failure occur, Amazon RDS can not automatically fail over to the standby availability zone.

## 推奨事項

Enable multi-AZ deployment for production databases.

- 推奨リンク：[https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 修正手順


### CLI

```text
aws rds create-db-instance --db-instance-identifier <db_instance_id> --multi-az true
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-multi-az.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-multi-az.html)

## 参考資料

- [https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_multi_az/metadata.json](../../sources/aws/rds_instance_multi_az/metadata.json)
- Source Code：[sources/aws/rds_instance_multi_az/check.py](../../sources/aws/rds_instance_multi_az/check.py)
- Source Metadata Path：`sources/aws/rds_instance_multi_az/metadata.json`
- Source Code Path：`sources/aws/rds_instance_multi_az/check.py`

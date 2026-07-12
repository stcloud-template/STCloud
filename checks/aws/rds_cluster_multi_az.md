# Check if RDS clusters have multi-AZ enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_cluster_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | redundancy |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Check if RDS clusters have multi-AZ enabled.

## リスク

In case of failure, with a single-AZ deployment configuration, should an availability zone specific database failure occur, Amazon RDS can not automatically fail over to the standby availability zone.

## 推奨事項

Enable multi-AZ deployment for production databases.

- 推奨リンク：[https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 修正手順


### CLI

```text
aws rds create-db-cluster --db-cluster-identifier <db_cluster_id> --multi-az true
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-15](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-15)

## 参考資料

- [https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 技術情報

- Source Metadata：[sources/aws/rds_cluster_multi_az/metadata.json](../../sources/aws/rds_cluster_multi_az/metadata.json)
- Source Code：[sources/aws/rds_cluster_multi_az/check.py](../../sources/aws/rds_cluster_multi_az/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_multi_az/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_multi_az/check.py`

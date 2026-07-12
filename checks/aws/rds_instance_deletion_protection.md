# Check if RDS instances have deletion protection enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_deletion_protection` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances have deletion protection enabled.

## リスク

You can only delete instances that do not have deletion protection enabled.

## 推奨事項

Enable deletion protection using the AWS Management Console for production DB instances.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --deletion-protection --apply-immediately
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-clusters-and-instances-have-deletion-protection-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-clusters-and-instances-have-deletion-protection-enabled#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/instance-deletion-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/instance-deletion-protection.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_deletion_protection/metadata.json](../../sources/aws/rds_instance_deletion_protection/metadata.json)
- Source Code：[sources/aws/rds_instance_deletion_protection/check.py](../../sources/aws/rds_instance_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/rds_instance_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/rds_instance_deletion_protection/check.py`

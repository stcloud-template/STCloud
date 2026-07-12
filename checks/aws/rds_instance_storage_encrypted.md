# Check if RDS instances storage is encrypted.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_storage_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances storage is encrypted.

## リスク

If not enabled sensitive information at rest is not protected.

## 推奨事項

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)

## 修正手順


### CLI

```text
aws rds create-db-instance --db-instance-identifier <db_instance_id> --db-instance-class <instance_class> --engine <engine> --storage-encrypted true
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_4#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_4#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_4#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-encryption-enabled.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_storage_encrypted/metadata.json](../../sources/aws/rds_instance_storage_encrypted/metadata.json)
- Source Code：[sources/aws/rds_instance_storage_encrypted/check.py](../../sources/aws/rds_instance_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_instance_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_instance_storage_encrypted/check.py`

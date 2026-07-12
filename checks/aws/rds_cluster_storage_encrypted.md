# Check if RDS clusters storage is encrypted.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_cluster_storage_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Check if RDS clusters storage is encrypted.

## リスク

If not enabled sensitive information at rest is not protected.

## 推奨事項

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling)

## 修正手順


### CLI

```text
aws rds create-db-cluster --db-cluster-identifier <db_cluster_id> --db-cluster-class <cluster_class> --engine <engine> --storage-encrypted true
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-27](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-27)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling)

## 技術情報

- Source Metadata：[sources/aws/rds_cluster_storage_encrypted/metadata.json](../../sources/aws/rds_cluster_storage_encrypted/metadata.json)
- Source Code：[sources/aws/rds_cluster_storage_encrypted/check.py](../../sources/aws/rds_cluster_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_storage_encrypted/check.py`

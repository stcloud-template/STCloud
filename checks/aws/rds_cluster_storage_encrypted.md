# Check if RDS clusters storage is encrypted.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_storage_encrypted` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Check if RDS clusters storage is encrypted.

## 风险

If not enabled sensitive information at rest is not protected.

## 推荐措施

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling)

## 修复步骤


### CLI

```text
aws rds create-db-cluster --db-cluster-identifier <db_cluster_id> --db-cluster-class <cluster_class> --engine <engine> --storage-encrypted true
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-27](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-27)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_storage_encrypted/metadata.json](../../sources/aws/rds_cluster_storage_encrypted/metadata.json)
- Source Code：[sources/aws/rds_cluster_storage_encrypted/check.py](../../sources/aws/rds_cluster_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_storage_encrypted/check.py`

# Check if RDS instances storage is encrypted.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_storage_encrypted` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS instances storage is encrypted.

## 风险

If not enabled sensitive information at rest is not protected.

## 推荐措施

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_storage_encrypted/metadata.json](../../sources/aws/rds_instance_storage_encrypted/metadata.json)
- Source Code：[sources/aws/rds_instance_storage_encrypted/check.py](../../sources/aws/rds_instance_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_instance_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_instance_storage_encrypted/check.py`

# Check if RDS instances have deletion protection enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_deletion_protection` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS instances have deletion protection enabled.

## 风险

You can only delete instances that do not have deletion protection enabled.

## 推荐措施

Enable deletion protection using the AWS Management Console for production DB instances.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html)

## 修复步骤


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --deletion-protection --apply-immediately
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-clusters-and-instances-have-deletion-protection-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-clusters-and-instances-have-deletion-protection-enabled#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/instance-deletion-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/instance-deletion-protection.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_deletion_protection/metadata.json](../../sources/aws/rds_instance_deletion_protection/metadata.json)
- Source Code：[sources/aws/rds_instance_deletion_protection/check.py](../../sources/aws/rds_instance_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/rds_instance_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/rds_instance_deletion_protection/check.py`

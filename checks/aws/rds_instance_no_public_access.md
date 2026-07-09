# Ensure there are no Public Accessible RDS instances.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_no_public_access` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Ensure there are no Public Accessible RDS instances.

## 风险

Publicly accessible databases could expose sensitive data to bad actors.

## 推荐措施

Using an AWS Config rule check for RDS public instances periodically and check there is a business reason for it.

- 推荐链接：[https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html)

## 修复步骤


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --no-publicly-accessible --apply-immediately
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/public-policies/public_2#cloudformation](https://docs.ST Cloud.com/checks/aws/public-policies/public_2#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/public-policies/public_2#terraform](https://docs.ST Cloud.com/checks/aws/public-policies/public_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-publicly-accessible.html)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_no_public_access/metadata.json](../../sources/aws/rds_instance_no_public_access/metadata.json)
- Source Code：[sources/aws/rds_instance_no_public_access/check.py](../../sources/aws/rds_instance_no_public_access/check.py)
- Source Metadata Path：`sources/aws/rds_instance_no_public_access/metadata.json`
- Source Code Path：`sources/aws/rds_instance_no_public_access/check.py`

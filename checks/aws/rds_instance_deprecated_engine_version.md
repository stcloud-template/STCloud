# Check if RDS instance is using a supported engine version

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_deprecated_engine_version` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS is using a supported engine version for MariaDB, MySQL and PostgreSQL

## 风险

If not enabled RDS instances may be vulnerable to security issues

## 推荐措施

Ensure all the RDS instances are using a supported engine version

- 推荐链接：[https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html)

## 修复步骤


### CLI

```text
aws rds describe-db-engine-versions --engine <my_engine>'
```

## 参考资料

- [https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_deprecated_engine_version/metadata.json](../../sources/aws/rds_instance_deprecated_engine_version/metadata.json)
- Source Code：[sources/aws/rds_instance_deprecated_engine_version/check.py](../../sources/aws/rds_instance_deprecated_engine_version/check.py)
- Source Metadata Path：`sources/aws/rds_instance_deprecated_engine_version/metadata.json`
- Source Code Path：`sources/aws/rds_instance_deprecated_engine_version/check.py`

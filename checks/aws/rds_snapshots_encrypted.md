# Check if RDS Snapshots and Cluster Snapshots are encrypted.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_snapshots_encrypted` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AwsRdsDbSnapshot |
| 资源组 | database |

## 描述

Check if RDS Snapshots and Cluster Snapshots are encrypted.

## 风险

Ensure that your manual Amazon RDS database snapshots are encrypted in order to achieve compliance for data-at-rest encryption within your organization.

## 推荐措施

When working with production databases that hold sensitive and critical data, it is strongly recommended to implement encryption at rest and protect your data from attackers or unauthorized personnel.

- 推荐链接：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4)

## 修复步骤


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/snapshot-encrypted.html#)

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4)

## 技术信息

- Source Metadata：[sources/aws/rds_snapshots_encrypted/metadata.json](../../sources/aws/rds_snapshots_encrypted/metadata.json)
- Source Code：[sources/aws/rds_snapshots_encrypted/check.py](../../sources/aws/rds_snapshots_encrypted/check.py)
- Source Metadata Path：`sources/aws/rds_snapshots_encrypted/metadata.json`
- Source Code Path：`sources/aws/rds_snapshots_encrypted/check.py`

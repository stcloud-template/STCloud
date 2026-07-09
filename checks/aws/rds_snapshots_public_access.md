# Check if RDS Snapshots and Cluster Snapshots are public.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_snapshots_public_access` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 资源类型 | AwsRdsDbSnapshot |
| 资源组 | database |

## 描述

Check if RDS Snapshots and Cluster Snapshots are public.

## 风险

Publicly accessible services could expose sensitive data to bad actors. t is recommended that your RDS snapshots should not be public in order to prevent potential leak or misuse of sensitive data or any other kind of security threat. If your RDS snapshot is public, then the data which is backed up in that snapshot is accessible to all other AWS accounts.

## 推荐措施

Use AWS Config to identify any snapshot that is public.

- 推荐链接：[https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html)

## 修复步骤


### CLI

```text
aws rds modify-db-snapshot-attribute --db-snapshot-identifier <snapshot_id> --attribute-name restore --values-to-remove all
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/public-snapshots.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/public-snapshots.html)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html)

## 技术信息

- Source Metadata：[sources/aws/rds_snapshots_public_access/metadata.json](../../sources/aws/rds_snapshots_public_access/metadata.json)
- Source Code：[sources/aws/rds_snapshots_public_access/check.py](../../sources/aws/rds_snapshots_public_access/check.py)
- Source Metadata Path：`sources/aws/rds_snapshots_public_access/metadata.json`
- Source Code Path：`sources/aws/rds_snapshots_public_access/check.py`

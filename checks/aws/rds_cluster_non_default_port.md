# Check if RDS clusters are using non-default ports.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_non_default_port` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Checks if an cluster uses a port other than the default port of the database engine. The control fails if the RDS cluster uses the default port.

## 风险

Using a default database port exposes the cluster to potential security vulnerabilities, as attackers are more likely to target known, commonly-used ports. This may result in unauthorized access to the database or increased susceptibility to automated attacks.

## 推荐措施

Modify the RDS cluster to use a non-default port, and ensure that the security group permits access to the new port.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 修复步骤


### CLI

```text
aws rds modify-db-cluster --db-cluster-identifier <db-cluster-id> --port <non-default-port>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-23](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-23)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_non_default_port/metadata.json](../../sources/aws/rds_cluster_non_default_port/metadata.json)
- Source Code：[sources/aws/rds_cluster_non_default_port/check.py](../../sources/aws/rds_cluster_non_default_port/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_non_default_port/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_non_default_port/check.py`

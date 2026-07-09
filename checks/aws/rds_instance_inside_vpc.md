# Check if RDS instances are deployed within a VPC.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_inside_vpc` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, AWS Security Best Practices |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS instances are deployed within a VPC.

## 风险

If your RDS instances are not deployed within a VPC, they are not isolated from the public internet and are exposed to potential security threats. Deploying RDS instances within a VPC allows you to control inbound and outbound traffic to and from the instances, and provides an additional layer of security to your database instances.

## 推荐措施

Ensure that your RDS instances are deployed within a VPC to provide an additional layer of security to your database instances.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 修复步骤


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <instance-identifier> --vpc-security-group-ids <vpc-security-group-ids>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-18](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-18)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_inside_vpc/metadata.json](../../sources/aws/rds_instance_inside_vpc/metadata.json)
- Source Code：[sources/aws/rds_instance_inside_vpc/check.py](../../sources/aws/rds_instance_inside_vpc/check.py)
- Source Metadata Path：`sources/aws/rds_instance_inside_vpc/metadata.json`
- Source Code Path：`sources/aws/rds_instance_inside_vpc/check.py`

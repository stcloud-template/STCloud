# EFS file system is Multi-AZ with more than one mount target

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `efs_multi_az_enabled` |
| 云平台 | AWS |
| 服务 | efs |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsEfsFileSystem |
| 资源组 | storage |

## 描述

**Amazon EFS** file systems are assessed for **multi-AZ resilience**: Regional type (no `availability_zone_id`) with mount targets in more than one Availability Zone. Single-AZ (One Zone) or Regional with only one mount target is identified for attention.

## 风险

Concentrating access through a single AZ or a lone mount target reduces **availability**. An AZ outage can sever client connectivity, causing downtime and I/O errors. A single mount target also forces cross-AZ traffic, increasing latency and costs and undermining **resilience** and seamless failover.

## 推荐措施

Use **Regional EFS** and create mount targets in each required **Availability Zone** to remove single points of failure and keep clients local to their AZ. Avoid One Zone for critical data. Periodically review mount target distribution to uphold **high availability** and **fault tolerance**.

## 修复步骤


### CLI

```text
aws efs create-mount-target --file-system-id <FILE_SYSTEM_ID> --subnet-id <SUBNET_ID>
```

### Native IaC

```yaml
# CloudFormation: add an extra EFS mount target to another AZ
Resources:
  <example_resource_name>:
    Type: AWS::EFS::MountTarget
    Properties:
      FileSystemId: fs-<example_resource_id>  # FIX: adds another mount target for this EFS
      SubnetId: subnet-<example_resource_id>  # FIX: choose a subnet in a different AZ
      SecurityGroups:
        - <example_security_group_id>         # Required by CFN
```

### Terraform

```hcl
# Add an extra EFS mount target in a different AZ/subnet
resource "aws_efs_mount_target" "<example_resource_name>" {
  file_system_id = "<example_resource_id>"  # FIX: target EFS
  subnet_id      = "<example_resource_id>"  # FIX: subnet in another AZ to make targets > 1
}
```

### Other

1. In AWS Console, go to EFS > File systems > select your file system
2. If File system type shows Regional: open the Network tab > Mount targets > Manage mount targets > Add mount target
3. Select a subnet in a different Availability Zone and save
4. If File system type shows One Zone: create a new EFS with File system type = Regional and create mount targets in at least two AZs; remount clients to the new file system and decommission the old one

## 参考资料

- [https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#availabiltydurability](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#availabiltydurability)
- [https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)
- [https://ops.tips/gists/how-aws-efs-multiple-availability-zones-terraform/](https://ops.tips/gists/how-aws-efs-multiple-availability-zones-terraform/)

## 技术信息

- Source Metadata：[sources/aws/efs_multi_az_enabled/metadata.json](../../sources/aws/efs_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/efs_multi_az_enabled/check.py](../../sources/aws/efs_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/efs_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/efs_multi_az_enabled/check.py`

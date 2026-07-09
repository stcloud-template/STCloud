# Unused Network Access Control Lists should be removed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_networkacl_unused` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | internet-exposed |
| 资源类型 | AwsEc2NetworkAcl |
| 资源组 | network |

## 描述

Ensure that there are no unused network access control lists (network ACLs) in your virtual private cloud (VPC). The control fails if the network ACL isn't associated with a subnet. The control doesn't generate findings for an unused default network ACL.

## 风险

Unused network ACLs may represent a potential security risk if left in place without purpose, as they could be mistakenly associated with subnets later.

## 推荐措施

For instructions on deleting an unused network ACL, see Deleting a network ACL in the Amazon VPC User Guide.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete)

## 修复步骤


### CLI

```text
aws ec2 delete-network-acl --network-acl-id <nacl_id>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html](https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html)
- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#vpc-network-acl-delete)

## 技术信息

- Source Metadata：[sources/aws/ec2_networkacl_unused/metadata.json](../../sources/aws/ec2_networkacl_unused/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_unused/check.py](../../sources/aws/ec2_networkacl_unused/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_unused/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_unused/check.py`

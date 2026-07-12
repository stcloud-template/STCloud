# EFS file system has no publicly accessible mount targets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `efs_mount_target_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | efs |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access, Effects/Data Exposure |
| リソースタイプ | AwsEfsFileSystem |
| リソースグループ | storage |

## 説明

**EFS mount targets** associated with VPC subnets that auto-assign public IPv4 addresses (`mapPublicIpOnLaunch=true`) are identified per file system. The evaluation focuses on the subnet attribute linked to each mount target.

## リスク

Publicly addressable mount targets expose NFS to Internet scanning and exploit attempts. - **Confidentiality**: unauthorized reads - **Integrity**: illicit writes or deletion - **Availability**: DDoS/resource exhaustion *Even with tight rules*, a public IP weakens isolation and eases recon.

## 推奨事項

Place mount targets in **private subnets** that do not auto-assign public IPs (`mapPublicIpOnLaunch=false`). Apply **least privilege**: restrict NFS via security groups to known sources, avoid Internet routes, and use **defense in depth** with NACLs. Prefer private connectivity (VPN/Direct Connect or peering) for access.

## 修正手順


### Native IaC

```yaml
# Create an EFS mount target in a private subnet
Resources:
  <example_resource_name>:
    Type: AWS::EFS::MountTarget
    Properties:
      FileSystemId: <example_resource_id>
      SubnetId: <example_resource_id>  # FIX: Use a private subnet (no route to an Internet Gateway)
      SecurityGroups:
        - <example_resource_id>  # Required SG for the mount target
```

### Terraform

```hcl
# Create an EFS mount target in a private subnet
resource "aws_efs_mount_target" "<example_resource_name>" {
  file_system_id  = "<example_resource_id>"
  subnet_id       = "<example_resource_id>"  # FIX: Use a private subnet (no route to an Internet Gateway)
  security_groups = ["<example_resource_id>"]
}
```

### Other

1. Open the AWS Console > EFS > File systems > select your file system
2. Go to Networking and click Create mount target
3. Choose a subnet that is private (no route to an Internet Gateway) and select a security group
4. Click Create
5. In Networking, select any mount targets in public subnets and click Delete to remove them

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-6](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-6)
- [https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)

## 技術情報

- Source Metadata：[sources/aws/efs_mount_target_not_publicly_accessible/metadata.json](../../sources/aws/efs_mount_target_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/efs_mount_target_not_publicly_accessible/check.py](../../sources/aws/efs_mount_target_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/efs_mount_target_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/efs_mount_target_not_publicly_accessible/check.py`

# EFS file system has all access points with a defined POSIX user

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `efs_access_point_enforce_user_identity` |
| 云平台 | AWS |
| 服务 | efs |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Privilege Escalation |
| 资源类型 | AwsEfsAccessPoint |
| 资源组 | storage |

## 描述

**Amazon EFS access points** are evaluated for a defined **POSIX user** (`uid`, `gid`, optional secondary groups). The check inspects each access point on a file system and flags those without a configured POSIX user identity.

## 风险

Without enforced **POSIX identity**, NFS clients can supply arbitrary UIDs/GIDs, enabling impersonation, unauthorized reads/writes, and ownership spoofing. This undermines **confidentiality** and **integrity** of shared data and can enable **lateral movement** across applications sharing the file system.

## 推荐措施

Enforce a **POSIX user identity** on every access point using least-privilege `uid`/`gid` (avoid `0`). Apply **separation of duties** with dedicated access points per application and minimal groups. Use **IAM** to require access point usage and add **defense in depth** by enforcing a restricted root directory.

## 修复步骤


### Native IaC

```yaml
Resources:
  ExampleAccessPoint:
    Type: AWS::EFS::AccessPoint
    Properties:
      FileSystemId: "<example_resource_id>"
      PosixUser:               # Critical: enforces a POSIX user for all requests via this access point
        Uid: "<uid>"          # Critical: POSIX user ID enforced
        Gid: "<gid>"          # Critical: POSIX group ID enforced
```

### Terraform

```hcl
resource "aws_efs_access_point" "example" {
  file_system_id = "<example_resource_id>"

  # Critical: enforces a POSIX user for all requests via this access point
  posix_user {
    uid = 1000  # Critical: user ID enforced
    gid = 1000  # Critical: group ID enforced
  }
}
```

### Other

1. In the AWS Console, go to Amazon EFS > Access points
2. Click Create access point, select the file system, and set POSIX user: enter User ID and Group ID
3. Click Create access point
4. Update clients to mount using the new access point ID
5. Delete the old access point(s) that lack a POSIX user

## 参考资料

- [https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html)
- [https://repost.aws/knowledge-center/efs-access-points-directory-access](https://repost.aws/knowledge-center/efs-access-points-directory-access)
- [https://www.plerion.com/cloud-knowledge-base/efs-access-points-should-be-configured-to-enforce-a-user-identity](https://www.plerion.com/cloud-knowledge-base/efs-access-points-should-be-configured-to-enforce-a-user-identity)
- [https://docs.aws.amazon.com/efs/latest/ug/enforce-identity-access-points.html](https://docs.aws.amazon.com/efs/latest/ug/enforce-identity-access-points.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-4](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-4)

## 技术信息

- Source Metadata：[sources/aws/efs_access_point_enforce_user_identity/metadata.json](../../sources/aws/efs_access_point_enforce_user_identity/metadata.json)
- Source Code：[sources/aws/efs_access_point_enforce_user_identity/check.py](../../sources/aws/efs_access_point_enforce_user_identity/check.py)
- Source Metadata Path：`sources/aws/efs_access_point_enforce_user_identity/metadata.json`
- Source Code Path：`sources/aws/efs_access_point_enforce_user_identity/check.py`

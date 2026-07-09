# Amazon WorkSpaces workspace root and user volumes are encrypted

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `workspaces_volume_encryption_enabled` |
| 云平台 | AWS |
| 服务 | workspaces |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsEc2Volume |
| 资源组 | compute |

## 描述

**Amazon WorkSpaces** evaluates **encryption at rest** on each workspace's EBS volumes. It checks whether the **root** and **user** volumes are encrypted with a KMS key and identifies workspaces where either volume is unencrypted.

## 风险

Unencrypted volumes allow offline access to files, cached credentials, and profile data from snapshots or underlying storage, harming **confidentiality**. Storage-level access can enable data tampering, impacting **integrity**, and facilitate token reuse for lateral movement.

## 推荐措施

Enable KMS-backed encryption for both **root** and **user** volumes on all WorkSpaces. Prefer **customer-managed keys**, enforce **least privilege** on key use, and enable rotation. Embed encryption into provisioning templates and policies to block unencrypted launches. *Keep required keys enabled for rebuilds and restores*.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: create a WorkSpace with both volumes encrypted
Resources:
  ExampleWorkspace:
    Type: AWS::WorkSpaces::Workspace
    Properties:
      BundleId: <example_bundle_id>
      DirectoryId: <example_directory_id>
      UserName: <example_user_name>
      RootVolumeEncryptionEnabled: true  # Critical: encrypts the root volume to pass the check
      UserVolumeEncryptionEnabled: true  # Critical: encrypts the user volume to pass the check
```

### Terraform

```hcl
# Terraform: create a WorkSpace with both volumes encrypted
resource "aws_workspaces_workspace" "example" {
  bundle_id    = "<example_bundle_id>"
  directory_id = "<example_directory_id>"
  user_name    = "<example_user_name>"

  root_volume_encryption_enabled = true  # Critical: encrypts the root volume
  user_volume_encryption_enabled = true  # Critical: encrypts the user volume
}
```

### Other

1. In the AWS Console, go to WorkSpaces > WorkSpaces and click Launch WorkSpaces
2. Select the directory and user, proceed to the WorkSpaces Configuration step
3. Under Encryption, enable Root volume and User volume
4. Keep the default AWS managed key (aws/workspaces) or select a CMK if required
5. Launch the WorkSpace, then migrate the user and terminate the unencrypted WorkSpace
6. Verify the Volume Encryption column shows Enabled for both volumes

## 参考资料

- [https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WorkSpaces/storage-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WorkSpaces/storage-encryption.html)

## 技术信息

- Source Metadata：[sources/aws/workspaces_volume_encryption_enabled/metadata.json](../../sources/aws/workspaces_volume_encryption_enabled/metadata.json)
- Source Code：[sources/aws/workspaces_volume_encryption_enabled/check.py](../../sources/aws/workspaces_volume_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/workspaces_volume_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/workspaces_volume_encryption_enabled/check.py`

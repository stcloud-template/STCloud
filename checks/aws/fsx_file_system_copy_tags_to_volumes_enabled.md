# FSx file system has copy tags to volumes enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `fsx_file_system_copy_tags_to_volumes_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | fsx |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | storage |

## 説明

**Amazon FSx file systems** are configured to **copy tags to volumes** via `copy_tags_to_volumes`. Identifies file systems where volume resources will not inherit the file system's tags.

## リスク

Without tag propagation, volumes lack consistent labels used for **ABAC**, classification, and automation. This can erode confidentiality through mis-scoped access controls and impact availability if backups or safeguards aren't applied to untagged volumes.

## 推奨事項

Enable `copy_tags_to_volumes` and adopt a **mandatory tagging policy** (owner, environment, data class). Apply **least privilege/ABAC** using tags and integrate tags into backup, retention, and monitoring workflows to enforce **defense in depth**.

## 修正手順


### CLI

```text
aws fsx update-file-system --file-system-id <file-system-id> --open-zfs-configuration CopyTagsToVolumes=true
```

### Native IaC

```yaml
# CloudFormation: Enable copying tags to volumes for FSx for OpenZFS
Resources:
  <example_resource_name>:
    Type: AWS::FSx::FileSystem
    Properties:
      FileSystemType: OPENZFS
      SubnetIds:
        - <example_resource_id>
      OpenZFSConfiguration:
        DeploymentType: SINGLE_AZ_1
        ThroughputCapacity: 64
        CopyTagsToVolumes: true  # Critical: ensures volumes inherit file system tags
```

### Terraform

```hcl
# FSx for OpenZFS with copy tags to volumes enabled
resource "aws_fsx_openzfs_file_system" "<example_resource_name>" {
  deployment_type      = "SINGLE_AZ_1"
  subnet_ids           = ["<example_resource_id>"]
  throughput_capacity  = 64
  copy_tags_to_volumes = true  # Critical: ensures volumes inherit file system tags
}
```

### Other

1. Open the AWS Console and go to Amazon FSx
2. Select your FSx for OpenZFS file system
3. Click Actions > Update file system
4. Set Copy tags to volumes to On
5. Click Update to save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html#fsx-1](https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html#fsx-1)
- [https://docs.aws.amazon.com/config/latest/developerguide/fsx-openzfs-copy-tags-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/fsx-openzfs-copy-tags-enabled.html)
- [https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html)

## 技術情報

- Source Metadata：[sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/metadata.json](../../sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/metadata.json)
- Source Code：[sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/check.py](../../sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/check.py)
- Source Metadata Path：`sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/metadata.json`
- Source Code Path：`sources/aws/fsx_file_system_copy_tags_to_volumes_enabled/check.py`

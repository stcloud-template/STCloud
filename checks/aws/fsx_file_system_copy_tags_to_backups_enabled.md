# FSx file system has copy tags to backups enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `fsx_file_system_copy_tags_to_backups_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | fsx |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsFSxFileSystem |
| リソースグループ | storage |

## 説明

**Amazon FSx file systems** are evaluated for whether they copy **resource tags** to their **backups** via the `copy_tags_to_backups` setting.

## リスク

Missing tag inheritance leaves backups unclassified and outside tag-based controls, weakening confidentiality and availability. Tag-aware IAM and retention policies may not apply, enabling unauthorized access, accidental deletion, or orphaned backups that complicate recovery and inflate costs.

## 推奨事項

Enable tag copying for FSx backups and standardize mandatory tags (owner, data classification, environment). Map **least privilege** and lifecycle policies to these tags, enforce with automation and guardrails, and regularly audit to prevent untagged or misclassified backups.

## 修正手順


### CLI

```text
aws fsx update-file-system --file-system-id <file-system-id> --open-zfs-configuration CopyTagsToBackups=true
```

### Native IaC

```yaml
# CloudFormation: Enable copying tags to backups for FSx OpenZFS
Resources:
  <example_resource_name>:
    Type: AWS::FSx::FileSystem
    Properties:
      FileSystemType: OPENZFS
      OpenZFSConfiguration:
        CopyTagsToBackups: true  # Critical: ensures tags are copied to backups (passes the check)
```

### Terraform

```hcl
# Terraform: Enable copying tags to backups for FSx OpenZFS
resource "aws_fsx_openzfs_file_system" "<example_resource_name>" {
  subnet_ids          = ["<subnet_id>"]
  deployment_type     = "SINGLE_AZ_1"
  throughput_capacity = 64
  storage_capacity    = 128

  copy_tags_to_backups = true # Critical: ensures tags are copied to backups (passes the check)
}
```

### Other

1. Open the AWS Console and go to Amazon FSx
2. Select your FSx file system and choose Actions > Update file system
3. Enable Copy tags to backups
4. Click Update to save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html#fsx-2](https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html#fsx-2)
- [https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/fsx-lustre-copy-tags-to-backups.html](https://docs.aws.amazon.com/config/latest/developerguide/fsx-lustre-copy-tags-to-backups.html)

## 技術情報

- Source Metadata：[sources/aws/fsx_file_system_copy_tags_to_backups_enabled/metadata.json](../../sources/aws/fsx_file_system_copy_tags_to_backups_enabled/metadata.json)
- Source Code：[sources/aws/fsx_file_system_copy_tags_to_backups_enabled/check.py](../../sources/aws/fsx_file_system_copy_tags_to_backups_enabled/check.py)
- Source Metadata Path：`sources/aws/fsx_file_system_copy_tags_to_backups_enabled/metadata.json`
- Source Code Path：`sources/aws/fsx_file_system_copy_tags_to_backups_enabled/check.py`

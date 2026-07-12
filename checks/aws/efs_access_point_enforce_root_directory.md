# EFS file system has no access points allowing access to the root directory

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `efs_access_point_enforce_root_directory` |
| クラウドプラットフォーム | AWS |
| サービス | efs |
| 重大度 | medium |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsEfsAccessPoint |
| リソースグループ | storage |

## 説明

**Amazon EFS access points** are evaluated to ensure they enforce a non-root directory. The check identifies access points whose configured root directory `Path` is `/`, meaning clients would mount the file system's root instead of a scoped subdirectory.

## リスク

Exposing the file system root via an access point undermines **confidentiality** and **integrity** by allowing traversal beyond intended datasets. Attackers or misconfigured apps could: - Read sensitive directories - Modify or delete shared data - Pivot across tenants, impacting **availability**

## 推奨事項

Apply **least privilege**: set each access point `Path` to a dedicated subdirectory and avoid `/`. - Use per-application access points - Enforce POSIX identity and directory permissions - Layer controls (network segmentation, monitoring) for **defense in depth**

## 修正手順


### CLI

```text
aws efs delete-access-point --access-point-id <access-point-id>
```

### Native IaC

```yaml
# CloudFormation: EFS access point enforcing a non-root directory
Resources:
  <example_resource_name>:
    Type: AWS::EFS::AccessPoint
    Properties:
      FileSystemId: <example_resource_id>
      RootDirectory:
        Path: /data  # Critical: set to a non-root path to avoid "/" and pass the check
        # This enforces the access point root to /data instead of the file system root
```

### Terraform

```hcl
# Terraform: EFS access point enforcing a non-root directory
resource "aws_efs_access_point" "<example_resource_name>" {
  file_system_id = "<example_resource_id>"

  root_directory {
    path = "/data"  # Critical: not "/"; enforces a subdirectory as root to pass the check
  }
}
```

### Other

1. In the AWS Console, go to EFS > Access points
2. Select the access point showing Root directory as /
3. Click Delete and confirm
4. Click Create access point
5. Select the file system and set Root directory Path to a non-root path (for example, /data)
6. Click Create access point

## 参考資料

- [https://docs.aws.amazon.com/efs/latest/ug/enforce-root-directory-access-point.html](https://docs.aws.amazon.com/efs/latest/ug/enforce-root-directory-access-point.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-3](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-3)

## 技術情報

- Source Metadata：[sources/aws/efs_access_point_enforce_root_directory/metadata.json](../../sources/aws/efs_access_point_enforce_root_directory/metadata.json)
- Source Code：[sources/aws/efs_access_point_enforce_root_directory/check.py](../../sources/aws/efs_access_point_enforce_root_directory/check.py)
- Source Metadata Path：`sources/aws/efs_access_point_enforce_root_directory/metadata.json`
- Source Code Path：`sources/aws/efs_access_point_enforce_root_directory/check.py`

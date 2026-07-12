# EFS file system policy does not allow access to any client within the VPC

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `efs_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | efs |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| リソースタイプ | AwsEfsFileSystem |
| リソースグループ | storage |

## 説明

**Amazon EFS** file system policy is assessed for **public or VPC-wide access**. Policies with broad `Principal` values or that permit any client in the VPC without the `elasticfilesystem:AccessedViaMountTarget` condition are identified. *An absent or empty policy is treated as open to VPC clients.*

## リスク

Broad EFS access lets any VPC client-or a compromised workload-mount the share, impacting CIA: - Confidentiality: bulk data exfiltration - Integrity: unauthorized writes or ransomware - Availability: deletion or lockout via elevated client access Also facilitates lateral movement within the VPC.

## 推奨事項

Apply **least privilege** to EFS resource policies: - Avoid wildcard `Principal` or `*` - Require `elasticfilesystem:AccessedViaMountTarget=true` - Constrain with `aws:SourceVpc`, `aws:SourceAccount`, or org IDs - Use EFS access points per app/role - Enable EFS **Block Public Access** for defense in depth

## 修正手順


### CLI

```text
aws efs put-file-system-policy --file-system-id <example_resource_id> --policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":"*","Action":"elasticfilesystem:ClientMount","Condition":{"Bool":{"elasticfilesystem:AccessedViaMountTarget":"true"}}}]}'
```

### Native IaC

```yaml
# CloudFormation: attach a non-public EFS file system policy
Resources:
  EFSFileSystemPolicy:
    Type: AWS::EFS::FileSystemPolicy
    Properties:
      FileSystemId: <example_resource_id>
      Policy:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal: "*"
            Action: elasticfilesystem:ClientMount
            Condition:
              Bool:
                elasticfilesystem:AccessedViaMountTarget: "true"  # Critical: restrict access to mount targets only to avoid public access
```

### Terraform

```hcl
# Attach a non-public EFS file system policy
resource "aws_efs_file_system_policy" "<example_resource_name>" {
  file_system_id = "<example_resource_id>"
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = "elasticfilesystem:ClientMount"
      Condition = {
        Bool = {
          "elasticfilesystem:AccessedViaMountTarget" = "true" # Critical: require mount target to make policy non-public
        }
      }
    }]
  })
}
```

### Other

1. In the AWS Console, go to EFS > File systems and select <example_resource_id>
2. Open the File system policy tab and click Edit
3. Replace the policy with one that requires access via mount targets only:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "elasticfilesystem:ClientMount",
         "Condition": {"Bool": {"elasticfilesystem:AccessedViaMountTarget": "true"}}
       }
     ]
   }
   ```
4. Save changes

## 参考資料

- [https://docs.aws.amazon.com/efs/latest/ug/access-control-block-public-access.html](https://docs.aws.amazon.com/efs/latest/ug/access-control-block-public-access.html)
- [https://support.icompaas.com/support/solutions/articles/62000233324-efs-should-not-have-policies-allowing-unrestricted-access-within-vpc](https://support.icompaas.com/support/solutions/articles/62000233324-efs-should-not-have-policies-allowing-unrestricted-access-within-vpc)

## 技術情報

- Source Metadata：[sources/aws/efs_not_publicly_accessible/metadata.json](../../sources/aws/efs_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/efs_not_publicly_accessible/check.py](../../sources/aws/efs_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/efs_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/efs_not_publicly_accessible/check.py`

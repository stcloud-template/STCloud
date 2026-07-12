# Amazon Redshift cluster does not use the default admin username

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `redshift_cluster_non_default_username` |
| クラウドプラットフォーム | AWS |
| サービス | redshift |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | AwsRedshiftCluster |
| リソースグループ | analytics |

## 説明

**Amazon Redshift clusters** are assessed for use of a **non-default admin username**; clusters using the known default `awsuser` are identified.

## リスク

Default admin names make accounts predictable, enabling username enumeration, password spraying, and brute-force attempts. A takeover can expose warehouse data (**confidentiality**), enable unauthorized queries or schema changes (**integrity**), and disrupt analytics workloads (**availability**).

## 推奨事項

Use a **unique, non-predictable** admin username at creation instead of `awsuser`. Apply **least privilege** by using dedicated roles and limiting superuser use. Enforce strong authentication, rotate credentials, and audit access. *For existing clusters*, create a new one with a unique admin and migrate.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Redshift cluster with non-default admin username
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      NodeType: <example_node_type>
      MasterUsername: <new-username>  # Critical: not 'awsuser' to pass the check
      MasterUserPassword: <password>
```

### Terraform

```hcl
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  node_type          = "<example_node_type>"
  cluster_type       = "single-node"
  master_username    = "<new-username>"  # Critical: not 'awsuser' to pass the check
  master_password    = "<password>"
}
```

### Other

1. In the Amazon Redshift console, choose Create cluster
2. Set Admin user name to a value other than awsuser (critical)
3. Enter the required minimal settings (password, node type) and create the cluster
4. Migrate data from the old cluster if needed
5. Delete the old cluster that uses the awsuser admin to remove the failing resource

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-8](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-8)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/master-username.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/master-username.html)
- [https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-prereq.html)

## 技術情報

- Source Metadata：[sources/aws/redshift_cluster_non_default_username/metadata.json](../../sources/aws/redshift_cluster_non_default_username/metadata.json)
- Source Code：[sources/aws/redshift_cluster_non_default_username/check.py](../../sources/aws/redshift_cluster_non_default_username/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_non_default_username/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_non_default_username/check.py`

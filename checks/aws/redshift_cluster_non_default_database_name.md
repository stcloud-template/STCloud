# Redshift cluster does not use the default database name dev

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `redshift_cluster_non_default_database_name` |
| クラウドプラットフォーム | AWS |
| サービス | redshift |
| 重大度 | low |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Discovery |
| リソースタイプ | AwsRedshiftCluster |
| リソースグループ | analytics |

## 説明

**Amazon Redshift clusters** are identified when the database name equals the default `dev`, rather than a custom name.

## リスク

Using the predictable `dev` name weakens **confidentiality** and **integrity**. Mis-scoped IAM or network rules may unintentionally match the database, and known names aid enumeration and targeted connection attempts, increasing the likelihood of unauthorized queries and data exposure.

## 推奨事項

Use a **unique, non-default database name** per cluster. Define a naming standard that avoids generic values (e.g., `dev`, `test`) and supports **least privilege** by preventing broad policy conditions. Review IAM and network rules to reference only intended, explicit resources.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create a Redshift cluster with a non-default DB name
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      NodeType: <NODE_TYPE>
      MasterUsername: <MASTER_USERNAME>
      MasterUserPassword: <MASTER_PASSWORD>
      DBName: <new-db-name>  # Critical: set initial database name to a value other than "dev" to pass the check
```

### Terraform

```hcl
# Terraform: Redshift cluster with non-default database name
resource "aws_redshift_cluster" "example" {
  cluster_identifier = "<example_resource_id>"
  node_type          = "<NODE_TYPE>"
  cluster_type       = "single-node"
  master_username    = "<MASTER_USERNAME>"
  master_password    = "<MASTER_PASSWORD>"
  database_name      = "<new-db-name>" # Critical: ensure this is not "dev" to pass the check
}
```

### Other

1. In the AWS Management Console, go to Amazon Redshift > Provisioned clusters
2. Click Create cluster
3. In Database configurations, set Database name to a value that is not "dev"
4. Complete the wizard and create the cluster
5. Migrate workloads to the new cluster and delete the old cluster that used the default "dev" database name

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-9](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-9)
- [https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)

## 技術情報

- Source Metadata：[sources/aws/redshift_cluster_non_default_database_name/metadata.json](../../sources/aws/redshift_cluster_non_default_database_name/metadata.json)
- Source Code：[sources/aws/redshift_cluster_non_default_database_name/check.py](../../sources/aws/redshift_cluster_non_default_database_name/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_non_default_database_name/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_non_default_database_name/check.py`

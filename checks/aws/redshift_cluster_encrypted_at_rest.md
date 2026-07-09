# Redshift cluster is encrypted at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_encrypted_at_rest` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | critical |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Effects/Data Exposure |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

**Amazon Redshift clusters** use **encryption at rest**. The evaluation inspects the cluster's encryption setting to determine if on-disk data and snapshots are protected with a managed key.

## 风险

Without **encryption at rest**, data blocks and snapshots can be read if storage media or backups are accessed by unauthorized parties. This compromises **confidentiality**, enabling bulk **data exfiltration** and exposure of sensitive analytics, which can facilitate further compromise.

## 推荐措施

Enable **encryption at rest** for all clusters and prefer **customer-managed keys** (`CMEK`) for control and auditing. Apply **least privilege** to key usage, rotate keys, and restrict snapshot access and cross-Region copies. Monitor key health and access events as part of **defense-in-depth**.

## 修复步骤


### CLI

```text
aws redshift modify-cluster --cluster-identifier <cluster-id> --encrypted
```

### Native IaC

```yaml
# CloudFormation: Enable at-rest encryption for a Redshift cluster
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterIdentifier: "<example_resource_id>"
      DBName: "<DB_NAME>"
      MasterUsername: "<MASTER_USERNAME>"
      MasterUserPassword: "<MASTER_PASSWORD>"
      NodeType: "<NODE_TYPE>"
      ClusterType: "<CLUSTER_TYPE>"
      Encrypted: true  # Critical: enables encryption at rest to pass the check
```

### Terraform

```hcl
# Terraform: Enable at-rest encryption for a Redshift cluster
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  node_type          = "<NODE_TYPE>"
  cluster_type       = "<CLUSTER_TYPE>"
  master_username    = "<MASTER_USERNAME>"
  master_password    = "<MASTER_PASSWORD>"

  encrypted = true  # Critical: enables encryption at rest to pass the check
}
```

### Other

1. Open the AWS Management Console and go to Amazon Redshift
2. Choose Clusters, then select your cluster
3. Open the Properties tab > Database configurations > Edit > Edit encryption
4. Select Enable encryption (use AWS-managed or a specific KMS key)
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/redshift/latest/mgmt/changing-cluster-encryption.html](https://docs.aws.amazon.com/redshift/latest/mgmt/changing-cluster-encryption.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-10](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-10)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_encrypted_at_rest/metadata.json](../../sources/aws/redshift_cluster_encrypted_at_rest/metadata.json)
- Source Code：[sources/aws/redshift_cluster_encrypted_at_rest/check.py](../../sources/aws/redshift_cluster_encrypted_at_rest/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_encrypted_at_rest/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_encrypted_at_rest/check.py`

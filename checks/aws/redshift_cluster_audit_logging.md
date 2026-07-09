# Redshift cluster has audit logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_audit_logging` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | medium |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

Amazon Redshift clusters are evaluated for **database audit logging** that exports connection, user, and user-activity events to Amazon S3 or CloudWatch.

## 风险

Without audit logs, malicious logins and queries can evade detection, impacting **confidentiality** (data exfiltration), **integrity** (unauthorized user/role changes), and **availability** of investigations due to missing evidence for forensics and incident response.

## 推荐措施

Enable comprehensive **Redshift audit logging** and include user-activity events. Centralize logs in a protected destination, enforce **least privilege** access, retention, and immutability. Implement **alerts** for anomalous connections and queries as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws redshift enable-logging --cluster-identifier <example_resource_id> --bucket-name <S3_BUCKET_NAME>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      NodeType: dc2.large
      DBName: mydb
      MasterUsername: masteruser
      MasterUserPassword: <PASSWORD>
      # Critical: Enables Redshift audit logging to S3
      LoggingProperties:
        BucketName: <S3_BUCKET_NAME>  # Critical: Required to turn on logging
```

### Terraform

```hcl
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  node_type          = "dc2.large"
  master_username    = "masteruser"
  master_password    = "SuperSecretPassw0rd!"
  cluster_type       = "single-node"

  logging {
    enable      = true                 # Critical: Turns on audit logging
    bucket_name = "<S3_BUCKET_NAME>"  # Critical: S3 destination required
  }
}
```

### Other

1. Open the Amazon Redshift console and go to Clusters
2. Select the target cluster and open the Properties tab
3. In Database audit logging, click Edit
4. Enable logging and select an S3 bucket
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_audit_logging/metadata.json](../../sources/aws/redshift_cluster_audit_logging/metadata.json)
- Source Code：[sources/aws/redshift_cluster_audit_logging/check.py](../../sources/aws/redshift_cluster_audit_logging/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_audit_logging/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_audit_logging/check.py`

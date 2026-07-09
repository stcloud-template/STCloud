# Redshift cluster has Multi-AZ enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_multi_az_enabled` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

**Amazon Redshift clusters** are evaluated for **Multi-AZ deployment** on provisioned `RA3` clusters, confirming compute spans two Availability Zones and is served via a single endpoint.

## 风险

Absent **Multi-AZ**, a single-AZ cluster is exposed to AZ or node failures, leading to dropped connections, aborted queries, and stalled ETL/BI jobs. This reduces **availability**, increases RTO, delays analytics, and risks SLA breaches with cascading pipeline backlogs.

## 推荐措施

Enable **Multi-AZ deployments** for provisioned `RA3` clusters to avoid single-AZ dependency. Align designs to **fault tolerance** and **high availability**: provision sufficient capacity, implement client/ETL retries and reconnects, validate failover periodically, and monitor performance and error rates.

## 修复步骤


### CLI

```text
aws redshift modify-cluster --cluster-identifier <cluster-id> --multi-az
```

### Native IaC

```yaml
# CloudFormation: Enable Multi-AZ on a Redshift cluster
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterIdentifier: <example_resource_id>
      MultiAZ: true  # Critical: enables Multi-AZ so the check passes
```

### Terraform

```hcl
# Enable Multi-AZ on a Redshift cluster
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  multi_az           = true  # Critical: enables Multi-AZ so the check passes
}
```

### Other

1. In the Amazon Redshift console, go to Clusters
2. Select the target cluster
3. Choose Actions > Activate Multi-AZ
4. Confirm and wait until the cluster shows Multi-AZ: Yes

## 参考资料

- [https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-multi-az.html](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-multi-az.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/overview-multi-az.html](https://docs.aws.amazon.com/redshift/latest/mgmt/overview-multi-az.html)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_multi_az_enabled/metadata.json](../../sources/aws/redshift_cluster_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/redshift_cluster_multi_az_enabled/check.py](../../sources/aws/redshift_cluster_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_multi_az_enabled/check.py`

# Redshift cluster has Multi-AZ enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `redshift_cluster_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | redshift |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsRedshiftCluster |
| リソースグループ | analytics |

## 説明

**Amazon Redshift clusters** are evaluated for **Multi-AZ deployment** on provisioned `RA3` clusters, confirming compute spans two Availability Zones and is served via a single endpoint.

## リスク

Absent **Multi-AZ**, a single-AZ cluster is exposed to AZ or node failures, leading to dropped connections, aborted queries, and stalled ETL/BI jobs. This reduces **availability**, increases RTO, delays analytics, and risks SLA breaches with cascading pipeline backlogs.

## 推奨事項

Enable **Multi-AZ deployments** for provisioned `RA3` clusters to avoid single-AZ dependency. Align designs to **fault tolerance** and **high availability**: provision sufficient capacity, implement client/ETL retries and reconnects, validate failover periodically, and monitor performance and error rates.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-multi-az.html](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-multi-az.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/overview-multi-az.html](https://docs.aws.amazon.com/redshift/latest/mgmt/overview-multi-az.html)

## 技術情報

- Source Metadata：[sources/aws/redshift_cluster_multi_az_enabled/metadata.json](../../sources/aws/redshift_cluster_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/redshift_cluster_multi_az_enabled/check.py](../../sources/aws/redshift_cluster_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_multi_az_enabled/check.py`

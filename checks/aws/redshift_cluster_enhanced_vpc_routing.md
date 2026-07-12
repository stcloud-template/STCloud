# Redshift cluster has Enhanced VPC Routing enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `redshift_cluster_enhanced_vpc_routing` |
| クラウドプラットフォーム | AWS |
| サービス | redshift |
| 重大度 | medium |
| カテゴリ | trust-boundaries, internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsRedshiftCluster |
| リソースグループ | analytics |

## 説明

**Amazon Redshift clusters** are assessed for the `EnhancedVpcRouting` setting, which routes all `COPY` and `UNLOAD` traffic between the cluster and data repositories through the VPC, enabling use of VPC security controls and logging.

## リスク

**Without enhanced VPC routing**, `COPY`/`UNLOAD` transfers can leave VPC oversight, reducing control and visibility. - VPC egress filtering and endpoint policies can be bypassed (confidentiality) - Limited flow-log telemetry (visibility) - Higher risk of unauthorized exfiltration or tampering (confidentiality, integrity)

## 推奨事項

Enable `EnhancedVpcRouting` and enforce **least privilege** egress: - Prefer private access with VPC endpoints and restrictive policies - Constrain outbound paths via security groups, NACLs, and routing - Monitor transfers with VPC Flow Logs This strengthens **defense in depth** and **zero trust** for data movement.

## 修正手順


### CLI

```text
aws redshift modify-cluster --cluster-identifier <cluster-id> --enhanced-vpc-routing
```

### Native IaC

```yaml
# CloudFormation: Enable Enhanced VPC Routing on a Redshift cluster
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterIdentifier: <example_resource_name>
      ClusterType: single-node
      NodeType: ra3.xlplus
      DBName: dev
      MasterUsername: <USERNAME>
      MasterUserPassword: <PASSWORD>
      EnhancedVpcRouting: true  # Critical: forces COPY/UNLOAD traffic through the VPC
```

### Terraform

```hcl
# Terraform: Enable Enhanced VPC Routing on a Redshift cluster
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier  = "<example_resource_name>"
  cluster_type        = "single-node"
  node_type           = "ra3.xlplus"
  master_username     = "<USERNAME>"
  master_password     = "<PASSWORD>"
  enhanced_vpc_routing = true  # Critical: routes COPY/UNLOAD via VPC
}
```

### Other

1. Open the AWS Console and go to Amazon Redshift
2. Choose Provisioned clusters, select your cluster
3. Click Actions > Modify
4. In Network and security, turn on Enhanced VPC routing
5. Click Save changes (apply immediately if prompted)

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-7](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-7)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/enable-enhanced-vpc-routing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/enable-enhanced-vpc-routing.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html)

## 技術情報

- Source Metadata：[sources/aws/redshift_cluster_enhanced_vpc_routing/metadata.json](../../sources/aws/redshift_cluster_enhanced_vpc_routing/metadata.json)
- Source Code：[sources/aws/redshift_cluster_enhanced_vpc_routing/check.py](../../sources/aws/redshift_cluster_enhanced_vpc_routing/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_enhanced_vpc_routing/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_enhanced_vpc_routing/check.py`

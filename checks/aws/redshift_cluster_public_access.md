# Redshift cluster is not publicly exposed to the Internet

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_public_access` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

Amazon Redshift clusters with `publicly accessible` endpoints in **public subnets** and security groups allowing TCP from `0.0.0.0/0` or `::/0` are identified as internet-exposed. Public endpoints without internet reachability due to private subnets or restrictive rules are recognized separately.

## 风险

Internet-exposed Redshift endpoints allow direct DB access from any host, impacting: - **Confidentiality**: credential brute force, unauthorized queries, data exfiltration - **Integrity**: unauthorized writes or schema changes - **Availability**: scanning/abuse leading to connection exhaustion or disruption

## 推荐措施

Prefer **private connectivity**: disable public access, place clusters in private subnets, and apply **least privilege** security groups limited to trusted CIDRs or VPC sources. Use **defense in depth** with VPN/peering/endpoints, strong authentication, and monitoring. Avoid `0.0.0.0/0` or `::/0` to database ports.

## 修复步骤


### CLI

```text
aws redshift modify-cluster --cluster-identifier <CLUSTER_ID> --no-publicly-accessible
```

### Native IaC

```yaml
# CloudFormation: Redshift cluster not publicly accessible
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      DBName: <example_db_name>
      MasterUsername: <example_username>
      MasterUserPassword: <example_password>
      NodeType: dc2.large
      PubliclyAccessible: false  # Critical: disables public access to prevent Internet exposure
```

### Terraform

```hcl
# Redshift cluster not publicly accessible
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier  = "<example_resource_id>"
  node_type           = "dc2.large"
  cluster_type        = "single-node"
  master_username     = "<example_username>"
  master_password     = "<example_password>"

  publicly_accessible = false  # Critical: disables public access to prevent Internet exposure
}
```

### Other

1. Open the AWS Management Console and go to Amazon Redshift
2. Select your cluster
3. Click Edit (or Actions > Modify)
4. Set Publicly accessible to Off/No
5. Save changes and apply the modification

## 参考资料

- [https://docs.aws.amazon.com/de_de/redshift/latest/mgmt/rs-ra3-VPC-public-private.html](https://docs.aws.amazon.com/de_de/redshift/latest/mgmt/rs-ra3-VPC-public-private.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/redshift-cluster-publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/redshift-cluster-publicly-accessible.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-vpc.html)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_public_access/metadata.json](../../sources/aws/redshift_cluster_public_access/metadata.json)
- Source Code：[sources/aws/redshift_cluster_public_access/check.py](../../sources/aws/redshift_cluster_public_access/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_public_access/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_public_access/check.py`

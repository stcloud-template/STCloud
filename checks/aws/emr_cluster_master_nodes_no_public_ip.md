# EMR Cluster without Public IP.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `emr_cluster_master_nodes_no_public_ip` |
| クラウドプラットフォーム | AWS |
| サービス | emr |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Amazon EMR clusters** in non-terminated states are assessed for **public IP assignment** on cluster nodes (primary and workers). The finding identifies clusters whose instances are reachable via public IPs rather than private VPC addresses.

## リスク

**Publicly reachable EMR nodes** expose admin UIs and SSH to the Internet, enabling brute force and service exploits. A compromised primary node can alter jobs and exfiltrate data from S3/HDFS, degrading **confidentiality** and **integrity**, and disrupt workloads, impacting **availability**.

## 推奨事項

Run EMR in **private subnets** without public IPs. Use **VPC endpoints** for AWS services and **NAT** only when needed. Enforce **least privilege** security groups, avoid `0.0.0.0/0`, and prefer **SSM** or a bastion for admin access. Keep **EMR block public access** enabled and favor **private connectivity** for external dependencies.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Launch EMR in a private subnet (no public IPs)
Resources:
  <example_resource_name>:
    Type: AWS::EMR::Cluster
    Properties:
      Name: <example_resource_name>
      ReleaseLabel: emr-6.10.0
      ServiceRole: EMR_DefaultRole
      JobFlowRole: EMR_EC2_DefaultRole
      Instances:
        Ec2SubnetId: <example_resource_id>  # CRITICAL: use a PRIVATE subnet to prevent public IPs
        InstanceGroups:
          - InstanceRole: MASTER
            InstanceType: m5.xlarge
            InstanceCount: 1
          - InstanceRole: CORE
            InstanceType: m5.xlarge
            InstanceCount: 1
```

### Terraform

```hcl
# Terraform: Launch EMR in a private subnet (no public IPs)
resource "aws_emr_cluster" "<example_resource_name>" {
  name                = "<example_resource_name>"
  release_label       = "emr-6.10.0"
  master_instance_type = "m5.xlarge"
  core_instance_type   = "m5.xlarge"

  service_role = "EMR_DefaultRole"
  ec2_attributes {
    instance_profile = "EMR_EC2_DefaultRole"
    subnet_id        = "<example_resource_id>"  # CRITICAL: private subnet ensures no public IPs
  }
}
```

### Other

1. In the AWS Console, go to EMR > Clusters, select the non-compliant cluster (with Public IP) and choose Terminate.
2. Click Create cluster.
3. Under Networking, select your VPC and choose a private Subnet (no auto-assign public IPv4).
4. Create the cluster. Its instances will launch without public IPs.

## 参考資料

- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-vpc-subnet.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-vpc-subnet.html)
- [https://aws.amazon.com/blogs/aws/new-launch-amazon-emr-clusters-in-private-subnets/](https://aws.amazon.com/blogs/aws/new-launch-amazon-emr-clusters-in-private-subnets/)
- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html)
- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-clusters-in-a-vpc.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-clusters-in-a-vpc.html)
- [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-vpc-launching-job-flows.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-vpc-launching-job-flows.html)

## 技術情報

- Source Metadata：[sources/aws/emr_cluster_master_nodes_no_public_ip/metadata.json](../../sources/aws/emr_cluster_master_nodes_no_public_ip/metadata.json)
- Source Code：[sources/aws/emr_cluster_master_nodes_no_public_ip/check.py](../../sources/aws/emr_cluster_master_nodes_no_public_ip/check.py)
- Source Metadata Path：`sources/aws/emr_cluster_master_nodes_no_public_ip/metadata.json`
- Source Code Path：`sources/aws/emr_cluster_master_nodes_no_public_ip/check.py`

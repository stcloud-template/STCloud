# EKS cluster has private endpoint access enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eks_cluster_private_nodes_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | eks |
| 重大度 | high |
| カテゴリ | internet-exposed, trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | AwsEksCluster |
| リソースグループ | container |

## 説明

**Amazon EKS cluster** has **private endpoint access** enabled for the **Kubernetes API server**, allowing control plane traffic to use a VPC-resolved private endpoint. The check evaluates the cluster's `endpointPrivateAccess` setting.

## リスク

Without **private endpoint access**, the API server is exposed on the public internet. This expands attack surface and weakens **confidentiality** and **integrity**: stolen creds or mis-scoped CIDRs can enable unauthorized API calls, secret reads, pod deployments, and config changes. **Availability** also depends on internet egress, increasing failure modes.

## 推奨事項

Enable **private endpoint access** and disable or tightly restrict the public endpoint. Require administration from private networks, enforce **least privilege** with IAM/RBAC, and apply **defense in depth** via segmentation and logging. *If external access is needed*, allow only specific CIDRs and monitor API activity.

## 修正手順


### CLI

```text
aws eks update-cluster-config --region <REGION> --name <CLUSTER_NAME> --resources-vpc-config endpointPrivateAccess=true
```

### Native IaC

```yaml
# CloudFormation: Enable private endpoint access for an EKS cluster
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn: <example_resource_id>
      ResourcesVpcConfig:
        SubnetIds:
          - <example_resource_id>
        EndpointPrivateAccess: true  # Critical: enables private endpoint access to pass the check
```

### Terraform

```hcl
# Terraform: Enable private endpoint access for an EKS cluster
resource "aws_eks_cluster" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_resource_id>"

  vpc_config {
    subnet_ids              = ["<example_resource_id>"]
    endpoint_private_access = true  # Critical: enables private API endpoint access to pass the check
  }
}
```

### Other

1. In the AWS Console, open Amazon EKS and select your cluster
2. Go to the Networking tab
3. Click Edit next to Cluster endpoint access
4. Enable Private access
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/userguide/private-clusters.html](https://docs.aws.amazon.com/eks/latest/userguide/private-clusters.html)
- [https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html)

## 技術情報

- Source Metadata：[sources/aws/eks_cluster_private_nodes_enabled/metadata.json](../../sources/aws/eks_cluster_private_nodes_enabled/metadata.json)
- Source Code：[sources/aws/eks_cluster_private_nodes_enabled/check.py](../../sources/aws/eks_cluster_private_nodes_enabled/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_private_nodes_enabled/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_private_nodes_enabled/check.py`

# EKS cluster has network policy enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `eks_cluster_network_policy_enabled` |
| 云平台 | AWS |
| 服务 | eks |
| 严重等级 | high |
| 类别 | trust-boundaries, cluster-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Lateral Movement |
| 资源类型 | AwsEksCluster |
| 资源组 | container |

## 描述

**Amazon EKS clusters** are evaluated for **pod-level network isolation** via Kubernetes `NetworkPolicy`, indicating whether traffic between pods and namespaces is restricted according to defined rules.

## 风险

Without **NetworkPolicy**, pods can communicate freely, enabling **lateral movement**, **data exfiltration**, and abuse of internal services. Unrestricted east-west traffic undermines confidentiality and integrity and enlarges the blast radius of a single compromised pod.

## 推荐措施

Enforce **least privilege** `NetworkPolicy` with a `default-deny` for ingress and egress, then explicitly allow required flows by labels and namespaces. Apply **defense in depth** with security groups for pods and private access, and continuously test and monitor policy effectiveness.

## 修复步骤


### CLI

```text
aws eks update-cluster-config --name <example_cluster_name> --resources-vpc-config securityGroupIds=<example_security_group_id>
```

### Native IaC

```yaml
# CloudFormation: attach a security group to the EKS cluster
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn: <example_role_arn>
      ResourcesVpcConfig:
        SubnetIds:
          - <example_subnet_id>
        SecurityGroupIds:
          - <example_security_group_id>  # Critical: sets a security group for the cluster, satisfying the check
```

### Terraform

```hcl
# Minimal EKS cluster config with a security group attached
resource "aws_eks_cluster" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  vpc_config {
    subnet_ids         = ["<example_subnet_id>"]
    security_group_ids = ["<example_security_group_id>"]  # Critical: attaches a security group to pass the check
  }
}
```

### Other

1. Open the AWS Console and go to EKS > Clusters
2. Select <your cluster> and open the Networking tab
3. Click Edit (or Update) in the Networking section
4. Under Security groups, add/select <example_security_group_id>
5. Click Save to apply

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/security-groups.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/security-groups.html)
- [https://docs.aws.amazon.com/eks/latest/userguide/eks-networking-add-ons.html](https://docs.aws.amazon.com/eks/latest/userguide/eks-networking-add-ons.html)
- [https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html)

## 技术信息

- Source Metadata：[sources/aws/eks_cluster_network_policy_enabled/metadata.json](../../sources/aws/eks_cluster_network_policy_enabled/metadata.json)
- Source Code：[sources/aws/eks_cluster_network_policy_enabled/check.py](../../sources/aws/eks_cluster_network_policy_enabled/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_network_policy_enabled/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_network_policy_enabled/check.py`

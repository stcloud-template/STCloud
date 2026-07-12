# EKS cluster endpoint is not publicly accessible from 0.0.0.0/0

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eks_cluster_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | eks |
| 重大度 | high |
| カテゴリ | internet-exposed, cluster-security |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsEksCluster |
| リソースグループ | container |

## 説明

**Amazon EKS** cluster API server endpoint is evaluated for **unrestricted Internet access**, specifically when the public endpoint permits connections from `0.0.0.0/0` instead of private access or limited CIDR ranges.

## リスク

An openly reachable API endpoint enables Internet-wide probing, brute force, and enumeration, increasing exposure to RBAC misconfigurations or API flaws. Successful access can drive secret exfiltration (confidentiality), workload tampering (integrity), and control-plane disruption or scaling abuse (availability, cost).

## 推奨事項

Prefer **private endpoint access** and avoid broad exposure. *If public access is required*, restrict to trusted admin CIDRs (not `0.0.0.0/0`), reach the API via **VPN/Direct Connect or bastions**, and enforce **least privilege** with IAM/RBAC. Apply **defense in depth** through network segmentation and continuous monitoring.

## 修正手順


### CLI

```text
aws eks update-cluster-config --region <region_name> --name <cluster_name> --resources-vpc-config endpointPublicAccess=false,endpointPrivateAccess=true
```

### Native IaC

```yaml
# CloudFormation: Disable public endpoint and enable private endpoint
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn: <example_role_arn>
      ResourcesVpcConfig:
        SubnetIds:
          - <example_subnet_id_1>
          - <example_subnet_id_2>
        EndpointPublicAccess: false  # critical: disables public API endpoint
        EndpointPrivateAccess: true  # critical: enables private API endpoint
```

### Terraform

```hcl
# Terraform: Disable public endpoint and enable private endpoint
resource "aws_eks_cluster" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  vpc_config {
    subnet_ids              = ["<example_subnet_id_1>", "<example_subnet_id_2>"]
    endpoint_public_access  = false  # critical: disables public API endpoint
    endpoint_private_access = true   # critical: enables private API endpoint
  }
}
```

### Other

1. Open the Amazon EKS console
2. Select your cluster
3. Go to the Networking tab and click Manage endpoint access
4. Enable Private access and Disable Public access
5. Click Update/Save

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/eksctl/vpc-cluster-access.html](https://docs.aws.amazon.com/eks/latest/eksctl/vpc-cluster-access.html)
- [https://docs.aws.amazon.com/eks/latest/userguide/config-cluster-endpoint.html](https://docs.aws.amazon.com/eks/latest/userguide/config-cluster-endpoint.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/endpoint-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/endpoint-access.html)

## 技術情報

- Source Metadata：[sources/aws/eks_cluster_not_publicly_accessible/metadata.json](../../sources/aws/eks_cluster_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/eks_cluster_not_publicly_accessible/check.py](../../sources/aws/eks_cluster_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_not_publicly_accessible/check.py`

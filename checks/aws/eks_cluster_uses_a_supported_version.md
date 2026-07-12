# EKS cluster uses a supported Kubernetes version

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eks_cluster_uses_a_supported_version` |
| クラウドプラットフォーム | AWS |
| サービス | eks |
| 重大度 | high |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEksCluster |
| リソースグループ | container |

## 説明

Amazon EKS clusters use a **supported Kubernetes version** at or above the defined baseline (e.g., `1.28+`). The evaluation compares each cluster's Kubernetes minor version to the minimum supported level and highlights clusters running below that baseline.

## リスク

Running an **unsupported Kubernetes version** removes upstream and EKS security fixes, exposing clusters to known CVEs and privilege escalation bugs (**confidentiality/integrity**). Deprecated or removed APIs can break controllers and add-ons, causing outages (**availability**).

## 推奨事項

Adopt a **version management policy**: keep clusters on a supported minor version, schedule regular upgrades, and test workloads for API deprecations. Upgrade nodes and add-ons with the control plane. Track EKS releases, automate drift alerts, and favor **defense in depth** over deprecated features.

## 修正手順


### CLI

```text
aws eks update-cluster-version --name <cluster_name> --kubernetes-version <supported_version>
```

### Native IaC

```yaml
# CloudFormation: update EKS cluster to a supported Kubernetes version
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      Name: <example_resource_name>
      RoleArn: <example_role_arn>
      ResourcesVpcConfig:
        SubnetIds: ["<example_subnet_id>"]
      Version: "<supported_version>"  # Critical: set a supported Kubernetes version to pass the check
```

### Terraform

```hcl
# Terraform: update EKS cluster to a supported Kubernetes version
resource "aws_eks_cluster" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  version = "<supported_version>" # Critical: set a supported Kubernetes version to pass the check

  vpc_config {
    subnet_ids = ["<example_subnet_id>"]
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon EKS
2. Select your cluster (<cluster_name>)
3. Click Update (or Edit) next to Kubernetes version
4. Choose a supported version (>= required) and confirm the update
5. Wait for the control plane update to complete

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/kubernetes-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/kubernetes-version.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-2](https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-2)
- [https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html)

## 技術情報

- Source Metadata：[sources/aws/eks_cluster_uses_a_supported_version/metadata.json](../../sources/aws/eks_cluster_uses_a_supported_version/metadata.json)
- Source Code：[sources/aws/eks_cluster_uses_a_supported_version/check.py](../../sources/aws/eks_cluster_uses_a_supported_version/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_uses_a_supported_version/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_uses_a_supported_version/check.py`

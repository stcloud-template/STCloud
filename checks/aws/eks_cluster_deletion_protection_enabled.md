# EKS cluster has deletion protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eks_cluster_deletion_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | eks |
| 重大度 | high |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Destruction |
| リソースタイプ | AwsEksCluster |
| リソースグループ | container |

## 説明

**Amazon EKS clusters** have **deletion protection** enabled blocking cluster removal until protection is explicitly disabled.

## リスク

Without **deletion protection**, automation errors or a compromised admin can remove the cluster control plane, causing immediate **availability** loss and downtime. Destructive actions can also affect the **integrity** of deployments, leave orphaned resources, hinder recovery, and raise **operational cost**.

## 推奨事項

Enable **deletion protection** on critical clusters (`deletionProtection=true`). Enforce **least privilege** so only narrowly scoped roles can disable or delete clusters. Require **change control** with approvals and **separation of duties**, and apply guardrails to prevent broad delete permissions.

## 修正手順


### CLI

```text
aws eks update-cluster-config --name <cluster_name> --region <region_name> --deletion-protection
```

### Native IaC

```yaml
# CloudFormation: enable deletion protection on the EKS cluster
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn: <example_role_arn>
      ResourcesVpcConfig:
        SubnetIds: [<example_subnet_id_1>, <example_subnet_id_2>]
      DeletionProtection: true  # critical: prevents cluster deletion until disabled
```

### Terraform

```hcl
# Enable deletion protection for the EKS cluster
resource "aws_eks_cluster" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  vpc_config {
    subnet_ids = ["<subnet_id_1>", "<subnet_id_2>"]
  }

  deletion_protection = true  # critical: prevents cluster deletion until disabled
}
```

### Other

1. Open the AWS Management Console and go to Amazon EKS
2. Select your cluster
3. Go to the Configuration tab and click Edit
4. Enable Deletion protection
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterConfig.html)
- [https://docs.aws.amazon.com/eks/latest/userguide/deletion-protection.html](https://docs.aws.amazon.com/eks/latest/userguide/deletion-protection.html)

## 技術情報

- Source Metadata：[sources/aws/eks_cluster_deletion_protection_enabled/metadata.json](../../sources/aws/eks_cluster_deletion_protection_enabled/metadata.json)
- Source Code：[sources/aws/eks_cluster_deletion_protection_enabled/check.py](../../sources/aws/eks_cluster_deletion_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_deletion_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_deletion_protection_enabled/check.py`

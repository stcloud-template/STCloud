# EKS cluster has Kubernetes secrets encryption enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `eks_cluster_kms_cmk_encryption_in_secrets_enabled` |
| 云平台 | AWS |
| 服务 | eks |
| 严重等级 | medium |
| 类别 | encryption, cluster-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsEksCluster |
| 资源组 | container |

## 描述

**Amazon EKS** clusters configure **AWS KMS envelope encryption** so Kubernetes **Secrets** are stored in etcd as ciphertext at rest.

## 风险

Without KMS-backed encryption, etcd data and snapshots can reveal plaintext secrets. Attackers with API, node, or storage access can steal tokens, passwords, and keys, enabling impersonation, pod takeover, and lateral movement-compromising confidentiality and leading to privilege escalation.

## 推荐措施

Enable cluster-level secrets encryption with **AWS KMS** and prefer a **customer managed KMS key** for control and rotation. Apply **least privilege** to key policies and cluster roles, monitor key usage, and combine with strict **RBAC** to limit who can read or create secrets as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws eks associate-encryption-config --cluster-name <example_resource_name> --encryption-config '[{"resources":["secrets"],"provider":{"keyArn":"arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<example_resource_id>"}}]'
```

### Native IaC

```yaml
# CloudFormation: enable KMS envelope encryption for Kubernetes secrets
Resources:
  EKSCluster:
    Type: AWS::EKS::Cluster
    Properties:
      Name: "<example_resource_name>"
      RoleArn: "arn:aws:iam::<ACCOUNT_ID>:role/<example_resource_name>"
      ResourcesVpcConfig:
        SubnetIds:
          - "<example_resource_id>"
          - "<example_resource_id>"
      EncryptionConfig:                # Critical: enables KMS encryption for Kubernetes secrets
        - Resources:
            - secrets                  # Critical: encrypts only Kubernetes secrets
          Provider:
            KeyArn: "arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<example_resource_id>"  # Critical: KMS key used for encryption
```

### Terraform

```hcl
# Enable KMS envelope encryption for Kubernetes secrets
resource "aws_eks_cluster" "main" {
  name     = "<example_resource_name>"
  role_arn = "arn:aws:iam::<ACCOUNT_ID>:role/<example_resource_name>"

  vpc_config {
    subnet_ids = ["<example_resource_id>", "<example_resource_id>"]
  }

  encryption_config {                 # Critical: enables KMS encryption for secrets
    resources = ["secrets"]          # Critical: scope to Kubernetes secrets
    provider {
      key_arn = "arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<example_resource_id>"  # Critical: KMS key
    }
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon EKS
2. Select your cluster
3. On the Overview tab, find Secrets encryption and click Enable
4. Select the KMS key and click Enable
5. Click Confirm to apply

## 参考资料

- [https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/eks.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/eks.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/enable-envelope-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EKS/enable-envelope-encryption.html)
- [https://devoriales.com/post/329/aws-eks-secret-encryption-securing-your-eks-secrets-at-rest-with-aws-kms](https://devoriales.com/post/329/aws-eks-secret-encryption-securing-your-eks-secrets-at-rest-with-aws-kms)
- [https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html)

## 技术信息

- Source Metadata：[sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/metadata.json](../../sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/metadata.json)
- Source Code：[sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/check.py](../../sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/check.py)
- Source Metadata Path：`sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/metadata.json`
- Source Code Path：`sources/aws/eks_cluster_kms_cmk_encryption_in_secrets_enabled/check.py`

# ECR repository has image tag immutability enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecr_repositories_tag_immutability` |
| 云平台 | AWS |
| 服务 | ecr |
| 严重等级 | medium |
| 类别 | container-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsEcrRepository |
| 资源组 | container |

## 描述

Amazon ECR repositories are assessed for **image tag immutability**. Repositories permitting tag updates (`MUTABLE`) are identified; those enforcing immutable tags (such as `IMMUTABLE`) are recognized.

## 风险

Mutable tags allow replacing the image behind a trusted tag, undermining release **integrity**. This enables supply-chain injection, unintended rollouts, and backdoored deployments, harming **availability**. Malicious images can exfiltrate data, impacting **confidentiality**.

## 推荐措施

Enable **tag immutability** so tags map to a single artifact. Use **versioned tags** per build, block retagging in CI/CD, and apply **least privilege** for push actions. Layer **image signing** and admission controls to run only trusted images. *If exceptions are needed, keep them narrow and monitored.*

## 修复步骤


### CLI

```text
aws ecr put-image-tag-mutability --repository-name <repository-name> --image-tag-mutability IMMUTABLE
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECR::Repository
    Properties:
      ImageTagMutability: IMMUTABLE  # Critical: enables tag immutability to prevent tag overwrites
```

### Terraform

```hcl
resource "aws_ecr_repository" "<example_resource_name>" {
  name                 = "<example_resource_name>"
  image_tag_mutability = "IMMUTABLE" # Critical: enables tag immutability to prevent tag overwrites
}
```

### Other

1. Open the Amazon ECR console
2. Go to Repositories (Private) and select the repository
3. Click Actions > Edit
4. Set Image tag immutability to Immutable
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-tag-immutability-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-tag-immutability-enabled.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-2](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-2)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html)

## 技术信息

- Source Metadata：[sources/aws/ecr_repositories_tag_immutability/metadata.json](../../sources/aws/ecr_repositories_tag_immutability/metadata.json)
- Source Code：[sources/aws/ecr_repositories_tag_immutability/check.py](../../sources/aws/ecr_repositories_tag_immutability/check.py)
- Source Metadata Path：`sources/aws/ecr_repositories_tag_immutability/metadata.json`
- Source Code Path：`sources/aws/ecr_repositories_tag_immutability/check.py`

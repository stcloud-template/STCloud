# ECR repository has a lifecycle policy configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecr_repositories_lifecycle_policy_enabled` |
| 云平台 | AWS |
| 服务 | ecr |
| 严重等级 | low |
| 类别 | container-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Resource Consumption |
| 资源类型 | AwsEcrRepository |
| 资源组 | container |

## 描述

Amazon ECR repositories have a **lifecycle policy** configured to automatically expire container images based on age, count, or tags.

## 风险

Without **lifecycle policies**, images accumulate indefinitely, leading to: - **Availability** issues when quotas block pushes and CI/CD - **Integrity** risk from redeploying outdated, vulnerable images - **Cost** growth from unnecessary storage

## 推荐措施

Implement **lifecycle policies** per repository to expire untagged, old, or excess images and retain a small set of trusted releases. Validate outcomes before applying, review rules regularly, and apply consistently across Regions when replicating. This supports **defense in depth** by reducing image attack surface and operational risk.

## 修复步骤


### CLI

```text
aws ecr put-lifecycle-policy --repository-name <REPOSITORY_NAME> --lifecycle-policy-text '{"rules":[{"rulePriority":1,"selection":{"tagStatus":"untagged","countType":"imageCountMoreThan","countNumber":1},"action":{"type":"expire"}}]}'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECR::Repository
    Properties:
      # Critical: Adding a lifecycle policy makes the repo PASS this check
      LifecyclePolicy:
        # Critical: The policy content; any valid rule satisfies the requirement
        LifecyclePolicyText: >-
          {"rules":[{"rulePriority":1,"selection":{"tagStatus":"untagged","countType":"imageCountMoreThan","countNumber":1},"action":{"type":"expire"}}]}
```

### Terraform

```hcl
resource "aws_ecr_lifecycle_policy" "<example_resource_name>" {
  repository = "<example_resource_name>"
  # Critical: The policy ensures a lifecycle policy is configured for the repo
  policy = <<POLICY
{"rules":[{"rulePriority":1,"selection":{"tagStatus":"untagged","countType":"imageCountMoreThan","countNumber":1},"action":{"type":"expire"}}]}
POLICY
}
```

### Other

1. Open the AWS Console and go to Amazon ECR > Repositories
2. Select the target repository
3. From Actions, choose "Lifecycle policies"
4. Click "Create rule"
5. Set Image status: Untagged, Match criteria: Image count more than = 1, Action: Expire
6. Click "Save" to apply the lifecycle policy

## 参考资料

- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/lp_creation.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lp_creation.html)
- [https://aws.plainenglish.io/automation-deletion-untagged-container-image-in-amazon-ecr-using-ecr-lifecycle-policy-995eae2f5b8d](https://aws.plainenglish.io/automation-deletion-untagged-container-image-in-amazon-ecr-using-ecr-lifecycle-policy-995eae2f5b8d)
- [https://blog.stackademic.com/title-implementing-lifecycle-policies-in-aws-ecr-a-practical-guide-3860b612b477](https://blog.stackademic.com/title-implementing-lifecycle-policies-in-aws-ecr-a-practical-guide-3860b612b477)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECR/lifecycle-policy-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECR/lifecycle-policy-in-use.html)

## 技术信息

- Source Metadata：[sources/aws/ecr_repositories_lifecycle_policy_enabled/metadata.json](../../sources/aws/ecr_repositories_lifecycle_policy_enabled/metadata.json)
- Source Code：[sources/aws/ecr_repositories_lifecycle_policy_enabled/check.py](../../sources/aws/ecr_repositories_lifecycle_policy_enabled/check.py)
- Source Metadata Path：`sources/aws/ecr_repositories_lifecycle_policy_enabled/metadata.json`
- Source Code Path：`sources/aws/ecr_repositories_lifecycle_policy_enabled/check.py`

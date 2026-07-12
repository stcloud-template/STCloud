# ECS task definition has all containers with read-only root filesystems

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecs_task_definitions_containers_readonly_access` |
| クラウドプラットフォーム | AWS |
| サービス | ecs |
| 重大度 | high |
| カテゴリ | container-security |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS Host Hardening Benchmarks |
| リソースタイプ | AwsEcsTaskDefinition |
| リソースグループ | container |

## 説明

Amazon ECS task definitions specify whether container root filesystems are **read-only** via `readonlyRootFilesystem`. Containers where this setting is absent or set to `false` effectively have write access to the root filesystem.

## リスク

A **writable root filesystem** enables runtime tampering and persistence. Attackers can modify binaries or configs, drop implants, or delete critical files, degrading **integrity** and **availability**. Access to writable paths can also expose secrets and logs, eroding **confidentiality** and complicating incident response.

## 推奨事項

Enforce `readonlyRootFilesystem: true` for containers. - Grant write access only via specific volumes required by the app - Apply **least privilege** and **defense in depth**: run as non-root, drop unnecessary capabilities, and keep images immutable so runtime writes aren't needed

## 修正手順


### CLI

```text
aws ecs register-task-definition --family <task-family> --container-definitions '[{"name":"<container-name>","image":"<image>","readonlyRootFilesystem":true}]'
```

### Native IaC

```yaml
# CloudFormation: ECS task definition with read-only root filesystem
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: <example_resource_name>
      ContainerDefinitions:
        - Name: <example_resource_name>
          Image: <image>
          ReadonlyRootFilesystem: true  # Critical: enforces read-only root FS for the container
```

### Terraform

```hcl
# ECS task definition with read-only root filesystem
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family                = "<example_resource_name>"
  container_definitions = jsonencode([
    {
      name                   = "<example_resource_name>"
      image                  = "<image>"
      readonlyRootFilesystem = true  # Critical: enforces read-only root FS for the container
    }
  ])
}
```

### Other

1. In the AWS Console, go to Amazon ECS > Task Definitions
2. Select the task family <task-family> and click Create new revision
3. For each container, edit and enable Read-only root filesystem (readonlyRootFilesystem = true)
4. Click Create to register the new revision
5. (If needed) Update services to use the new revision

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-readonly-access.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-readonly-access.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/userguide/task_definition_parameters.html#container_definition_readonly](https://docs.aws.amazon.com/AmazonECS/latest/userguide/task_definition_parameters.html#container_definition_readonly)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-5](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-5)

## 技術情報

- Source Metadata：[sources/aws/ecs_task_definitions_containers_readonly_access/metadata.json](../../sources/aws/ecs_task_definitions_containers_readonly_access/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_containers_readonly_access/check.py](../../sources/aws/ecs_task_definitions_containers_readonly_access/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_containers_readonly_access/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_containers_readonly_access/check.py`

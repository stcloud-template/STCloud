# ECS task definition has no privileged containers

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecs_task_definitions_no_privileged_containers` |
| クラウドプラットフォーム | AWS |
| サービス | ecs |
| 重大度 | high |
| カテゴリ | container-security |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS Host Hardening Benchmarks, TTPs/Privilege Escalation |
| リソースタイプ | AwsEcsTaskDefinition |
| リソースグループ | container |

## 説明

**Amazon ECS task definitions** are evaluated for containers configured with **privileged mode** (`privileged: true`). The outcome indicates whether any container definition enables this setting.

## リスク

**Privileged containers** can act with host-level root, breaking isolation. A foothold lets attackers achieve **container escape**, mount host devices, read secrets, alter configs, and control other workloads-impacting confidentiality, integrity, and availability via data theft, tampering, and service disruption.

## 推奨事項

Run containers without elevated rights (`privileged: false`) and as non-root (`user`). Apply **least privilege**: - Grant only required Linux capabilities via `capDrop`/`capAdd` - Prefer `readonlyRootFilesystem: true` - Isolate networks and separate duties - Monitor with logging to support defense in depth

## 修正手順


### CLI

```text
aws ecs deregister-task-definition --task-definition <task-family>:<revision>
```

### Native IaC

```yaml
# CloudFormation: ECS task definition with non-privileged container
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: <example_resource_name>
      ContainerDefinitions:
        - Name: <example_resource_name>
          Image: <image>
          Privileged: false  # Critical: ensures container is non-privileged to pass the check
```

### Terraform

```hcl
# ECS task definition with non-privileged container
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family                = "<example_resource_name>"
  container_definitions = jsonencode([
    {
      name       = "<example_resource_name>"
      image      = "<image>"
      privileged = false # Critical: ensures container is non-privileged to pass the check
    }
  ])
}
```

### Other

1. Open the Amazon ECS console and go to Task definitions
2. Select the failing task definition family and open the failing revision
3. Click Create new revision
4. Edit the affected container and uncheck Privileged (set it to false)
5. Click Create to register the new revision

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-nonprivileged.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-nonprivileged.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-4](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-4)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_security)

## 技術情報

- Source Metadata：[sources/aws/ecs_task_definitions_no_privileged_containers/metadata.json](../../sources/aws/ecs_task_definitions_no_privileged_containers/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_no_privileged_containers/check.py](../../sources/aws/ecs_task_definitions_no_privileged_containers/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_no_privileged_containers/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_no_privileged_containers/check.py`

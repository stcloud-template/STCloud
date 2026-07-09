# ECS task definition does not share the host's process namespace with its containers

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_task_definitions_host_namespace_not_shared` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | high |
| 类别 | container-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS Host Hardening Benchmarks, TTPs/Privilege Escalation, TTPs/Discovery |
| 资源类型 | AwsEcsTaskDefinition |
| 资源组 | container |

## 描述

**ECS task definitions** where `pidMode` is `host` are configured to share the host's **process namespace** with containers, rather than using isolated task or private namespaces.

## 风险

**Host PID sharing** lets containers view and interact with host processes, eroding isolation. - Confidentiality: process enumeration and metadata leakage - Integrity/Availability: signal or `ptrace` tampering, killing services Enables lateral movement and privilege escalation from a compromised container.

## 推荐措施

Prefer **isolated PID namespaces**: set `pidMode=task` or use the default per-container namespace. Avoid `host` PID sharing except for tightly controlled diagnostics. Apply **least privilege**: non-root users, minimal capabilities, read-only filesystems; and **defense in depth** with network and runtime controls.

## 修复步骤


### CLI

```text
aws ecs register-task-definition --family <example_resource_name> --pid-mode task --container-definitions '[{"name":"<container-name>","image":"<image>"}]'
```

### Native IaC

```yaml
# CloudFormation: ECS Task Definition without host PID namespace
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: <example_resource_name>
      ContainerDefinitions:
        - Name: <container-name>
          Image: <image>
      PidMode: task  # Critical: ensures containers use task PID namespace, not host
```

### Terraform

```hcl
# ECS Task Definition without host PID namespace
resource "aws_ecs_task_definition" "example" {
  family                = "<example_resource_name>"
  container_definitions = jsonencode([{ name = "<container-name>", image = "<image>" }])
  pid_mode              = "task"  # Critical: prevents sharing the host's process namespace
}
```

### Other

1. In the AWS Console, go to Amazon ECS > Task Definitions
2. Select the task definition and click Create new revision
3. Set Process namespace sharing (PID mode) to Task (not Host)
4. Save the new revision
5. (If the previous Host PID revision remains active) Select that revision and click Deregister

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-3](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-3)
- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-pid-mode-check.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-pid-mode-check.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/userguide/task_definition_parameters.html#container_definition_pid_mode](https://docs.aws.amazon.com/AmazonECS/latest/userguide/task_definition_parameters.html#container_definition_pid_mode)

## 技术信息

- Source Metadata：[sources/aws/ecs_task_definitions_host_namespace_not_shared/metadata.json](../../sources/aws/ecs_task_definitions_host_namespace_not_shared/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_host_namespace_not_shared/check.py](../../sources/aws/ecs_task_definitions_host_namespace_not_shared/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_host_namespace_not_shared/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_host_namespace_not_shared/check.py`

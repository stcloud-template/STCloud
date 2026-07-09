# Amazon ECS task definition does not use host network mode, or non-privileged containers specify a non-root user

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_task_definitions_host_networking_mode_users` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | high |
| 类别 | container-security, trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS Host Hardening Benchmarks, TTPs/Privilege Escalation, TTPs/Lateral Movement |
| 资源类型 | AwsEcsTaskDefinition |
| 资源组 | container |

## 描述

**Amazon ECS task definitions** in `host` network mode are assessed for containers where `privileged=false` and the container `user` is `root` or unset.

## 风险

Sharing the host network lets containers reach host interfaces directly. Running as **root** (or with no user set) increases the chance to bind low ports, sniff traffic, or impersonate services, and makes kernel flaws more exploitable-enabling data exfiltration, tampering, and outages, impacting **confidentiality**, **integrity**, and **availability**.

## 推荐措施

Prefer **`awsvpc`** for isolation. If `host` is required, enforce **least privilege**: - Run as a non-root `user` - Avoid `privileged` unless strictly justified - Limit capabilities and exposed ports Apply **defense in depth** with network segmentation and minimal IAM permissions.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: ECS task definition not using host network mode
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      NetworkMode: awsvpc  # CRITICAL: avoids host mode to pass the check
      ContainerDefinitions:
        - Name: <example_resource_name>
          Image: <image>
```

### Terraform

```hcl
# ECS task definition not using host network mode
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family                = "<example_resource_name>"
  network_mode          = "awsvpc"  # CRITICAL: avoids host mode to pass the check
  container_definitions = jsonencode([
    {
      name  = "<example_resource_name>"
      image = "nginx"
    }
  ])
}
```

### Other

1. Open the Amazon ECS console and go to Task definitions
2. Select the task definition and choose the latest revision
3. Click Create new revision
4. Set Network mode to awsvpc (not host)
5. Save the revision and, if used by a service, update the service to this new revision
6. If you must keep host mode: edit each non-privileged container and set User to a non-root value (e.g., 1000) and save a new revision

## 参考资料

- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-6](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-6)
- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-user-for-host-mode-check.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-user-for-host-mode-check.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html)

## 技术信息

- Source Metadata：[sources/aws/ecs_task_definitions_host_networking_mode_users/metadata.json](../../sources/aws/ecs_task_definitions_host_networking_mode_users/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_host_networking_mode_users/check.py](../../sources/aws/ecs_task_definitions_host_networking_mode_users/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_host_networking_mode_users/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_host_networking_mode_users/check.py`

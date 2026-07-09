# ECS task definition has logging configured for all containers

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_task_definitions_logging_enabled` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | high |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsEcsTaskDefinition |
| 资源组 | container |

## 描述

**Amazon ECS task definition** containers specify a **logging configuration** with a non-null `logDriver` for every container in the latest active revision.

## 风险

Absent container logs erode visibility, letting intrusions, data exfiltration, and configuration tampering go undetected. Missing audit trails weaken confidentiality and integrity, hinder forensics, and increase MTTR during outages, impacting availability and compliance evidence.

## 推荐措施

Implement centralized, tamper-resistant **container logging** for all tasks. Define a `logDriver` per container and ship logs to a managed destination with restricted access. Apply **least privilege**, encryption, and retention. Monitor and alert on anomalies. *If using external collectors, ensure equivalent coverage and durability.*

## 修复步骤


### CLI

```text
aws ecs register-task-definition --family <task-family> --container-definitions '[{"name":"<container-name>","image":"<image>","logConfiguration":{"logDriver":"awslogs","options":{"awslogs-group":"<log-group>","awslogs-region":"<region>"}}}]'
```

### Native IaC

```yaml
# CloudFormation: ECS task definition with logging enabled for the container
Resources:
  ExampleTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      ContainerDefinitions:
        - Name: "<example_resource_name>"
          Image: "<image>"
          LogConfiguration:                 # Critical: ensures container has logging configured
            LogDriver: awslogs              # Critical: non-null log driver passes the check
            Options:
              awslogs-group: "<log-group>" # Critical: CloudWatch Logs group
              awslogs-region: "<region>"
```

### Terraform

```hcl
# ECS task definition with logging enabled for the container
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family                = "<example_resource_name>"
  container_definitions = jsonencode([
    {
      name  = "<example_resource_name>"
      image = "<image>"
      logConfiguration = {                 # Critical: enables container logging
        logDriver = "awslogs"             # Critical: non-null log driver passes the check
        options = {
          awslogs-group  = "<log-group>"  # Critical: CloudWatch Logs group
          awslogs-region = "<region>"
        }
      }
    }
  ])
}
```

### Other

1. In the AWS Console, go to Amazon ECS > Task Definitions
2. Select your task definition and click Create new revision
3. For each container, open Edit and set Log configuration to awslogs
4. Set Log group to the desired CloudWatch Logs group and select the Region
5. Save and Create to register the new revision (ensure all containers have logging)

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-9](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-9)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config)
- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html)

## 技术信息

- Source Metadata：[sources/aws/ecs_task_definitions_logging_enabled/metadata.json](../../sources/aws/ecs_task_definitions_logging_enabled/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_logging_enabled/check.py](../../sources/aws/ecs_task_definitions_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_logging_enabled/check.py`

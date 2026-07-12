# ECS task definition has container logging in non-blocking mode

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecs_task_definitions_logging_block_mode` |
| クラウドプラットフォーム | AWS |
| サービス | ecs |
| 重大度 | low |
| カテゴリ | logging, resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Effects/Denial of Service |
| リソースタイプ | AwsEcsTaskDefinition |
| リソースグループ | container |

## 説明

**ECS task definition containers** use **non-blocking logging mode** via the `logConfiguration.mode` option on the latest active revision

## リスク

**Blocking log mode** can stall writes to stdout/stderr, making containers unresponsive, failing health checks, and causing task restarts or startup failures if log groups/streams can't be created. This reduces **availability** and may trigger cascading instability across dependent services.

## 推奨事項

Set `logConfiguration.mode` to `non-blocking` for all containers and size `max-buffer-size` to handle bursts. Keep log destinations in-Region to lower latency. Apply **defense in depth**: decouple application execution from logging, monitor log throughput, and design for backpressure so logging never blocks runtime.

## 修正手順


### CLI

```text
aws ecs register-task-definition --family <task-family> --container-definitions '[{"name":"<container-name>","image":"<image>","logConfiguration":{"logDriver":"awslogs","options":{"awslogs-group":"<log-group>","awslogs-region":"<region>","awslogs-stream-prefix":"ecs","mode":"non-blocking"}}}]'
```

### Native IaC

```yaml
# CloudFormation: ECS Task Definition with non-blocking container logging
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: <example_resource_name>
      ContainerDefinitions:
        - Name: <example_resource_name>
          Image: <image>
          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: <log-group>
              awslogs-region: <region>
              awslogs-stream-prefix: ecs
              mode: non-blocking  # CRITICAL: sets logging to non-blocking to pass the check
```

### Terraform

```hcl
# ECS Task Definition with container logging set to non-blocking
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family = "<example_resource_name>"

  # CRITICAL: "mode": "non-blocking" in logConfiguration options enforces non-blocking logging
  container_definitions = jsonencode([
    {
      name  = "<example_resource_name>"
      image = "<image>"
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "<log-group>"
          awslogs-region        = "<region>"
          awslogs-stream-prefix = "ecs"
          mode                  = "non-blocking" # CRITICAL: required to pass the check
        }
      }
    }
  ])
}
```

### Other

1. Open the AWS Console and go to ECS > Task Definitions
2. Select the failing task definition and choose Create new revision
3. Edit the affected container > Log configuration
4. Set Log driver to awslogs and add option: mode = non-blocking
5. Ensure awslogs-group, awslogs-region, and (if needed) awslogs-stream-prefix are set
6. Save and Create; the new revision will have non-blocking logging

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html)
- [https://www.amazonaws.cn/en/blog-selection/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/](https://www.amazonaws.cn/en/blog-selection/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config)

## 技術情報

- Source Metadata：[sources/aws/ecs_task_definitions_logging_block_mode/metadata.json](../../sources/aws/ecs_task_definitions_logging_block_mode/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_logging_block_mode/check.py](../../sources/aws/ecs_task_definitions_logging_block_mode/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_logging_block_mode/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_logging_block_mode/check.py`

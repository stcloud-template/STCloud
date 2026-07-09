# ECS Fargate service uses the latest Fargate platform version

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_service_fargate_latest_platform_version` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | medium |
| 类别 | vulnerabilities, container-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsEcsService |
| 资源组 | container |

## 描述

**ECS Fargate services** use the **latest Fargate platform version** via `platformVersion`=`LATEST` or an explicit value matching the current release for their `platformFamily` (Linux/Windows).

## 风险

Running on an outdated platform leaves known CVEs in the kernel/runtime unpatched, risking: - **Confidentiality**: data exposure via container escape - **Integrity**: privilege escalation and tampering - **Availability**: crashes/DoS and instability under load

## 推荐措施

- Prefer `platformVersion` `LATEST` to receive patches. - If pinning, monitor releases and redeploy quickly to the current version. - Automate updates with staged rollouts in CI/CD. - Apply **defense in depth** and **least privilege** to limit runtime exploit impact.

## 修复步骤


### CLI

```text
aws ecs update-service --cluster <cluster-name> --service <service-name> --platform-version LATEST
```

### Native IaC

```yaml
# CloudFormation: set ECS Fargate service to latest platform version
Resources:
  <example_resource_name>:
    Type: AWS::ECS::Service
    Properties:
      Cluster: <example_resource_id>
      TaskDefinition: <example_resource_name>
      LaunchType: FARGATE
      PlatformVersion: LATEST  # Critical: use the latest Fargate platform version
      NetworkConfiguration:
        AwsvpcConfiguration:
          Subnets:
            - <example_resource_id>
```

### Terraform

```hcl
# ECS Fargate service using the latest platform version
resource "aws_ecs_service" "<example_resource_name>" {
  name            = "<example_resource_name>"
  cluster         = "<example_resource_id>"
  task_definition = "<example_resource_name>"
  launch_type     = "FARGATE"
  platform_version = "LATEST" # Critical: ensures the latest Fargate platform version

  network_configuration {
    subnets = ["<example_resource_id>"]
  }
}
```

### Other

1. In the AWS Console, go to Amazon ECS
2. Open your cluster and select the service
3. Click Update
4. Set Platform version to LATEST
5. Click Update service (or Deploy) to apply

## 参考资料

- [https://servian.dev/setting-up-fargate-for-ecs-exec-8f5cc8d7d80e](https://servian.dev/setting-up-fargate-for-ecs-exec-8f5cc8d7d80e)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-fargate.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-fargate.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECS/platform-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECS/platform-version.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-fargate-latest-platform-version.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-fargate-latest-platform-version.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-10](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-10)

## 技术信息

- Source Metadata：[sources/aws/ecs_service_fargate_latest_platform_version/metadata.json](../../sources/aws/ecs_service_fargate_latest_platform_version/metadata.json)
- Source Code：[sources/aws/ecs_service_fargate_latest_platform_version/check.py](../../sources/aws/ecs_service_fargate_latest_platform_version/check.py)
- Source Metadata Path：`sources/aws/ecs_service_fargate_latest_platform_version/metadata.json`
- Source Code Path：`sources/aws/ecs_service_fargate_latest_platform_version/check.py`

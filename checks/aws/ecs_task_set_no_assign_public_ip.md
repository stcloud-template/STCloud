# ECS task set does not automatically assign a public IP address

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_task_set_no_assign_public_ip` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| 资源类型 | AwsEcsService |
| 资源组 | container |

## 描述

**ECS task sets** are assessed for **automatic public IP assignment** via `AssignPublicIP`. When set to `ENABLED`, tasks are given public addresses in their network configuration.

## 风险

Public IPs make tasks directly reachable from the Internet, enabling scanning, brute force, and exploit attempts. Impacts: **confidentiality** (data exposure), **integrity** (unauthorized actions), **availability** (DoS). Attackers can bypass internal controls and pivot for lateral movement.

## 推荐措施

Disable **automatic public IPs** on task sets. Use private subnets behind controlled entry points (load balancers, API gateways, or service discovery). Enforce **least privilege** security groups and **defense in depth**. Prefer private connectivity (VPC endpoints/VPN). *Expose only frontends, not tasks.*

## 修复步骤


### Native IaC

```yaml
# CloudFormation to ensure ECS Task Set does not auto-assign public IP
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskSet
    Properties:
      Cluster: "<example_resource_id>"
      Service: "<example_resource_id>"
      TaskDefinition: "<example_resource_id>"
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: DISABLED  # CRITICAL: disables automatic public IP assignment
          Subnets:
            - "<example_resource_id>"
```

### Terraform

```hcl
# ECS Task Set with public IP assignment disabled
resource "aws_ecs_task_set" "<example_resource_name>" {
  cluster         = "<example_resource_id>"
  service         = "<example_resource_id>"
  task_definition = "<example_resource_id>"

  network_configuration {
    subnets          = ["<example_resource_id>"]
    assign_public_ip = false  # CRITICAL: disables automatic public IP assignment
  }
}
```

### Other

1. In the AWS Console, go to ECS > Clusters > select your cluster
2. Open your Service and choose Update (or Edit)
3. In Networking, set Public IP assignment to Disabled
4. Save/Deploy the update to create a new deployment/task set
5. After the new task set is Primary and stable, delete the old task set that had Public IP enabled

## 参考资料

- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskSet.html](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskSet.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-16](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-16)

## 技术信息

- Source Metadata：[sources/aws/ecs_task_set_no_assign_public_ip/metadata.json](../../sources/aws/ecs_task_set_no_assign_public_ip/metadata.json)
- Source Code：[sources/aws/ecs_task_set_no_assign_public_ip/check.py](../../sources/aws/ecs_task_set_no_assign_public_ip/check.py)
- Source Metadata Path：`sources/aws/ecs_task_set_no_assign_public_ip/metadata.json`
- Source Code Path：`sources/aws/ecs_task_set_no_assign_public_ip/check.py`

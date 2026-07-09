# ECS service does not have automatic public IP assignment

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_service_no_assign_public_ip` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| 资源类型 | AwsEcsService |
| 资源组 | container |

## 描述

**ECS services** are assessed for automatic public IP assignment via the `assignPublicIp` setting in their network configuration. The finding indicates whether tasks launched by the service receive a public IP or are limited to private addressing.

## 风险

Automatic **public IPs** make tasks directly reachable from the Internet, enabling: - Port scanning and remote exploitation - Brute-force against admin endpoints - Data exfiltration via exposed APIs This jeopardizes **confidentiality**, **integrity**, and **availability**, and can facilitate lateral movement within the VPC.

## 推荐措施

Disable `assignPublicIp` to keep tasks private. Expose services through **load balancers** or **private endpoints**, restrict ingress with **least-privilege** security groups, and route egress via **NAT**. Apply **defense in depth** (WAF, TLS, monitoring) and segment networks to minimize blast radius.

## 修复步骤


### CLI

```text
aws ecs update-service --cluster <cluster-name> --service <service-name> --network-configuration "awsvpcConfiguration={subnets=[<subnet-id>],assignPublicIp=DISABLED}"
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECS::Service
    Properties:
      Cluster: <example_resource_id>
      TaskDefinition: <example_resource_id>
      NetworkConfiguration:
        AwsvpcConfiguration:
          Subnets:
            - <example_resource_id>
          AssignPublicIp: DISABLED  # Critical: disables automatic public IP assignment for the service
```

### Terraform

```hcl
resource "aws_ecs_service" "<example_resource_name>" {
  name           = "<example_resource_name>"
  cluster        = "<example_resource_id>"
  task_definition = "<example_resource_id>"

  network_configuration {
    subnets          = ["<example_resource_id>"]
    assign_public_ip = false  # Critical: disables automatic public IP assignment
  }
}
```

### Other

1. In the AWS Console, go to ECS > Clusters and open your cluster
2. Select the service and click Update
3. Under Networking (awsvpc), set Assign public IP to Disabled
4. Click Update service to apply

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-2](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-2)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

## 技术信息

- Source Metadata：[sources/aws/ecs_service_no_assign_public_ip/metadata.json](../../sources/aws/ecs_service_no_assign_public_ip/metadata.json)
- Source Code：[sources/aws/ecs_service_no_assign_public_ip/check.py](../../sources/aws/ecs_service_no_assign_public_ip/check.py)
- Source Metadata Path：`sources/aws/ecs_service_no_assign_public_ip/metadata.json`
- Source Code Path：`sources/aws/ecs_service_no_assign_public_ip/check.py`

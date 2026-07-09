# Auto Scaling group uses multiple Availability Zones

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `autoscaling_group_multiple_az` |
| 云平台 | AWS |
| 服务 | autoscaling |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsAutoScalingAutoScalingGroup |
| 资源组 | compute |

## 描述

**EC2 Auto Scaling groups** use **multiple Availability Zones** within a Region, with instances distributed across more than one zone rather than confined to a single zone.

## 风险

Relying on a single zone concentrates failure risk and harms **availability**. An AZ outage or capacity shortfall can block replacements and scaling, causing downtime, dropped traffic, and a wider blast radius. Recovery can lag because workloads can't shift to healthy zones.

## 推荐措施

Distribute each group across at least two **Availability Zones** to design for failure. Use a load balancer to spread traffic and health-based replacement to sustain capacity. Apply **resilience** and **fault isolation** principles so service continues during zonal degradation.

## 修复步骤


### CLI

```text
aws autoscaling update-auto-scaling-group --auto-scaling-group-name <example_resource_name> --vpc-zone-identifier "<subnet_id_az1>,<subnet_id_az2>"
```

### Native IaC

```yaml
# CloudFormation: ensure ASG spans multiple AZs
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: '1'
      MaxSize: '1'
      LaunchTemplate:
        LaunchTemplateId: <example_resource_id>
        Version: '$Latest'
      VPCZoneIdentifier:
        - <subnet_id_az1>
        - <subnet_id_az2>  # CRITICAL: Add a second subnet in a different AZ to ensure multiple AZs
```

### Terraform

```hcl
# Terraform: ensure ASG spans multiple AZs
resource "aws_autoscaling_group" "<example_resource_name>" {
  min_size = 1
  max_size = 1

  launch_template {
    id      = "<example_resource_id>"
    version = "$Latest"
  }

  vpc_zone_identifier = [
    "<subnet_id_az1>",
    "<subnet_id_az2>" # CRITICAL: two subnets in different AZs to pass the check
  ]
}
```

### Other

1. In the AWS Console, go to EC2 > Auto Scaling Groups
2. Select the group and open the Details tab
3. Click Network > Edit
4. In Subnets, add one more subnet from a different Availability Zone
5. Click Update to save

## 参考资料

- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-availability-zone-balanced.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-availability-zone-balanced.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/multiple-availability-zones.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/multiple-availability-zones.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/disaster-recovery-resiliency.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/disaster-recovery-resiliency.html)

## 技术信息

- Source Metadata：[sources/aws/autoscaling_group_multiple_az/metadata.json](../../sources/aws/autoscaling_group_multiple_az/metadata.json)
- Source Code：[sources/aws/autoscaling_group_multiple_az/check.py](../../sources/aws/autoscaling_group_multiple_az/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_multiple_az/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_multiple_az/check.py`

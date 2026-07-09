# Amazon EC2 Auto Scaling group has Capacity Rebalancing enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `autoscaling_group_capacity_rebalance_enabled` |
| 云平台 | AWS |
| 服务 | autoscaling |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsAutoScalingAutoScalingGroup |
| 资源组 | compute |

## 描述

**EC2 Auto Scaling groups** use **Capacity Rebalancing** to act on EC2 `rebalance` recommendations by launching replacement Spot instances and terminating at-risk ones after they are healthy. *Assesses whether this proactive replacement behavior is enabled.*

## 风险

Without **Capacity Rebalancing**, Spot interruptions can drop targets and reduce capacity, causing timeouts, 5xx spikes, and backlog growth. The two-minute notice is often insufficient, reducing service **availability** and increasing the chance of cascading failures and slow recovery.

## 推荐措施

Enable **Capacity Rebalancing** for ASGs that use Spot. Apply resilience practices: - Prefer `price-capacity-optimized` allocation - Keep headroom below `MaxSize` - Use lifecycle hooks to drain/deregister - Design stateless, interruption-tolerant workloads (least privilege and defense-in-depth for dependencies)

## 修复步骤


### CLI

```text
aws autoscaling update-auto-scaling-group --auto-scaling-group-name <example_resource_name> --capacity-rebalance
```

### Native IaC

```yaml
# CloudFormation: Enable Capacity Rebalancing on an Auto Scaling group
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: "1"
      MaxSize: "1"
      AvailabilityZones: ["<example_az>"]
      LaunchTemplate:
        LaunchTemplateName: <example_resource_name>
        Version: "$Default"
      CapacityRebalance: true  # CRITICAL: Enables proactive replacement of at-risk Spot instances
```

### Terraform

```hcl
# Terraform: Enable Capacity Rebalancing on an Auto Scaling group
resource "aws_autoscaling_group" "<example_resource_name>" {
  name               = "<example_resource_name>"
  min_size           = 1
  max_size           = 1
  desired_capacity   = 1
  availability_zones = ["<example_az>"]

  launch_template {
    id    = "<example_resource_id>"
    version = "$Latest"
  }

  capacity_rebalance = true  # CRITICAL: Turns on Capacity Rebalancing
}
```

### Other

1. In the AWS Console, go to EC2 > Auto Scaling Groups
2. Select <example_resource_name> and open the Details tab
3. Click Allocation strategies > Edit, check Capacity rebalancing
4. Click Update/Save

## 参考资料

- [https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ec2-auto-scaling-group-capacity-rebalance-enabled](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-ec2-auto-scaling-group-capacity-rebalance-enabled)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/enable-capacity-rebalancing.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/enable-capacity-rebalancing.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-capacity-rebalancing-console-cli.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-capacity-rebalancing-console-cli.html)

## 技术信息

- Source Metadata：[sources/aws/autoscaling_group_capacity_rebalance_enabled/metadata.json](../../sources/aws/autoscaling_group_capacity_rebalance_enabled/metadata.json)
- Source Code：[sources/aws/autoscaling_group_capacity_rebalance_enabled/check.py](../../sources/aws/autoscaling_group_capacity_rebalance_enabled/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_capacity_rebalance_enabled/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_capacity_rebalance_enabled/check.py`

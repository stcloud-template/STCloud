# Auto Scaling group spans multiple Availability Zones and has multiple instance types per Availability Zone

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `autoscaling_group_multiple_instance_types` |
| 云平台 | AWS |
| 服务 | autoscaling |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsAutoScalingAutoScalingGroup |
| 资源组 | compute |

## 描述

**EC2 Auto Scaling groups** are evaluated for using **multiple instance types** in each **Availability Zone** and spanning more than one AZ. Groups are identified when every AZ defines at least two instance types; groups with any AZ using a single or no type, or confined to one AZ, are noted.

## 风险

Limited to one instance type per AZ or a single AZ, scaling can stall during **capacity shortages**, hindering **failover** and degrading **availability** (timeouts, backlog growth). Costs may spike if only expensive capacity is available. Reduced diversity increases the likelihood of prolonged outages during zonal or market disruptions.

## 推荐措施

Adopt a **mixed instances** strategy for resilience: - Use diverse instance families and sizes per AZ - Distribute capacity across multiple AZs - Favor allocation approaches that tolerate spot/on-demand scarcity Apply **redundancy** and **fault tolerance** principles and validate scaling policies to avoid single points of capacity failure.

## 修复步骤


### CLI

```text
aws autoscaling update-auto-scaling-group --auto-scaling-group-name <example_resource_name> --mixed-instances-policy '{"LaunchTemplate":{"LaunchTemplateSpecification":{"LaunchTemplateName":"<example_resource_name>","Version":"$Latest"},"Overrides":[{"InstanceType":"<INSTANCE_TYPE_1>"},{"InstanceType":"<INSTANCE_TYPE_2>"}]}}' --vpc-zone-identifier "<subnet_id_1>,<subnet_id_2>"
```

### Native IaC

```yaml
# CloudFormation: Ensure ASG uses multiple instance types across multiple AZs
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: "1"
      MaxSize: "1"
      VPCZoneIdentifier:
        - <subnet_id_1>  # CRITICAL: Use subnets in different AZs to span multiple AZs
        - <subnet_id_2>  # CRITICAL: Ensures at least two Availability Zones
      MixedInstancesPolicy:
        LaunchTemplate:
          LaunchTemplateSpecification:
            LaunchTemplateName: <example_resource_name>
            Version: $Latest
          Overrides:
            - InstanceType: <INSTANCE_TYPE_1>  # CRITICAL: Multiple instance types per AZ
            - InstanceType: <INSTANCE_TYPE_2>  # CRITICAL: Multiple instance types per AZ
```

### Terraform

```hcl
# Terraform: Ensure ASG uses multiple instance types across multiple AZs
resource "aws_autoscaling_group" "<example_resource_name>" {
  name               = "<example_resource_name>"
  min_size           = 1
  max_size           = 1
  vpc_zone_identifier = ["<subnet_id_1>", "<subnet_id_2>"] # CRITICAL: Subnets in different AZs

  mixed_instances_policy {
    launch_template {
      launch_template_specification {
        launch_template_name = "<example_resource_name>"
        version              = "$Latest"
      }
      override { instance_type = "<INSTANCE_TYPE_1>" } # CRITICAL: Multiple instance types per AZ
      override { instance_type = "<INSTANCE_TYPE_2>" } # CRITICAL: Multiple instance types per AZ
    }
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Auto Scaling Groups and select <example_resource_name>
2. Click Edit
3. Under Network, add at least two subnets in different Availability Zones
4. Under Launch options, choose Mixed instance types
5. Select your Launch template and set Version to $Latest
6. Add at least two Instance types in Overrides
7. Click Update to save

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-multiple-instance-type-az.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-multiple-instance-type-az.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-6](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-6)

## 技术信息

- Source Metadata：[sources/aws/autoscaling_group_multiple_instance_types/metadata.json](../../sources/aws/autoscaling_group_multiple_instance_types/metadata.json)
- Source Code：[sources/aws/autoscaling_group_multiple_instance_types/check.py](../../sources/aws/autoscaling_group_multiple_instance_types/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_multiple_instance_types/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_multiple_instance_types/check.py`

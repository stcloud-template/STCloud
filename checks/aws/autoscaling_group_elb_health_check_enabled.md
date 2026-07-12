# Auto Scaling group associated with a load balancer has ELB health checks enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `autoscaling_group_elb_health_check_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | autoscaling |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsAutoScalingAutoScalingGroup |
| リソースグループ | compute |

## 説明

EC2 Auto Scaling groups attached to a load balancer are evaluated for **ELB-based health checks** that use the load balancer's target health instead of instance-only checks.

## リスク

Without **ELB health checks**, the group may keep instances that fail load balancer probes, causing: - Reduced **availability** from routing to bad targets - Higher error rates impacting transaction **integrity** - Inefficient scaling and increased **costs**

## 推奨事項

Enable **ELB health checks** for Auto Scaling groups behind load balancers to reflect real client reachability. Apply **high availability** and **defense in depth** by: - Using application-appropriate LB probes - Tuning grace and threshold settings to avoid flapping - Monitoring health metrics and alerts

## 修正手順


### CLI

```text
aws autoscaling update-auto-scaling-group --auto-scaling-group-name <auto-scaling-group-name> --health-check-type ELB
```

### Native IaC

```yaml
# CloudFormation: Enable ELB health checks for the Auto Scaling group
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      HealthCheckType: ELB  # Remediation: use ELB health checks so the ASG evaluates instance health via the load balancer
```

### Terraform

```hcl
# Enable ELB health checks on the Auto Scaling group
resource "aws_autoscaling_group" "<example_resource_name>" {
  health_check_type = "ELB"  # Remediation: ensures ASG uses load balancer health status
}
```

### Other

1. In AWS Console, go to EC2 > Auto Scaling Groups
2. Select the Auto Scaling group
3. On the Details tab, click Edit under Health checks
4. Under Additional health check types, select Elastic Load Balancing (ELB)
5. Click Update/Save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-1](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-1)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-health-check.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-health-check.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html#as-add-elb-healthcheck-console](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html#as-add-elb-healthcheck-console)

## 技術情報

- Source Metadata：[sources/aws/autoscaling_group_elb_health_check_enabled/metadata.json](../../sources/aws/autoscaling_group_elb_health_check_enabled/metadata.json)
- Source Code：[sources/aws/autoscaling_group_elb_health_check_enabled/check.py](../../sources/aws/autoscaling_group_elb_health_check_enabled/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_elb_health_check_enabled/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_elb_health_check_enabled/check.py`

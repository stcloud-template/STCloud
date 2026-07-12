# Auto Scaling group associated launch configuration does not assign a public IP address

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `autoscaling_group_launch_configuration_no_public_ip` |
| クラウドプラットフォーム | AWS |
| サービス | autoscaling |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsAutoScalingAutoScalingGroup |
| リソースグループ | compute |

## 説明

**Amazon EC2 Auto Scaling groups** are evaluated to determine whether their associated **launch configuration** assigns **public IP addresses** to instances (e.g., `AssociatePublicIpAddress=true`).

## リスク

**Publicly addressable instances** are reachable from the Internet, enabling reconnaissance, brute-force, and exploitation of exposed services. Compromise can lead to remote access, **data exfiltration**, and **lateral movement**, impacting **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Place instances in private subnets and disable public addressing (`AssociatePublicIpAddress=false`). Publish services via **load balancers** or **private endpoints**, enforce **least privilege** security groups, and use **SSM**, VPN, or a hardened bastion for admin access. Prefer **launch templates** to standardize network controls.

## 修正手順


### Native IaC

```yaml
# CloudFormation Launch Configuration without public IPs
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId: <example_ami_id>
      InstanceType: <example_instance_type>
      AssociatePublicIpAddress: false  # Critical: disables assigning public IPs to instances
```

### Terraform

```hcl
# Launch Configuration without public IPs
resource "aws_launch_configuration" "<example_resource_name>" {
  image_id                    = "<example_ami_id>"
  instance_type               = "<example_instance_type>"
  associate_public_ip_address = false  # Critical: disables assigning public IPs
}
```

### Other

1. In the AWS console, go to EC2 > Auto Scaling > Launch configurations and click Create launch configuration
2. Use the same AMI and instance type as the current group; under Advanced details set IP address type to Do not assign a public IP address
3. Create the launch configuration
4. Go to EC2 > Auto Scaling Groups, select your group, click Edit next to Launch configuration, choose the new configuration, and click Update

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-5](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-5)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-configuration.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-configuration.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html)

## 技術情報

- Source Metadata：[sources/aws/autoscaling_group_launch_configuration_no_public_ip/metadata.json](../../sources/aws/autoscaling_group_launch_configuration_no_public_ip/metadata.json)
- Source Code：[sources/aws/autoscaling_group_launch_configuration_no_public_ip/check.py](../../sources/aws/autoscaling_group_launch_configuration_no_public_ip/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_launch_configuration_no_public_ip/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_launch_configuration_no_public_ip/check.py`

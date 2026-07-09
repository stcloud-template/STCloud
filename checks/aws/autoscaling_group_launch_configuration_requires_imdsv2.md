# Auto Scaling group enforces IMDSv2 or disables the instance metadata service

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `autoscaling_group_launch_configuration_requires_imdsv2` |
| 云平台 | AWS |
| 服务 | autoscaling |
| 严重等级 | high |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Credential Access, Effects/Data Exposure |
| 资源类型 | AwsAutoScalingAutoScalingGroup |
| 资源组 | compute |

## 描述

Amazon EC2 Auto Scaling launch configurations are evaluated for **Instance Metadata Service** settings. Instances should have the metadata endpoint `enabled` with `http_tokens=required` (enforcing **IMDSv2**), or have the metadata service `disabled`. Allowing `http_tokens=optional` or omitting the version leaves legacy access enabled.

## 风险

Without enforced **IMDSv2**, **SSRF** and local escape paths can access **IAM role credentials**, enabling unauthorized API calls. Attackers could: - Exfiltrate data with stolen tokens - Move laterally and modify resources, degrading confidentiality and integrity

## 推荐措施

Require **IMDSv2** for Auto Scaling-launched instances by setting `http_tokens=required` when metadata is `enabled`. *If metadata is not needed*, disable it. Apply **least privilege** to instance roles, set IMDSv2 as an account default, and use **defense in depth** (egress filtering, SSRF protections) to limit exposure.

## 修复步骤


### CLI

```text
aws autoscaling create-launch-configuration --launch-configuration-name <new-launch-config> --image-id <AMI_ID> --instance-type <INSTANCE_TYPE> --metadata-options 'HttpTokens=required,HttpEndpoint=enabled'
```

### Native IaC

```yaml
# CloudFormation: ASG launch configuration enforces IMDSv2
Resources:
  LaunchConfig:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId: <example_ami_id>
      InstanceType: <example_instance_type>
      MetadataOptions:
        HttpTokens: required     # critical: require IMDSv2 tokens (disables IMDSv1)
        HttpEndpoint: enabled    # critical: keep IMDS enabled while enforcing v2

  AutoScalingGroup:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      LaunchConfigurationName: !Ref LaunchConfig
      MinSize: 1
      MaxSize: 1
      VPCZoneIdentifier:
        - <example_subnet_id>
```

### Terraform

```hcl
# ASG launch configuration enforces IMDSv2
resource "aws_launch_configuration" "example" {
  image_id      = "<example_ami_id>"
  instance_type = "<example_instance_type>"

  metadata_options {
    http_tokens   = "required"  # critical: require IMDSv2 tokens (blocks IMDSv1)
    http_endpoint = "enabled"   # critical: IMDS enabled while enforcing v2
  }
}

resource "aws_autoscaling_group" "example" {
  launch_configuration = aws_launch_configuration.example.name
  min_size             = 1
  max_size             = 1
  vpc_zone_identifier  = ["<example_subnet_id>"]
}
```

### Other

1. In the AWS Console, go to EC2 > Auto Scaling > Launch configurations
2. Click Create launch configuration and choose the same AMI and instance type used by the group
3. Expand Advanced details and set Metadata options to: Metadata accessible = Enabled, Metadata version = V2 only (token required)
4. Create the launch configuration
5. Go to EC2 > Auto Scaling > Auto Scaling groups, select the group, click Edit
6. Under Launch configuration, select the new launch configuration and Save
7. (Alternative) To disable IMDS entirely: when creating the launch configuration, set Metadata accessible = Disabled

## 参考资料

- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-3](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-3)
- [https://aws.plainenglish.io/dont-let-metadata-leak-why-imdsv2-is-a-must-and-how-to-migrate-a88e1e285394](https://aws.plainenglish.io/dont-let-metadata-leak-why-imdsv2-is-a-must-and-how-to-migrate-a88e1e285394)

## 技术信息

- Source Metadata：[sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/metadata.json](../../sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/metadata.json)
- Source Code：[sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/check.py](../../sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/check.py)
- Source Metadata Path：`sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/metadata.json`
- Source Code Path：`sources/aws/autoscaling_group_launch_configuration_requires_imdsv2/check.py`

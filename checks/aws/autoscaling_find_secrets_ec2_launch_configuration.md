# [DEPRECATED] EC2 Auto Scaling launch configuration user data contains no secrets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `autoscaling_find_secrets_ec2_launch_configuration` |
| 云平台 | AWS |
| 服务 | autoscaling |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Effects/Data Exposure |
| 资源类型 | AwsAutoScalingLaunchConfiguration |
| 资源组 | compute |

## 描述

[DEPRECATED] EC2 Auto Scaling launch configurations are analyzed for **secrets** embedded in `User Data`, such as passwords, tokens, or API keys in bootstrapping scripts.

## 风险

Secrets in `User Data` erode **confidentiality** and **integrity**: - Instance users or processes can read or log them - Exposed keys enable unauthorized API calls, data exfiltration, and lateral movement - Credential reuse increases blast radius across accounts and services

## 推荐措施

Never place secrets in `User Data`. - Use a managed secret store with an instance role to fetch at runtime - Enforce **least privilege**, rotate secrets, and avoid writing secrets to logs - Prefer short-lived, scoped credentials and layer controls for **defense in depth**

## 修复步骤


### Native IaC

```yaml
# CloudFormation Launch Configuration without secrets in UserData
Resources:
  <example_resource_name>:
    Type: AWS::AutoScaling::LaunchConfiguration
    Properties:
      ImageId: <AMI_ID>
      InstanceType: <INSTANCE_TYPE>
      UserData: ''  # Critical: empty user data ensures no secrets are present
```

### Terraform

```hcl
# Launch configuration with no secrets in user data
resource "aws_launch_configuration" "<example_resource_name>" {
  image_id      = "<AMI_ID>"
  instance_type = "<INSTANCE_TYPE>"
  user_data     = "" # Critical: empty user data ensures no secrets are present
}
```

### Other

1. In the AWS Console, go to EC2 > Launch configurations and click Create launch configuration
2. Reuse the same AMI and instance type; leave User data empty
3. Go to EC2 > Auto Scaling groups, select the group using the failing launch configuration, click Edit
4. Under Launch options, select the new launch configuration and Save
5. After the ASG is updated, delete the old launch configuration

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 技术信息

- Source Metadata：[sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json](../../sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json)
- Source Code：[sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py](../../sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py)
- Source Metadata Path：`sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json`
- Source Code Path：`sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py`

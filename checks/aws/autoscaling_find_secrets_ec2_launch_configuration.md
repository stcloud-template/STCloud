# [DEPRECATED] EC2 Auto Scaling launch configuration user data contains no secrets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `autoscaling_find_secrets_ec2_launch_configuration` |
| クラウドプラットフォーム | AWS |
| サービス | autoscaling |
| 重大度 | critical |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Effects/Data Exposure |
| リソースタイプ | AwsAutoScalingLaunchConfiguration |
| リソースグループ | compute |

## 説明

[DEPRECATED] EC2 Auto Scaling launch configurations are analyzed for **secrets** embedded in `User Data`, such as passwords, tokens, or API keys in bootstrapping scripts.

## リスク

Secrets in `User Data` erode **confidentiality** and **integrity**: - Instance users or processes can read or log them - Exposed keys enable unauthorized API calls, data exfiltration, and lateral movement - Credential reuse increases blast radius across accounts and services

## 推奨事項

Never place secrets in `User Data`. - Use a managed secret store with an instance role to fetch at runtime - Enforce **least privilege**, rotate secrets, and avoid writing secrets to logs - Prefer short-lived, scoped credentials and layer controls for **defense in depth**

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 技術情報

- Source Metadata：[sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json](../../sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json)
- Source Code：[sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py](../../sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py)
- Source Metadata Path：`sources/aws/autoscaling_find_secrets_ec2_launch_configuration/metadata.json`
- Source Code Path：`sources/aws/autoscaling_find_secrets_ec2_launch_configuration/check.py`

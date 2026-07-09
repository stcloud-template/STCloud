# AWS Config recorder uses the AWSServiceRoleForConfig service-linked role

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `config_recorder_using_aws_service_role` |
| 云平台 | AWS |
| 服务 | config |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | monitoring |

## 描述

**AWS Config recorders** are evaluated for use of the service‑linked IAM role `AWSServiceRoleForConfig` linked to `config.amazonaws.com` rather than a custom role. The evaluation inspects active recorders and their role ARN to confirm the AWS‑managed service‑linked role is in use.

## 风险

Using a custom or incorrect role can break recording or create blind spots, undermining the **integrity** and **availability** of configuration history. Over‑privileged roles weaken **least privilege**, increasing risk of unauthorized access, stealthy changes, and delayed incident response.

## 推荐措施

Use the AWS‑managed service‑linked role `AWSServiceRoleForConfig` for all recorders to enforce **least privilege** and consistent trust. Avoid custom roles; restrict who can modify the recorder or role; monitor for drift and ensure recording remains enabled as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws configservice put-configuration-recorder --configuration-recorder name=<RECORDER_NAME>,roleARN=arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig
```

### Native IaC

```yaml
Resources:
  example_resource:
    Type: AWS::Config::ConfigurationRecorder
    Properties:
      Name: example_resource
      RoleARN: arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig  # This line fixes the security issue
```

### Terraform

```hcl
resource "aws_config_configuration_recorder" "example_resource" {
  name     = "example_resource"
  role_arn = "arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"  # This line fixes the security issue
}
```

### Other

1. Open the AWS Console and go to AWS Config
2. Choose Settings (or Recording) and click Edit
3. For IAM role, select Use service-linked role (AWSServiceRoleForConfig)
4. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1](https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1)
- [https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html](https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html)

## 技术信息

- Source Metadata：[sources/aws/config_recorder_using_aws_service_role/metadata.json](../../sources/aws/config_recorder_using_aws_service_role/metadata.json)
- Source Code：[sources/aws/config_recorder_using_aws_service_role/check.py](../../sources/aws/config_recorder_using_aws_service_role/check.py)
- Source Metadata Path：`sources/aws/config_recorder_using_aws_service_role/metadata.json`
- Source Code Path：`sources/aws/config_recorder_using_aws_service_role/check.py`

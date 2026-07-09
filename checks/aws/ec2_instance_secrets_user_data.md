# Find secrets in EC2 User Data.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_secrets_user_data` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | IAM |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Find secrets in EC2 User Data.

## 风险

Secrets hardcoded into instance user data can be used by malware and bad actors to gain lateral access to other services.

## 推荐措施

Implement automated detective control (e.g. using tools like ST Cloud) to scan accounts for passwords and secrets. Use secrets manager service to store and retrieve passwords and secrets.

- 推荐链接：[https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html)

## 修复步骤


### CLI

```text
aws ec2 describe-instance-attribute --attribute userData --region <REGION> --instance-id <INSTANCE_ID> --query UserData.Value --output text > encodeddata; base64 --decode encodeddata
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#cloudformation](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#terraform](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1](https://docs.ST Cloud.com/checks/aws/secrets-policies/bc_aws_secrets_1)

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_secrets_user_data/metadata.json](../../sources/aws/ec2_instance_secrets_user_data/metadata.json)
- Source Code：[sources/aws/ec2_instance_secrets_user_data/check.py](../../sources/aws/ec2_instance_secrets_user_data/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_secrets_user_data/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_secrets_user_data/check.py`

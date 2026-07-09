# AWS Secrets Manager secret is rotated within the configured maximum number of days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `secretsmanager_secret_rotated_periodically` |
| 云平台 | AWS |
| 服务 | secretsmanager |
| 严重等级 | medium |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsSecretsManagerSecret |
| 资源组 | security |

## 描述

**AWS Secrets Manager secrets** are evaluated for **periodic rotation** within a configured window (default `90` days). Secrets with no recorded rotation, or with rotation older than the allowed window, are identified for review.

## 风险

**Long-lived or never-rotated secrets** widen the attack window. Leaked or brute-forced credentials stay valid, enabling unauthorized access to databases and APIs, **data exfiltration**, and unauthorized changes-compromising **confidentiality** and **integrity**.

## 推荐措施

Enable **automatic rotation** for all secrets with intervals aligned to sensitivity (**`90` days or more frequent). Ensure apps retrieve secrets at runtime. Apply **least privilege** to rotation roles and KMS keys, use **separation of duties**, and monitor rotation health with alerts. Avoid hard-coded credentials and retire unused secrets.

## 修复步骤


### CLI

```text
aws secretsmanager rotate-secret --secret-id <secret-id>
```

### Native IaC

```yaml
# CloudFormation: enable rotation and rotate now
Resources:
  <example_resource_name>:
    Type: AWS::SecretsManager::RotationSchedule
    Properties:
      SecretId: <example_resource_id>  # CRITICAL: target secret to rotate
      RotationLambdaARN: <example_resource_id>  # CRITICAL: Lambda ARN used to perform rotation
      ScheduleExpression: rate(30 days)  # CRITICAL: ensures rotation occurs within max allowed days
      RotateImmediatelyOnUpdate: true  # CRITICAL: triggers an immediate rotation to pass the check
```

### Terraform

```hcl
# Enable rotation for the secret
resource "aws_secretsmanager_secret_rotation" "<example_resource_name>" {
  secret_id          = "<example_resource_id>"  # CRITICAL: target secret
  rotation_lambda_arn = "<example_resource_id>" # CRITICAL: Lambda ARN used to rotate

  rotation_rules {
    automatically_after_days = 30            # CRITICAL: rotate within allowed days
  }
}
```

### Other

1. Open the AWS Console > Secrets Manager
2. Select the secret
3. If Rotation status is Enabled: click Rotate secret immediately
4. If Rotation is Disabled: click Edit rotation, turn on Automatic rotation, choose the rotation Lambda function, Save, then click Rotate secret immediately

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.html)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

## 技术信息

- Source Metadata：[sources/aws/secretsmanager_secret_rotated_periodically/metadata.json](../../sources/aws/secretsmanager_secret_rotated_periodically/metadata.json)
- Source Code：[sources/aws/secretsmanager_secret_rotated_periodically/check.py](../../sources/aws/secretsmanager_secret_rotated_periodically/check.py)
- Source Metadata Path：`sources/aws/secretsmanager_secret_rotated_periodically/metadata.json`
- Source Code Path：`sources/aws/secretsmanager_secret_rotated_periodically/check.py`

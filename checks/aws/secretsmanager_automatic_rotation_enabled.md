# Secrets Manager secret has rotation enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `secretsmanager_automatic_rotation_enabled` |
| 云平台 | AWS |
| 服务 | secretsmanager |
| 严重等级 | high |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA) |
| 资源类型 | AwsSecretsManagerSecret |
| 资源组 | security |

## 描述

**AWS Secrets Manager secrets** are evaluated for **automatic rotation**; the check determines if a rotation schedule is enabled for each secret

## 风险

Absent rotation, **long-lived secrets** widen the attack window: - Valid after leakage in code, images, or logs - Enable **unauthorized access** and **lateral movement** - Complicate incident response and recovery This impacts **confidentiality** and **integrity**, and can threaten **availability** if revocation lags.

## 推荐措施

Enable **automatic rotation** for secrets and set schedules based on sensitivity (e.g., `30-90 days`). Enforce **least privilege** for accessing and rotating secrets and apply **separation of duties**. Monitor rotation health. Avoid hardcoded credentials; retrieve secrets at runtime and support versioned updates.

## 修复步骤


### CLI

```text
aws secretsmanager rotate-secret --secret-id <example_resource_id> --rotation-lambda-arn <example_resource_id> --rotation-rules AutomaticallyAfterDays=30
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::SecretsManager::RotationSchedule
    Properties:
      SecretId: <example_resource_id>
      RotationLambdaARN: <example_resource_id>
      RotationRules:
        AutomaticallyAfterDays: 30  # Critical: enables rotation on a 30-day schedule
```

### Terraform

```hcl
resource "aws_secretsmanager_secret_rotation" "<example_resource_name>" {
  secret_id          = "<example_resource_id>"
  rotation_lambda_arn = "<example_resource_id>"
  rotation_rules {
    automatically_after_days = 30  # Critical: enables rotation schedule
  }
}
```

### Other

1. Open AWS Console > Secrets Manager
2. Select the secret
3. Click Rotation > Enable automatic rotation
4. Choose the rotation Lambda function
5. Set rotation interval to 30 days
6. Save

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets_strategies.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets_strategies.html)

## 技术信息

- Source Metadata：[sources/aws/secretsmanager_automatic_rotation_enabled/metadata.json](../../sources/aws/secretsmanager_automatic_rotation_enabled/metadata.json)
- Source Code：[sources/aws/secretsmanager_automatic_rotation_enabled/check.py](../../sources/aws/secretsmanager_automatic_rotation_enabled/check.py)
- Source Metadata Path：`sources/aws/secretsmanager_automatic_rotation_enabled/metadata.json`
- Source Code Path：`sources/aws/secretsmanager_automatic_rotation_enabled/check.py`

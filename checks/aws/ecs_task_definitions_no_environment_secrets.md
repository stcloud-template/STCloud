# ECS task definition has no secrets in environment variables

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecs_task_definitions_no_environment_secrets` |
| クラウドプラットフォーム | AWS |
| サービス | ecs |
| 重大度 | critical |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Sensitive Data Identifications/Passwords, TTPs/Credential Access |
| リソースタイプ | AwsEcsTaskDefinition |
| リソースグループ | container |

## 説明

**ECS task definitions** are analyzed for **plaintext secrets** placed in container `environment` variables. It identifies values that resemble credentials (keys, tokens, passwords) within container definitions.

## リスク

Exposed secrets in env vars undermine confidentiality via logs, task metadata, and introspection. With container or read-only API access, attackers can reuse credentials to read databases, modify records (integrity), pivot to other services, and trigger outages or unauthorized costs (availability).

## 推奨事項

Store secrets in **AWS Secrets Manager** or **SSM Parameter Store** and inject them at runtime instead of plaintext env vars. Apply **least privilege** via task roles, enable regular **rotation**, avoid logging secret values, and prefer **ephemeral credentials** for downstream services.

## 修正手順


### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: <example_resource_name>
      ContainerDefinitions:
        - Name: app
          Image: <image>
          Secrets:                      # Critical: use Secrets instead of plaintext env vars
            - Name: DB_PASSWORD         # Critical: inject secret at runtime
              ValueFrom: <secret_arn_or_parameter_arn>  # Critical: reference Secrets Manager/SSM parameter
```

### Terraform

```hcl
resource "aws_ecs_task_definition" "<example_resource_name>" {
  family                = "<example_resource_name>"
  # Critical: define container secrets instead of plaintext env vars
  container_definitions = jsonencode([
    {
      name    = "app"
      image   = "<image>"
      secrets = [
        { name = "DB_PASSWORD", valueFrom = "<secret_arn_or_parameter_arn>" } # Critical: inject secret at runtime
      ]
    }
  ])
}
```

### Other

1. In the AWS Console, go to ECS > Task Definitions and open your task definition
2. Create a new revision
3. For each container, remove any sensitive values from Environment variables
4. Under Environment variables, add a new entry in the Secrets section with Name (e.g., DB_PASSWORD) and ValueFrom pointing to your Secrets Manager/SSM parameter
5. Save to create the new revision
6. If using a service, update the service to use the new task definition revision and deploy

## 参考資料

- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html)

## 技術情報

- Source Metadata：[sources/aws/ecs_task_definitions_no_environment_secrets/metadata.json](../../sources/aws/ecs_task_definitions_no_environment_secrets/metadata.json)
- Source Code：[sources/aws/ecs_task_definitions_no_environment_secrets/check.py](../../sources/aws/ecs_task_definitions_no_environment_secrets/check.py)
- Source Metadata Path：`sources/aws/ecs_task_definitions_no_environment_secrets/metadata.json`
- Source Code Path：`sources/aws/ecs_task_definitions_no_environment_secrets/check.py`

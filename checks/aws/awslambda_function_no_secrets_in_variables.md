# Lambda function environment variables do not contain secrets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `awslambda_function_no_secrets_in_variables` |
| 云平台 | AWS |
| 服务 | awslambda |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Effects/Data Exposure |
| 资源类型 | AwsLambdaFunction |
| 资源组 | serverless |

## 描述

AWS Lambda function environment variables are analyzed for content that resembles **secrets** (API keys, tokens, passwords). Pattern-based detection highlights potential hardcoded credentials present in the function's environment.

## 风险

Secrets in Lambda environment variables weaken **confidentiality**: users with config read access, runtime introspection, or logs may obtain them. Exposure can grant access to downstream systems, enable **lateral movement**, and allow tampering, impacting **integrity** and **availability**.

## 推荐措施

Do not store secrets in environment variables or code. Use **AWS Secrets Manager** or **Parameter Store** with encryption, fetch at runtime using **least privilege** IAM, and prefer short-lived creds via **IAM roles**. Rotate keys, limit configuration read access, and apply **defense in depth** with logging and alerts for secret access.

## 修复步骤


### CLI

```text
aws lambda update-function-configuration --region <REGION> --function-name <FUNCTION_NAME> --environment "Variables={}"
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Lambda::Function
    Properties:
      Environment:
        Variables: {}  # CRITICAL: clears environment variables to ensure no secrets are stored
```

### Terraform

```hcl
resource "aws_lambda_function" "<example_resource_name>" {
  environment {
    variables = {} # CRITICAL: remove all env vars so no secrets are present
  }
}
```

### Other

1. Open the AWS Lambda console and select the function
2. Go to Configuration > Environment variables
3. Click Edit
4. Delete variables that contain secrets (or remove all variables)
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [https://support.icompaas.com/support/solutions/articles/62000129505-ensure-there-are-no-secrets-in-lambda-functions-variables](https://support.icompaas.com/support/solutions/articles/62000129505-ensure-there-are-no-secrets-in-lambda-functions-variables)

## 技术信息

- Source Metadata：[sources/aws/awslambda_function_no_secrets_in_variables/metadata.json](../../sources/aws/awslambda_function_no_secrets_in_variables/metadata.json)
- Source Code：[sources/aws/awslambda_function_no_secrets_in_variables/check.py](../../sources/aws/awslambda_function_no_secrets_in_variables/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_no_secrets_in_variables/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_no_secrets_in_variables/check.py`

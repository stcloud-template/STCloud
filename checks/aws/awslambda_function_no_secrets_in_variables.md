# Lambda function environment variables do not contain secrets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_no_secrets_in_variables` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | critical |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Effects/Data Exposure |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

AWS Lambda function environment variables are analyzed for content that resembles **secrets** (API keys, tokens, passwords). Pattern-based detection highlights potential hardcoded credentials present in the function's environment.

## リスク

Secrets in Lambda environment variables weaken **confidentiality**: users with config read access, runtime introspection, or logs may obtain them. Exposure can grant access to downstream systems, enable **lateral movement**, and allow tampering, impacting **integrity** and **availability**.

## 推奨事項

Do not store secrets in environment variables or code. Use **AWS Secrets Manager** or **Parameter Store** with encryption, fetch at runtime using **least privilege** IAM, and prefer short-lived creds via **IAM roles**. Rotate keys, limit configuration read access, and apply **defense in depth** with logging and alerts for secret access.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [https://support.icompaas.com/support/solutions/articles/62000129505-ensure-there-are-no-secrets-in-lambda-functions-variables](https://support.icompaas.com/support/solutions/articles/62000129505-ensure-there-are-no-secrets-in-lambda-functions-variables)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_no_secrets_in_variables/metadata.json](../../sources/aws/awslambda_function_no_secrets_in_variables/metadata.json)
- Source Code：[sources/aws/awslambda_function_no_secrets_in_variables/check.py](../../sources/aws/awslambda_function_no_secrets_in_variables/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_no_secrets_in_variables/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_no_secrets_in_variables/check.py`

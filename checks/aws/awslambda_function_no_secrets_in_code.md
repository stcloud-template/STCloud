# Lambda function code contains no hardcoded secrets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `awslambda_function_no_secrets_in_code` |
| 云平台 | AWS |
| 服务 | awslambda |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Effects/Data Exposure |
| 资源类型 | AwsLambdaFunction |
| 资源组 | serverless |

## 描述

**Lambda function code** is analyzed for **embedded secrets** across files in the deployment package, detecting patterns like API keys, passwords, tokens, and connection strings. Findings reference file names and line numbers where potential secrets appear.

## 风险

**Hardcoded secrets** undermine confidentiality and integrity: if code, layers, or artifacts are exposed, attackers can reuse credentials to access databases, APIs, or cloud resources, enabling data exfiltration and unauthorized changes. Rotation is harder, increasing dwell time and blast radius of compromises.

## 推荐措施

Use **AWS Secrets Manager** (or Parameter Store) to store secrets and retrieve at runtime; never put them in code or Lambda env vars. - Apply **least privilege** IAM - Enable **rotation** - Prevent secret logging; encrypt - Add CI/CD secret scanning

## 修复步骤


### Other

1. In AWS Secrets Manager, click Store a new secret and create a secret for the value you hardcoded. Note the secret name/ARN.
2. In IAM > Roles, open your Lambda execution role and add an inline policy allowing secretsmanager:GetSecretValue on that secret only.
3. Edit your Lambda function code to remove the hardcoded value and retrieve it at runtime using the AWS SDK (GetSecretValue) with the secret name/ARN.
4. Deploy the updated function code.

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [https://aws.amazon.com/blogs/security/how-to-securely-provide-database-credentials-to-lambda-functions-by-using-aws-secrets-manager/](https://aws.amazon.com/blogs/security/how-to-securely-provide-database-credentials-to-lambda-functions-by-using-aws-secrets-manager/)
- [https://www.cloudcurls.com/2025/08/how-to-manage-secrets-securely-with-aws-secrets-manager.html](https://www.cloudcurls.com/2025/08/how-to-manage-secrets-securely-with-aws-secrets-manager.html)

## 技术信息

- Source Metadata：[sources/aws/awslambda_function_no_secrets_in_code/metadata.json](../../sources/aws/awslambda_function_no_secrets_in_code/metadata.json)
- Source Code：[sources/aws/awslambda_function_no_secrets_in_code/check.py](../../sources/aws/awslambda_function_no_secrets_in_code/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_no_secrets_in_code/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_no_secrets_in_code/check.py`

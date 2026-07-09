# Lambda function URL is not publicly accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `awslambda_function_url_public` |
| 云平台 | AWS |
| 服务 | awslambda |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| 资源类型 | AwsLambdaFunction |
| 资源组 | serverless |

## 描述

**AWS Lambda function URLs** are assessed to determine whether `AuthType` enforces **AWS IAM authentication** or permits **public invocation**. Applies to functions with a function URL and highlights when requests must be authenticated and authorized via IAM principals.

## 风险

An unauthenticated function URL lets anyone invoke code: - Confidentiality: data exposure - Integrity: unintended changes via over-privileged logic - Availability: DoS/denial-of-wallet through high request rates Attackers can script calls, exfiltrate data, and pivot using the function's permissions.

## 推荐措施

Enforce `AWS_IAM` on function URLs and apply **least privilege**: - Grant `lambda:InvokeFunctionUrl` only to required principals - Avoid `*` principals or broad conditions - Limit CORS to trusted origins and methods - Set reserved concurrency to contain abuse Consider **defense in depth** (WAF/CDN or private access) for Internet use.

## 修复步骤


### CLI

```text
aws lambda update-function-url-config --function-name <FUNCTION_NAME> --auth-type AWS_IAM
```

### Native IaC

```yaml
# CloudFormation: set Lambda Function URL to require IAM auth
Resources:
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn: arn:aws:lambda:<region>:<account-id>:function/<example_resource_name>
      AuthType: AWS_IAM  # CRITICAL: requires IAM authentication, preventing public access
```

### Terraform

```hcl
# Set Lambda Function URL to require IAM authentication
resource "aws_lambda_function_url" "example" {
  function_name      = "<example_resource_name>"
  authorization_type = "AWS_IAM"  # CRITICAL: blocks public access by requiring IAM auth
}
```

### Other

1. In AWS Console, go to Lambda > Functions and open <example_resource_name>
2. Select Configuration > Function URL > Edit
3. Set Auth type to AWS_IAM
4. Click Save

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/iam-auth-function-url.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/iam-auth-function-url.html)
- [https://www.roastdev.com/post/aws-lambda-url-invocations-with-iam-authentication-and-throttling-limits](https://www.roastdev.com/post/aws-lambda-url-invocations-with-iam-authentication-and-throttling-limits)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/lambda-functions.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/lambda-functions.html)
- [https://dev.to/aws-builders/hands-on-aws-lambda-function-url-with-aws-iam-authentication-type-180g](https://dev.to/aws-builders/hands-on-aws-lambda-function-url-with-aws-iam-authentication-type-180g)
- [https://www.rahulpnath.com/blog/how-to-secure-and-authenticate-lambda-function-urls/](https://www.rahulpnath.com/blog/how-to-secure-and-authenticate-lambda-function-urls/)

## 技术信息

- Source Metadata：[sources/aws/awslambda_function_url_public/metadata.json](../../sources/aws/awslambda_function_url_public/metadata.json)
- Source Code：[sources/aws/awslambda_function_url_public/check.py](../../sources/aws/awslambda_function_url_public/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_url_public/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_url_public/check.py`

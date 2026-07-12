# Lambda function URL CORS does not allow wildcard origins (*)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_url_cors_policy` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

**Lambda function URL** CORS policy is reviewed for `AllowOrigins`. The presence of `*` indicates a wide origin allowance in the CORS configuration.

## リスク

**Wildcard origins** allow any website to call the endpoint from a browser and read responses, weakening origin isolation. This can lead to data exposure (C) and unauthorized actions (I) if state-changing methods are reachable, enabling scripted abuse and cross-origin attacks.

## 推奨事項

Apply least privilege to CORS: - Restrict `AllowOrigins` to trusted domains; avoid `*` - Limit `AllowMethods`/`AllowHeaders`; disable `AllowCredentials` unless required - Prefer authenticated access (e.g., `AWS_IAM`) and enforce resource policies for defense in depth

## 修正手順


### CLI

```text
aws lambda update-function-url-config --function-name <example_resource_name> --cors AllowOrigins=https://www.example.com
```

### Native IaC

```yaml
# CloudFormation: restrict Lambda Function URL CORS to a specific origin
Resources:
  FunctionUrl:
    Type: AWS::Lambda::Url
    Properties:
      TargetFunctionArn: <example_resource_arn>
      AuthType: AWS_IAM
      Cors:
        AllowOrigins:
          - https://www.example.com  # Critical: removes '*' wildcard by allowing only this origin
```

### Terraform

```hcl
# Terraform: restrict Lambda Function URL CORS to a specific origin
resource "aws_lambda_function_url" "example" {
  function_name      = "<example_resource_name>"
  authorization_type = "AWS_IAM"
  cors {
    allow_origins = ["https://www.example.com"] # Critical: removes '*' wildcard by allowing only this origin
  }
}
```

### Other

1. In the AWS Console, go to Lambda > Functions and select <example_resource_name>
2. Open Configuration > Function URL > Edit
3. In CORS, remove '*' from Allowed origins and enter https://www.example.com
4. Save changes

## 参考資料

- [https://support.icompaas.com/support/solutions/articles/62000229584-ensure-lambda-function-url-cors-configurations-were-checked](https://support.icompaas.com/support/solutions/articles/62000229584-ensure-lambda-function-url-cors-configurations-were-checked)
- [https://docs.aws.amazon.com/lambda/latest/api/API_Cors.html](https://docs.aws.amazon.com/lambda/latest/api/API_Cors.html)
- [https://tutorialsdojo.com/how-to-configure-aws-lambda-function-url-with-cross-origin-resource-sharing/](https://tutorialsdojo.com/how-to-configure-aws-lambda-function-url-with-cross-origin-resource-sharing/)
- [https://dev.to/rimutaka/aws-lambda-function-url-with-cors-explained-by-example-14df](https://dev.to/rimutaka/aws-lambda-function-url-with-cors-explained-by-example-14df)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_url_cors_policy/metadata.json](../../sources/aws/awslambda_function_url_cors_policy/metadata.json)
- Source Code：[sources/aws/awslambda_function_url_cors_policy/check.py](../../sources/aws/awslambda_function_url_cors_policy/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_url_cors_policy/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_url_cors_policy/check.py`

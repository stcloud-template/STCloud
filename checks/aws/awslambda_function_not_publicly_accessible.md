# Lambda function resource-based policy does not allow public access

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `awslambda_function_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | awslambda |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsLambdaFunction |
| 资源组 | serverless |

## 描述

**AWS Lambda** function resource-based policies are assessed for **public access**. The finding identifies policies with wildcard or empty `Principal` that allow actions like `lambda:InvokeFunction` to any principal.

## 风险

**Public invocation** lets outsiders run code under the function's IAM role. Impacts: - **Confidentiality**: data exfiltration via backend access - **Integrity**: unauthorized state changes from side effects - **Availability/cost**: invocation floods causing throttling and spend spikes

## 推荐措施

Remove public principals from function policies. Grant access only to specific accounts, roles, or services using fixed ARNs and **least privilege**. Add conditions like `AWS:SourceAccount` and `AWS:SourceArn` to constrain service triggers. Enforce **separation of duties** and monitor access for **defense in depth**.

## 修复步骤


### CLI

```text
aws lambda remove-permission --function-name <example_function_name> --statement-id <example_statement_id>
```

### Native IaC

```yaml
# CloudFormation: restrict Lambda permission to a non-public principal
Resources:
  <example_resource_name>Permission:
    Type: AWS::Lambda::Permission
    Properties:
      Action: lambda:InvokeFunction
      FunctionName: <example_resource_name>
      Principal: 123456789012  # Critical: not "*"; limits invoke permission to a specific account to prevent public access
```

### Terraform

```hcl
# Restrict Lambda permission to a non-public principal
resource "aws_lambda_permission" "<example_resource_name>" {
  statement_id  = "AllowSpecificPrincipal"
  action        = "lambda:InvokeFunction"
  function_name = "<example_resource_name>"
  principal     = "123456789012"  # Critical: not "*"; prevents public access
}
```

### Other

1. Open the AWS Lambda console and select the function
2. Go to Configuration > Permissions
3. Under Resource-based policy, view the policy statements
4. Find any statement with Principal set to "*" (or { "AWS": "*" })
5. Delete that statement and save
6. If access is needed, re-add a permission for a specific principal only (for example, an AWS account ID or a service principal)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-public-access-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-public-access-prohibited.html)
- [https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/function-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/function-exposed.html)

## 技术信息

- Source Metadata：[sources/aws/awslambda_function_not_publicly_accessible/metadata.json](../../sources/aws/awslambda_function_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/awslambda_function_not_publicly_accessible/check.py](../../sources/aws/awslambda_function_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_not_publicly_accessible/check.py`

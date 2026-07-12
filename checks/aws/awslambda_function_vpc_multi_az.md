# Lambda function is configured with VPC subnets in at least two Availability Zones

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_vpc_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

**AWS Lambda** functions attached to a VPC use subnets that span at least the required number of **Availability Zones** (`2` by default). The evaluation counts the unique AZs of the function's configured subnets.

## リスク

Single-AZ placement limits **availability**. An AZ outage or subnet/IP exhaustion can block ENI creation and VPC access, causing failed invocations, timeouts, and event backlogs. This degrades uptime and can delay processing of critical events.

## 推奨事項

Distribute VPC-connected functions across subnets in `2` distinct AZs to ensure **fault tolerance**. - Choose subnets from different AZs - Avoid AZ-pinned configs or fixed IPs - Provide per-AZ egress/endpoints and routing - Regularly test AZ failover Aligns with **resilience** and **defense in depth**.

## 修正手順


### CLI

```text
aws lambda update-function-configuration --function-name <example_resource_name> --vpc-config SubnetIds=<subnet_id_az1>,<subnet_id_az2>,SecurityGroupIds=<example_security_group_id>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::Lambda::Function
    Properties:
      Role: <example_role_arn>
      Handler: index.handler
      Runtime: python3.12
      Code:
        ZipFile: |
          def handler(event, context):
            return ""
      VpcConfig:
        SecurityGroupIds:
          - <example_security_group_id>
        SubnetIds:
          - <subnet_id_az1>  # Critical: select subnets in different AZs
          - <subnet_id_az2>  # Critical: ensures function operates in >=2 AZs
```

### Terraform

```hcl
resource "aws_lambda_function" "<example_resource_name>" {
  function_name = "<example_resource_name>"
  role          = "<example_role_arn>"
  handler       = "index.handler"
  runtime       = "python3.12"
  filename      = "function.zip"

  vpc_config {
    subnet_ids         = ["<subnet_id_az1>", "<subnet_id_az2>"] # Critical: subnets in different AZs
    security_group_ids = ["<example_security_group_id>"]
  }
}
```

### Other

1. Open the Lambda console and select the function
2. Go to Configuration > VPC > Edit
3. Select the target VPC and choose at least two subnets in different Availability Zones
4. Select a security group
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/lambda/latest/operatorguide/networking-vpc.html](https://docs.aws.amazon.com/lambda/latest/operatorguide/networking-vpc.html)
- [https://stackzonecom.tawk.help/article/aws-config-rule-lambda-vpc-multi-az-check](https://stackzonecom.tawk.help/article/aws-config-rule-lambda-vpc-multi-az-check)
- [https://stackoverflow.com/questions/62052490/why-aws-lambda-suggests-to-set-up-two-subnets-if-vpc-is-configured](https://stackoverflow.com/questions/62052490/why-aws-lambda-suggests-to-set-up-two-subnets-if-vpc-is-configured)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-5](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-5)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_vpc_multi_az/metadata.json](../../sources/aws/awslambda_function_vpc_multi_az/metadata.json)
- Source Code：[sources/aws/awslambda_function_vpc_multi_az/check.py](../../sources/aws/awslambda_function_vpc_multi_az/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_vpc_multi_az/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_vpc_multi_az/check.py`

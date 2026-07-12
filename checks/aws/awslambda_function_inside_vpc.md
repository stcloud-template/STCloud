# Lambda function is deployed inside a VPC

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `awslambda_function_inside_vpc` |
| クラウドプラットフォーム | AWS |
| サービス | awslambda |
| 重大度 | low |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsLambdaFunction |
| リソースグループ | serverless |

## 説明

**AWS Lambda function** uses **VPC networking** with specified subnets and security groups, rather than the default Lambda-managed network. Presence of a VPC association (`vpc_id`) indicates private connectivity to VPC resources.

## リスク

Without VPC attachment, functions lack network isolation and granular egress control, weakening **confidentiality** and **integrity**. Traffic must use public endpoints, raising risks of data exfiltration and SSRF via unrestricted outbound. If private databases are required, missing VPC access can impact **availability**.

## 推奨事項

Attach functions to a VPC with private subnets and restrictive security groups to enforce **least privilege** and egress control. - Prefer **VPC endpoints** for AWS services - Use NAT only when necessary - Spread subnets across AZs for resilience - Govern with IAM conditions requiring `VpcIds`, `SubnetIds`, and `SecurityGroupIds`.

## 修正手順


### CLI

```text
aws lambda update-function-configuration --function-name <example_resource_name> --vpc-config SubnetIds=<example_subnet_id>,SecurityGroupIds=<example_security_group_id>
```

### Native IaC

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  LambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: <example_resource_name>
      Role: <example_role_arn>
      Handler: index.handler
      Runtime: python3.12
      Code:
        S3Bucket: <example_code_bucket>
        S3Key: <example_code_key>
      # Critical: Attach the function to a VPC by specifying at least one subnet and one security group
      # This sets VpcConfig, which gives the function a VPC ID and makes the check PASS
      VpcConfig:
        SubnetIds:
          - <example_subnet_id>
        SecurityGroupIds:
          - <example_security_group_id>
```

### Terraform

```hcl
resource "aws_lambda_function" "example" {
  function_name = "<example_resource_name>"
  role          = "<example_role_arn>"
  handler       = "index.handler"
  runtime       = "python3.12"
  filename      = "<example_package.zip>"

  # Critical: VPC config attaches the function to a VPC, providing a VPC ID so the check passes
  vpc_config {
    subnet_ids         = ["<example_subnet_id>"]      # at least one subnet
    security_group_ids = ["<example_security_group_id>"]
  }
}
```

### Other

1. In the AWS Lambda console, open your function
2. Go to Configuration > VPC and click Edit
3. Select the target VPC
4. Choose at least one Subnet and one Security group
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- [https://repost.aws/pt/knowledge-center/lambda-dedicated-vpc](https://repost.aws/pt/knowledge-center/lambda-dedicated-vpc)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/function-in-vpc.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Lambda/function-in-vpc.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-3](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-3)
- [https://stackoverflow.com/questions/55074793/how-can-we-force-aws-lamda-to-run-securely-in-a-vpc](https://stackoverflow.com/questions/55074793/how-can-we-force-aws-lamda-to-run-securely-in-a-vpc)
- [https://www.techtarget.com/searchCloudComputing/answer/How-do-I-configure-AWS-Lambda-functions-in-a-VPC/](https://www.techtarget.com/searchCloudComputing/answer/How-do-I-configure-AWS-Lambda-functions-in-a-VPC/)

## 技術情報

- Source Metadata：[sources/aws/awslambda_function_inside_vpc/metadata.json](../../sources/aws/awslambda_function_inside_vpc/metadata.json)
- Source Code：[sources/aws/awslambda_function_inside_vpc/check.py](../../sources/aws/awslambda_function_inside_vpc/check.py)
- Source Metadata Path：`sources/aws/awslambda_function_inside_vpc/metadata.json`
- Source Code Path：`sources/aws/awslambda_function_inside_vpc/check.py`

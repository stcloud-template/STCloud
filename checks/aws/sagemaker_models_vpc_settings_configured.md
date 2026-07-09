# Amazon SageMaker model has VPC settings enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_models_vpc_settings_configured` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | medium |
| 类别 | trust-boundaries, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

**SageMaker models** use **VPC settings** (`VpcConfig` with subnets and security groups) so inference containers communicate through a selected VPC rather than the public internet. This evaluates whether a model defines VPC subnets for its network path.

## 风险

Without **VPC isolation**, model traffic and data access can traverse public paths, weakening **confidentiality** and **integrity** through interception or misrouting. Missing security groups and private endpoints reduce **access control**, enabling excessive egress, data exfiltration, or command-and-control from compromised containers.

## 推荐措施

Enable **VPC-only networking** for models by defining `VpcConfig` with private subnets and restrictive security groups. Apply **least privilege egress**, use **VPC endpoints** for S3 and SageMaker runtime, avoid public routes, and implement **defense in depth** with segmentation and traffic monitoring.

## 修复步骤


### Native IaC

```yaml
Resources:
  SageMakerModel:
    Type: AWS::SageMaker::Model
    Properties:
      ExecutionRoleArn: "<example_resource_id>"
      PrimaryContainer:
        Image: "<example_resource_name>"
      # Critical: VpcConfig enables VPC networking for the model so the check passes
      VpcConfig:
        SecurityGroupIds:
          - "<example_resource_id>"  # Critical: security group in the VPC
        Subnets:
          - "<example_resource_id>"  # Critical: at least one subnet in the VPC
```

### Terraform

```hcl
resource "aws_sagemaker_model" "model" {
  name               = "<example_resource_name>"
  execution_role_arn = "<example_resource_id>"

  primary_container {
    image = "<example_resource_name>"
  }

  # Critical: VPC config enables VPC networking for the model so the check passes
  vpc_config {
    subnets            = ["<example_resource_id>"]       # Critical
    security_group_ids = ["<example_resource_id>"]       # Critical
  }
}
```

### Other

1. Open the AWS Console > Amazon SageMaker > Inference > Models
2. Open the model and note its container image and execution role
3. Delete the model (models cannot be updated to add VPC settings)
4. Click Create model
5. Enter the same Model name, set the Execution role, and the Container image
6. Under Network, select a VPC, then choose at least one Subnet and one Security group
7. Create the model
8. Verify the model shows VPC settings enabled

## 参考资料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_models_vpc_settings_configured/metadata.json](../../sources/aws/sagemaker_models_vpc_settings_configured/metadata.json)
- Source Code：[sources/aws/sagemaker_models_vpc_settings_configured/check.py](../../sources/aws/sagemaker_models_vpc_settings_configured/check.py)
- Source Metadata Path：`sources/aws/sagemaker_models_vpc_settings_configured/metadata.json`
- Source Code Path：`sources/aws/sagemaker_models_vpc_settings_configured/check.py`

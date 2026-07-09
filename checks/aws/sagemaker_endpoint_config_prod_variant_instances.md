# SageMaker endpoint configuration has all production variants with at least two initial instances

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_endpoint_config_prod_variant_instances` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | medium |
| 类别 | resilience, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

Amazon SageMaker endpoint configurations are evaluated to ensure each production variant uses an **initial instance count** of at least two. Variants with `InitialInstanceCount` less than two in instance-based endpoints are identified, indicating no built-in multi-AZ redundancy.

## 风险

A **single-instance variant** is a **single point of failure**. If the instance or its Availability Zone fails, inference becomes unavailable, leading to **service outages**, **SLA breaches**, and **cascading failures** in dependent systems. This primarily degrades **availability** and reliability.

## 推荐措施

Apply the **resilience** principle: - Run each production variant with `InitialInstanceCount >= 2` - Spread capacity across AZs with health-based scaling - Use rolling/canary updates to avoid downtime - Right-size capacity to tolerate node loss *For bursty workloads, consider serverless or autoscaling for elasticity.*

## 修复步骤


### CLI

```text
aws sagemaker delete-endpoint-config --endpoint-config-name <endpoint-config-name>
```

### Native IaC

```yaml
# CloudFormation: EndpointConfig with InitialInstanceCount > 1
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::EndpointConfig
    Properties:
      ProductionVariants:
        - VariantName: <example_resource_name>
          ModelName: <example_resource_name>
          InstanceType: ml.m5.large
          InitialInstanceCount: 2  # Critical: set >=2 so all variants start with at least two instances
```

### Terraform

```hcl
# SageMaker Endpoint Configuration with InitialInstanceCount > 1
resource "aws_sagemaker_endpoint_configuration" "<example_resource_name>" {
  production_variants {
    variant_name           = "<example_resource_name>"
    model_name             = "<example_resource_name>"
    instance_type          = "ml.m5.large"
    initial_instance_count = 2 # Critical: set >=2 so the variant passes the check
  }
}
```

### Other

1. In the AWS Console, go to SageMaker > Inference > Endpoint configurations
2. Click Create endpoint configuration and add each Production variant with Initial instance count set to 2
3. If any endpoints use the old configuration, go to SageMaker > Inference > Endpoints, select the endpoint, choose Update, and select the new endpoint configuration
4. Return to Endpoint configurations and delete the noncompliant configuration

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-4](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-4)
- [https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-config-prod-instance-count.html](https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-config-prod-instance-count.html)
- [https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html#serverless-endpoints-create-config](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-create.html#serverless-endpoints-create-config)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_endpoint_config_prod_variant_instances/metadata.json](../../sources/aws/sagemaker_endpoint_config_prod_variant_instances/metadata.json)
- Source Code：[sources/aws/sagemaker_endpoint_config_prod_variant_instances/check.py](../../sources/aws/sagemaker_endpoint_config_prod_variant_instances/check.py)
- Source Metadata Path：`sources/aws/sagemaker_endpoint_config_prod_variant_instances/metadata.json`
- Source Code Path：`sources/aws/sagemaker_endpoint_config_prod_variant_instances/check.py`

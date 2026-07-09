# Amazon SageMaker notebook instance has VPC settings configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_notebook_instance_vpc_settings_configured` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | high |
| 类别 | internet-exposed, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsSageMakerNotebookInstance |
| 资源组 | ai_ml |

## 描述

**SageMaker notebook instances** are evaluated for **VPC attachment**. Instances configured with a VPC (via a `subnet_id` and security groups) use private networking; those without VPC settings rely on public networking.

## 风险

Without a VPC, notebooks lose **network isolation**. Traffic to AWS services may traverse the public internet, limiting **egress control** and **private endpoints**, enabling data exfiltration and interception, and easing lateral movement-impacting **confidentiality** and **integrity**.

## 推荐措施

Run notebooks in a **private VPC**, applying **least-privilege** security groups and **network segmentation**. Prefer **VPC endpoints** for AWS services and restrict outbound traffic to approved destinations to enforce **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: SageMaker Notebook Instance with VPC settings
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      InstanceType: ml.t3.medium
      RoleArn: <example_resource_id>
      SubnetId: <example_resource_id>  # critical: places the notebook in a VPC subnet so the check passes
```

### Terraform

```hcl
resource "aws_sagemaker_notebook_instance" "<example_resource_name>" {
  name          = "<example_resource_name>"
  role_arn      = "<example_resource_id>"
  instance_type = "ml.t3.medium"
  subnet_id     = "<example_resource_id>" # critical: ensures the notebook is in a VPC subnet to pass the check
}
```

### Other

1. In the AWS Console, go to SageMaker > Notebook instances
2. Select the failing notebook instance, choose Stop, then Delete
3. Click Create notebook instance and use the same name
4. Under Network, select your VPC and a Subnet (select any required Security group)
5. Create the notebook instance
6. After it is InService, rerun the check

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-instance-in-vpc.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-instance-in-vpc.html)
- [https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_notebook_instance_vpc_settings_configured/metadata.json](../../sources/aws/sagemaker_notebook_instance_vpc_settings_configured/metadata.json)
- Source Code：[sources/aws/sagemaker_notebook_instance_vpc_settings_configured/check.py](../../sources/aws/sagemaker_notebook_instance_vpc_settings_configured/check.py)
- Source Metadata Path：`sources/aws/sagemaker_notebook_instance_vpc_settings_configured/metadata.json`
- Source Code Path：`sources/aws/sagemaker_notebook_instance_vpc_settings_configured/check.py`

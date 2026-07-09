# Amazon SageMaker notebook instance has direct internet access disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_notebook_instance_without_direct_internet_access_configured` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | high |
| 类别 | internet-exposed, trust-boundaries, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, Effects/Data Exfiltration |
| 资源类型 | AwsSageMakerNotebookInstance |
| 资源组 | ai_ml |

## 描述

Amazon SageMaker notebook instances are evaluated for the `DirectInternetAccess` setting. Instances with it disabled use only VPC connectivity; instances with it enabled permit direct outbound internet access.

## 风险

Direct internet access from notebooks weakens **egress control**, risking **confidentiality** and **integrity**. Adversaries or unvetted code can exfiltrate data, download malware, or run command-and-control. Public package installs bypass inspection, enabling supply-chain tampering and **lateral movement** from compromised sessions.

## 推荐措施

Disable direct internet access (`DirectInternetAccess: Disabled`) and place notebooks in private subnets. Use **VPC endpoints/PrivateLink** for required services, restrict egress with allowlists and **least privilege** security groups, and apply **defense in depth** with network isolation and monitoring of outbound traffic.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: SageMaker notebook with direct internet access disabled
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      NotebookInstanceName: <example_resource_name>
      InstanceType: ml.t3.medium
      RoleArn: <example_role_arn>
      SubnetId: <example_subnet_id>               # Required when disabling direct internet access
      SecurityGroupIds:                           # Required when disabling direct internet access
        - <example_security_group_id>
      DirectInternetAccess: "Disabled"            # CRITICAL: disables direct internet access to pass the check
```

### Terraform

```hcl
# SageMaker notebook with direct internet access disabled
resource "aws_sagemaker_notebook_instance" "<example_resource_name>" {
  name                = "<example_resource_name>"
  role_arn            = "<example_role_arn>"
  instance_type       = "ml.t3.medium"
  subnet_id           = "<example_subnet_id>"          # Required when disabling direct internet access
  security_groups     = ["<example_security_group_id>"] # Required when disabling direct internet access

  direct_internet_access = "Disabled" # CRITICAL: disables direct internet access to pass the check
}
```

### Other

1. In the AWS Console, go to SageMaker > Notebook instances
2. Select the notebook instance, choose Stop, and wait until status is Stopped
3. Click Edit
4. Set Direct internet access to Disabled
5. If prompted, select a Subnet and at least one Security group (VPC required when disabled)
6. Click Update, then choose Start to bring the instance back online

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-direct-internet-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-direct-internet-access.html)
- [https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/metadata.json](../../sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/metadata.json)
- Source Code：[sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/check.py](../../sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/check.py)
- Source Metadata Path：`sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/metadata.json`
- Source Code Path：`sources/aws/sagemaker_notebook_instance_without_direct_internet_access_configured/check.py`

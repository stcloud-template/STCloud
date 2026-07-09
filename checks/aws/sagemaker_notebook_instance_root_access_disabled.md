# Amazon SageMaker notebook instance has root access disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_notebook_instance_root_access_disabled` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | medium |
| 类别 | identity-access, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Privilege Escalation |
| 资源类型 | AwsSageMakerNotebookInstance |
| 资源组 | ai_ml |

## 描述

**Amazon SageMaker notebook instances** with user **root access disabled**. The evaluation checks whether interactive users can obtain root privileges on the instance, highlighting notebooks where `RootAccess` is not set to `Disabled`.

## 风险

Allowing user **root access** enables full system control, risking **integrity** (tampering with code, packages, and kernels), **confidentiality** (reading secrets, credentials, data copies), and **availability** (disabling agents or breaking environments). Compromise of a notebook can lead to lateral movement via the instance role.

## 推荐措施

Apply **least privilege**: set `RootAccess` to `Disabled` for notebook users. Provide needed software via **managed images** or **lifecycle automation**, not ad-hoc root installs. Limit the notebook IAM role, enforce **defense in depth** (network isolation and monitoring), and require controlled admin workflows for privileged changes.

## 修复步骤


### CLI

```text
aws sagemaker update-notebook-instance --notebook-instance-name <example_resource_name> --root-access Disabled
```

### Native IaC

```yaml
# CloudFormation: Disable root access on a SageMaker Notebook Instance
Resources:
  Notebook:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      InstanceType: ml.t3.medium
      RoleArn: <example_role_arn>
      RootAccess: Disabled  # Critical: disables user root access to pass the check
```

### Terraform

```hcl
# Terraform: Disable root access on a SageMaker Notebook Instance
resource "aws_sagemaker_notebook_instance" "notebook" {
  name          = "<example_resource_name>"
  role_arn      = "<example_role_arn>"
  instance_type = "ml.t3.medium"
  root_access   = "Disabled"  # Critical: disables user root access to pass the check
}
```

### Other

1. In the AWS Console, go to SageMaker > Notebook instances
2. Select <example_resource_name> and click Stop if it is running
3. After it stops, click Edit
4. Set Root access to Disabled
5. Save changes, then click Start

## 参考资料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json](../../sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json)
- Source Code：[sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py](../../sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py`

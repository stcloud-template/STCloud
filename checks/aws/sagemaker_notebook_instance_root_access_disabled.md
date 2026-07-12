# Amazon SageMaker notebook instance has root access disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sagemaker_notebook_instance_root_access_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | sagemaker |
| 重大度 | medium |
| カテゴリ | identity-access, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Privilege Escalation |
| リソースタイプ | AwsSageMakerNotebookInstance |
| リソースグループ | ai_ml |

## 説明

**Amazon SageMaker notebook instances** with user **root access disabled**. The evaluation checks whether interactive users can obtain root privileges on the instance, highlighting notebooks where `RootAccess` is not set to `Disabled`.

## リスク

Allowing user **root access** enables full system control, risking **integrity** (tampering with code, packages, and kernels), **confidentiality** (reading secrets, credentials, data copies), and **availability** (disabling agents or breaking environments). Compromise of a notebook can lead to lateral movement via the instance role.

## 推奨事項

Apply **least privilege**: set `RootAccess` to `Disabled` for notebook users. Provide needed software via **managed images** or **lifecycle automation**, not ad-hoc root installs. Limit the notebook IAM role, enforce **defense in depth** (network isolation and monitoring), and require controlled admin workflows for privileged changes.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-root-access.html)

## 技術情報

- Source Metadata：[sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json](../../sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json)
- Source Code：[sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py](../../sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_notebook_instance_root_access_disabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_notebook_instance_root_access_disabled/check.py`

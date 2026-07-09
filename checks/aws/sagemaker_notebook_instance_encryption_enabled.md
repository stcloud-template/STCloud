# SageMaker notebook instance is encrypted with a KMS key

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_notebook_instance_encryption_enabled` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | high |
| 类别 | encryption, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsSageMakerNotebookInstance |
| 资源组 | ai_ml |

## 描述

**Amazon SageMaker notebook instances** are assessed for **at-rest encryption** using an AWS KMS key. The finding reflects whether a `KmsKeyId` is configured for the notebook's ML volume encryption.

## 风险

Without **at-rest encryption** using a customer-managed KMS key, data on notebook EBS volumes and snapshots can be exposed via storage access, copied backups, or host compromise, reducing **confidentiality** and limiting **key rotation** and **revocation** controls.

## 推荐措施

Use a **customer-managed KMS key** for notebook ML volumes by setting `KmsKeyId`, and apply KMS to related S3 inputs/outputs. Enforce **least privilege** on key usage, enable **rotation**, and align key access with **defense in depth** to protect data at rest.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: SageMaker notebook with KMS encryption
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      InstanceType: ml.t3.medium
      RoleArn: <example_resource_arn>
      KmsKeyId: <example_resource_id>  # Critical: encrypts the notebook's EBS volume with the specified KMS key
```

### Terraform

```hcl
# SageMaker notebook with KMS encryption
resource "aws_sagemaker_notebook_instance" "<example_resource_name>" {
  name          = "<example_resource_name>"
  role_arn      = "<example_resource_arn>"
  instance_type = "ml.t3.medium"
  kms_key_id    = "<example_resource_id>"  # Critical: enables EBS encryption using this KMS key
}
```

### Other

1. Open the AWS Console > Amazon SageMaker > Notebook instances
2. Select the failing notebook instance and click Stop
3. Click Create notebook instance
4. Enter name, choose instance type and IAM role
5. In Encryption key, select your KMS key
6. Create the instance and verify it starts
7. Migrate notebooks/data as needed (e.g., via S3)
8. Delete the old unencrypted notebook instance

## 参考资料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html](https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-data-encrypted.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/notebook-data-encrypted.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_notebook_instance_encryption_enabled/metadata.json](../../sources/aws/sagemaker_notebook_instance_encryption_enabled/metadata.json)
- Source Code：[sources/aws/sagemaker_notebook_instance_encryption_enabled/check.py](../../sources/aws/sagemaker_notebook_instance_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_notebook_instance_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_notebook_instance_encryption_enabled/check.py`

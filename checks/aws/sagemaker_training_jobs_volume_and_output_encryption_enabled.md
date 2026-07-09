# Amazon SageMaker training job volume has KMS encryption enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sagemaker_training_jobs_volume_and_output_encryption_enabled` |
| 云平台 | AWS |
| 服务 | sagemaker |
| 严重等级 | high |
| 类别 | encryption, gen-ai |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

**Amazon SageMaker training jobs** use **KMS encryption** for their attached ML storage volumes via `VolumeKmsKeyId`. The finding identifies training jobs where the volume encryption key is not configured.

## 风险

Missing **CMEK** leaves training data, checkpoints, and logs on the volume without tenant-controlled encryption. This reduces **confidentiality**, enables data exposure via snapshots or privileged access, and limits control over key policies, rotation, and emergency revocation.

## 推荐措施

Encrypt training volumes with **customer-managed KMS keys** and apply the same to S3 input/output. Use **least privilege** on key policies, enable **rotation**, restrict grants, and prevent storage of unencrypted artifacts to achieve **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: SageMaker TrainingJob with EBS volume KMS encryption enabled
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::TrainingJob
    Properties:
      TrainingJobName: <example_resource_name>
      RoleArn: <example_role_arn>
      AlgorithmSpecification:
        TrainingImage: <example_ecr_image_uri>
        TrainingInputMode: File
      OutputDataConfig:
        S3OutputPath: s3://<example_bucket>
      ResourceConfig:
        InstanceType: ml.m5.large
        InstanceCount: 1
        VolumeSizeInGB: 10
        VolumeKmsKeyId: <example_kms_key_arn>  # CRITICAL: Encrypts the training EBS volume with the specified KMS key
      StoppingCondition:
        MaxRuntimeInSeconds: 3600
```

### Terraform

```hcl
# SageMaker Training Job with EBS volume KMS encryption enabled
resource "aws_sagemaker_training_job" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  algorithm_specification {
    training_image      = "<example_ecr_image_uri>"
    training_input_mode = "File"
  }

  output_data_config {
    s3_output_path = "s3://<example_bucket>"
  }

  resource_config {
    instance_type     = "ml.m5.large"
    instance_count    = 1
    volume_size_in_gb = 10
    volume_kms_key_id = "<example_kms_key_arn>" # CRITICAL: Enables KMS encryption for the training EBS volume
  }

  stopping_condition {
    max_runtime_in_seconds = 3600
  }
}
```

### Other

1. In the AWS console, go to SageMaker > Training > Training jobs
2. Select the non-encrypted job and click Clone to create a new job
3. In Resource configuration, set Volume encryption key to your KMS key (Customer managed key)
4. Complete required fields and click Create training job
5. Verify the new job shows the KMS key under Volume encryption

## 参考资料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html](https://docs.aws.amazon.com/sagemaker/latest/dg/key-management.html)

## 技术信息

- Source Metadata：[sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/metadata.json](../../sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/metadata.json)
- Source Code：[sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/check.py](../../sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_training_jobs_volume_and_output_encryption_enabled/check.py`

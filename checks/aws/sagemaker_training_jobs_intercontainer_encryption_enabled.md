# Amazon SageMaker training job has inter-container traffic encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sagemaker_training_jobs_intercontainer_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | sagemaker |
| 重大度 | medium |
| カテゴリ | encryption, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Security, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

Amazon SageMaker training jobs have **inter-container traffic encryption** configured for container-to-container communications during training. The evaluation inspects the `EnableInterContainerTrafficEncryption` setting on training jobs.

## リスク

Without inter-container encryption, in-node traffic may be plaintext, enabling capture by a compromised host or co-resident workload. This threatens **confidentiality** (training data, model parameters, credentials) and **integrity** (tampering with gradients/results), and can facilitate **lateral movement** via token or session theft.

## 推奨事項

Enable `EnableInterContainerTrafficEncryption` on all training jobs to enforce **encryption in transit**. Apply **defense in depth**: combine with **network isolation**, limit roles and container privileges per **least privilege**, and standardize secure job templates or guardrails to prevent launching unencrypted jobs.

## 修正手順


### Native IaC

```yaml
# CloudFormation: SageMaker Training Job with inter-container traffic encryption enabled
Resources:
  SageMakerTrainingJob:
    Type: AWS::SageMaker::TrainingJob
    Properties:
      TrainingJobName: <example_resource_name>
      RoleArn: <example_resource_id>
      AlgorithmSpecification:
        TrainingImage: <example_resource_id>
        TrainingInputMode: File
      OutputDataConfig:
        S3OutputPath: s3://<example_resource_name>/
      ResourceConfig:
        InstanceCount: 1
        InstanceType: ml.m5.large
        VolumeSizeInGB: 10
      StoppingCondition:
        MaxRuntimeInSeconds: 3600
      EnableInterContainerTrafficEncryption: true  # Critical: encrypts traffic between containers to pass the check
```

### Terraform

```hcl
# Terraform: SageMaker Training Job with inter-container traffic encryption enabled
resource "aws_sagemaker_training_job" "job" {
  name     = "<example_resource_name>"
  role_arn = "<example_resource_id>"

  algorithm_specification {
    training_image      = "<example_resource_id>"
    training_input_mode = "File"
  }

  output_data_config {
    s3_output_path = "s3://<example_resource_name>/"
  }

  resource_config {
    instance_count = 1
    instance_type  = "ml.m5.large"
    volume_size_gb = 10
  }

  stopping_condition {
    max_runtime_in_seconds = 3600
  }

  enable_inter_container_traffic_encryption = true  # Critical: ensures inter-container traffic is encrypted
}
```

### Other

1. In the AWS console, go to Amazon SageMaker > Training jobs
2. Click Create training job
3. Configure required fields (algorithm, role, inputs, output, resources)
4. Enable the setting: Enable inter-container traffic encryption
5. Click Create to start the new job (existing jobs cannot be modified)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/enable-inter-container-traffic-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SageMaker/enable-inter-container-traffic-encryption.html)
- [https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html)

## 技術情報

- Source Metadata：[sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/metadata.json](../../sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/metadata.json)
- Source Code：[sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/check.py](../../sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_training_jobs_intercontainer_encryption_enabled/check.py`

# Amazon SageMaker training job has network isolation enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sagemaker_training_jobs_network_isolation_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | sagemaker |
| 重大度 | high |
| カテゴリ | trust-boundaries, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exfiltration |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

**SageMaker training jobs** have **network isolation** enabled, preventing the training container from making any inbound or outbound network calls during execution

## リスク

Without `network isolation`, training code can reach the internet or internal services, enabling: - **Data exfiltration** of datasets and model artifacts - **Supply-chain compromise** via untrusted downloads - **C2 beacons** and resource abuse This harms **confidentiality** and **integrity**, and may impact **availability**.

## 推奨事項

Enable **network isolation** for training jobs by default. If network access is required, enforce **least privilege** and **defense in depth**: - Use private networking and `VPC endpoints` - Restrict egress and narrow IAM permissions - Prepackage dependencies to avoid external downloads

## 修正手順


### Native IaC

```yaml
# CloudFormation: SageMaker Training Job with network isolation enabled
Resources:
  <example_resource_name>:
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
        InstanceType: ml.m5.large
        InstanceCount: 1
        VolumeSizeInGB: 10
      StoppingCondition:
        MaxRuntimeInSeconds: 3600
      InputDataConfig:
        - ChannelName: training
          DataSource:
            S3DataSource:
              S3DataType: S3Prefix
              S3Uri: s3://<example_resource_name>/input/
      EnableNetworkIsolation: true  # Critical: blocks all network access from the training container
```

### Terraform

```hcl
# SageMaker Training Job with network isolation enabled
resource "aws_sagemaker_training_job" "<example_resource_name>" {
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
    instance_type  = "ml.m5.large"
    instance_count = 1
    volume_size_gb = 10
  }

  stopping_condition {
    max_runtime_in_seconds = 3600
  }

  input_data_config {
    channel_name = "training"
    data_source {
      s3_data_source {
        s3_data_type = "S3Prefix"
        s3_uri       = "s3://<example_resource_name>/input/"
      }
    }
  }

  enable_network_isolation = true # Critical: blocks all network access from the training container
}
```

### Other

1. In the AWS Console, open SageMaker > Training jobs
2. Click Create training job
3. Fill required fields (role, image, input/output, resources)
4. Enable the setting: Enable network isolation
5. Create the job

Note: You cannot edit an existing training job to enable this; create a new job with network isolation and retire non-compliant jobs.

## 参考資料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html)

## 技術情報

- Source Metadata：[sources/aws/sagemaker_training_jobs_network_isolation_enabled/metadata.json](../../sources/aws/sagemaker_training_jobs_network_isolation_enabled/metadata.json)
- Source Code：[sources/aws/sagemaker_training_jobs_network_isolation_enabled/check.py](../../sources/aws/sagemaker_training_jobs_network_isolation_enabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_training_jobs_network_isolation_enabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_training_jobs_network_isolation_enabled/check.py`

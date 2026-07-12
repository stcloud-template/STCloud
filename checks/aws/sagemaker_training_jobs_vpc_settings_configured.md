# Amazon SageMaker training job has VPC configuration enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sagemaker_training_jobs_vpc_settings_configured` |
| クラウドプラットフォーム | AWS |
| サービス | sagemaker |
| 重大度 | high |
| カテゴリ | trust-boundaries, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

**SageMaker training jobs** are evaluated for **VPC configuration** by detecting defined `subnets` in the job settings. With VPC settings, ENIs place the job in your VPC so traffic for training volumes and outputs uses private networking.

## リスク

Without VPC settings, training containers rely on public networking and broad egress. This weakens **confidentiality** and **integrity**, enabling data exfiltration of datasets or model artifacts, malware downloads, and bypass of granular security group controls and VPC-based monitoring.

## 推奨事項

Run training in a VPC using specific `subnets` and tightly scoped `security groups`. - Use `VPC endpoints` for S3, ECR, and SageMaker to keep traffic private - Block outbound Internet by default and allow only required destinations - Apply network segmentation and, when feasible, enable `network isolation`

## 修正手順


### Native IaC

```yaml
# CloudFormation: SageMaker TrainingJob with VPC enabled
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
      VpcConfig:
        Subnets:
          - <example_resource_id>  # CRITICAL: adds VPC subnets so job has VPC config
        SecurityGroupIds:
          - <example_resource_id>  # Required by SageMaker when using VPC
```

### Terraform

```hcl
# SageMaker Training Job with VPC configuration
resource "aws_sagemaker_training_job" "<example_resource_name>" {
  name     = "<example_resource_name>"
  role_arn = "<example_resource_id>"

  algorithm_specification {
    training_image     = "<example_resource_id>"
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

  vpc_config {
    subnets            = ["<example_resource_id>"]     # CRITICAL: enables VPC on the training job
    security_group_ids = ["<example_resource_id>"]     # Required with VPC
  }
}
```

### Other

1. In the AWS Console, go to SageMaker > Training > Training jobs
2. Click Create training job (or select a job and choose Create copy)
3. In Networking, select a VPC, then choose at least one Subnet and one Security group
4. Complete required fields and Create the job
5. Verify the new training job shows VPC subnets in its details

## 参考資料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html](https://docs.aws.amazon.com/sagemaker/latest/dg/interface-vpc-endpoint.html)

## 技術情報

- Source Metadata：[sources/aws/sagemaker_training_jobs_vpc_settings_configured/metadata.json](../../sources/aws/sagemaker_training_jobs_vpc_settings_configured/metadata.json)
- Source Code：[sources/aws/sagemaker_training_jobs_vpc_settings_configured/check.py](../../sources/aws/sagemaker_training_jobs_vpc_settings_configured/check.py)
- Source Metadata Path：`sources/aws/sagemaker_training_jobs_vpc_settings_configured/metadata.json`
- Source Code Path：`sources/aws/sagemaker_training_jobs_vpc_settings_configured/check.py`

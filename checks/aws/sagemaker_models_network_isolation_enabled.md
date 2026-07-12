# Amazon SageMaker model has network isolation enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sagemaker_models_network_isolation_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | sagemaker |
| 重大度 | high |
| カテゴリ | trust-boundaries, container-security, gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exfiltration |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

**SageMaker models** are evaluated for **network isolation** status, indicating whether model containers are blocked from initiating network connections during hosting/inference, aside from required service control traffic.

## リスク

**Disabled network isolation** allows model containers to reach external networks, enabling exfiltration of inputs, outputs, or credentials, retrieval of untrusted code, and covert callbacks. This compromises confidentiality and integrity and can facilitate lateral movement from the hosting environment.

## 推奨事項

Enable **network isolation** for all hosted models. Run endpoints in a **private VPC**, restrict egress with tight **security groups** and **VPC endpoints**, and enforce **least privilege IAM**. Adopt **defense in depth**: avoid public routes, allow-list destinations, and monitor outbound traffic.

## 修正手順


### Native IaC

```yaml
# CloudFormation: SageMaker Model with network isolation enabled
Resources:
  <example_resource_name>:
    Type: AWS::SageMaker::Model
    Properties:
      ExecutionRoleArn: <example_resource_arn>
      PrimaryContainer:
        Image: <example_image>
      EnableNetworkIsolation: true  # Critical: ensures the model container has network isolation enabled
```

### Terraform

```hcl
# SageMaker Model with network isolation enabled
resource "aws_sagemaker_model" "<example_resource_name>" {
  name               = "<example_resource_name>"
  execution_role_arn = "<example_resource_arn>"

  primary_container {
    image = "<example_image>"
  }

  enable_network_isolation = true  # Critical: enables network isolation to pass the check
}
```

### Other

1. In the AWS console, go to SageMaker > Inference > Models
2. Click Create model
3. Enter a name and select the execution role; set the container Image
4. Check Enable network isolation
5. Click Create model
6. If used by an endpoint, create a new endpoint configuration with this model and update the endpoint, then remove the old non-isolated model

## 参考資料

- [https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html)

## 技術情報

- Source Metadata：[sources/aws/sagemaker_models_network_isolation_enabled/metadata.json](../../sources/aws/sagemaker_models_network_isolation_enabled/metadata.json)
- Source Code：[sources/aws/sagemaker_models_network_isolation_enabled/check.py](../../sources/aws/sagemaker_models_network_isolation_enabled/check.py)
- Source Metadata Path：`sources/aws/sagemaker_models_network_isolation_enabled/metadata.json`
- Source Code Path：`sources/aws/sagemaker_models_network_isolation_enabled/check.py`

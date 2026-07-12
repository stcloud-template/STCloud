# AWS Config recorder is enabled and not in failure state or disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `config_recorder_all_regions_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | config |
| 重大度 | medium |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**AWS accounts** have **AWS Config recorders** active and healthy in each Region. It identifies Regions with no recorder, a disabled recorder, or a recorder in a failure state.

## リスク

**Gaps in Config recording** create **blind spots**. Changes in unmonitored Regions aren't captured, weakening **integrity** and **auditability**. Adversaries can alter resources or stage assets unnoticed, enabling misconfigurations and delaying **incident response**.

## 推奨事項

Enable **AWS Config** in every Region with continuous recording and maintain healthy recorder status.

## 修正手順


### Native IaC

```yaml
Resources:
  example_resource_recorder:
    Type: AWS::Config::ConfigurationRecorder
    Properties:
      Name: example_resource
      RoleARN: !Sub arn:aws:iam::${AWS::AccountId}:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig

  example_resource_channel:
    Type: AWS::Config::DeliveryChannel
    Properties:
      S3BucketName: example_resource

  example_resource_status:
    Type: AWS::Config::ConfigurationRecorderStatus
    Properties:
      Name: example_resource
      Recording: true  # This line fixes the security issue
    DependsOn:
      - example_resource_channel
```

### Terraform

```hcl
resource "aws_iam_service_linked_role" "example_resource" {
  aws_service_name = "config.amazonaws.com"
}

resource "aws_config_configuration_recorder" "example_resource" {
  name     = "example_resource"
  role_arn = aws_iam_service_linked_role.example_resource.arn
}

resource "aws_config_delivery_channel" "example_resource" {
  s3_bucket_name = "example_resource"
}

resource "aws_config_configuration_recorder_status" "example_resource" {
  name         = aws_config_configuration_recorder.example_resource.name
  is_recording = true  # This line fixes the security issue
  depends_on   = [aws_config_delivery_channel.example_resource]
}
```

### Other

1. In the AWS Console, go to Config
2. Click Set up AWS Config (or Settings)
3. Select a resource recording option (any) and choose an existing S3 bucket for delivery
4. Keep the default AWSServiceRoleForConfig role
5. Click Confirm/Turn on to start recording
6. Verify on the Settings page that Status shows Recording and not Failure

## 参考資料

- [https://repost.aws/es/questions/QUGcgeerhcTamRkwgdwh_tLQ/enable-aws-config](https://repost.aws/es/questions/QUGcgeerhcTamRkwgdwh_tLQ/enable-aws-config)
- [https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v1.5.0_L2.audit:6a5136528bd329139e5969f8f1e5ffbc](https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v1.5.0_L2.audit:6a5136528bd329139e5969f8f1e5ffbc)
- [https://aws.amazon.com/blogs/mt/aws-config-best-practices/](https://aws.amazon.com/blogs/mt/aws-config-best-practices/)

## 技術情報

- Source Metadata：[sources/aws/config_recorder_all_regions_enabled/metadata.json](../../sources/aws/config_recorder_all_regions_enabled/metadata.json)
- Source Code：[sources/aws/config_recorder_all_regions_enabled/check.py](../../sources/aws/config_recorder_all_regions_enabled/check.py)
- Source Metadata Path：`sources/aws/config_recorder_all_regions_enabled/metadata.json`
- Source Code Path：`sources/aws/config_recorder_all_regions_enabled/check.py`

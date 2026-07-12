# AWS Config recorder uses the AWSServiceRoleForConfig service-linked role

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `config_recorder_using_aws_service_role` |
| クラウドプラットフォーム | AWS |
| サービス | config |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**AWS Config recorders** are evaluated for use of the service‑linked IAM role `AWSServiceRoleForConfig` linked to `config.amazonaws.com` rather than a custom role. The evaluation inspects active recorders and their role ARN to confirm the AWS‑managed service‑linked role is in use.

## リスク

Using a custom or incorrect role can break recording or create blind spots, undermining the **integrity** and **availability** of configuration history. Over‑privileged roles weaken **least privilege**, increasing risk of unauthorized access, stealthy changes, and delayed incident response.

## 推奨事項

Use the AWS‑managed service‑linked role `AWSServiceRoleForConfig` for all recorders to enforce **least privilege** and consistent trust. Avoid custom roles; restrict who can modify the recorder or role; monitor for drift and ensure recording remains enabled as part of **defense in depth**.

## 修正手順


### CLI

```text
aws configservice put-configuration-recorder --configuration-recorder name=<RECORDER_NAME>,roleARN=arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig
```

### Native IaC

```yaml
Resources:
  example_resource:
    Type: AWS::Config::ConfigurationRecorder
    Properties:
      Name: example_resource
      RoleARN: arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig  # This line fixes the security issue
```

### Terraform

```hcl
resource "aws_config_configuration_recorder" "example_resource" {
  name     = "example_resource"
  role_arn = "arn:<PARTITION>:iam::<ACCOUNT_ID>:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"  # This line fixes the security issue
}
```

### Other

1. Open the AWS Console and go to AWS Config
2. Choose Settings (or Recording) and click Edit
3. For IAM role, select Use service-linked role (AWSServiceRoleForConfig)
4. Save changes

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1](https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1)
- [https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html](https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html)

## 技術情報

- Source Metadata：[sources/aws/config_recorder_using_aws_service_role/metadata.json](../../sources/aws/config_recorder_using_aws_service_role/metadata.json)
- Source Code：[sources/aws/config_recorder_using_aws_service_role/check.py](../../sources/aws/config_recorder_using_aws_service_role/check.py)
- Source Metadata Path：`sources/aws/config_recorder_using_aws_service_role/metadata.json`
- Source Code Path：`sources/aws/config_recorder_using_aws_service_role/check.py`

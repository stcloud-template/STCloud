# Elastic Beanstalk environment has managed platform updates enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticbeanstalk_environment_managed_updates_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticbeanstalk |
| 重大度 | high |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsElasticBeanstalkEnvironment |
| リソースグループ | compute |

## 説明

**Elastic Beanstalk environments** with **managed platform updates** enabled (`ManagedActionsEnabled: true`) automatically apply platform patch/minor updates during a scheduled maintenance window.

## リスク

Without automatic platform updates, environments may run **vulnerable OS/runtime versions**, enabling exploitation of known CVEs, RCE, or privilege escalation. Patch drift also increases instability, harming **availability** and undermining application **integrity**.

## 推奨事項

Enable **managed platform updates** with a set maintenance window and choose an update level (`patch` or `minor`). Ensure **enhanced health** is on and the update role follows **least privilege**. Validate in staging, roll out gradually, and stagger windows across environments to strengthen **defense in depth** and resilience.

## 修正手順


### CLI

```text
aws elasticbeanstalk update-environment --environment-name <environment-name> --option-settings Namespace=aws:elasticbeanstalk:managedactions,OptionName=ManagedActionsEnabled,Value=true
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ElasticBeanstalk::Environment
    Properties:
      ApplicationName: <example_resource_name>
      SolutionStackName: <example_resource_name>
      OptionSettings:
        - Namespace: aws:elasticbeanstalk:managedactions
          OptionName: ManagedActionsEnabled  # Critical: enables managed platform updates
          Value: "true"                      # Critical: set to true to pass the check
```

### Terraform

```hcl
resource "aws_elastic_beanstalk_environment" "<example_resource_name>" {
  name                = "<example_resource_name>"
  application         = "<example_resource_name>"
  solution_stack_name = "<example_resource_name>"

  setting {
    namespace = "aws:elasticbeanstalk:managedactions"
    name      = "ManagedActionsEnabled"   # Critical: enables managed platform updates
    value     = "true"                    # Critical: set to true to pass the check
  }
}
```

### Other

1. Open the AWS Management Console and go to Elastic Beanstalk
2. Select your environment
3. Choose Configuration
4. In Managed updates, click Edit
5. Turn Managed updates to Enabled
6. Click Apply/Save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-2](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-2)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElasticBeanstalk/managed-platform-updates.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElasticBeanstalk/managed-platform-updates.html)
- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-platform-update-managed.html)

## 技術情報

- Source Metadata：[sources/aws/elasticbeanstalk_environment_managed_updates_enabled/metadata.json](../../sources/aws/elasticbeanstalk_environment_managed_updates_enabled/metadata.json)
- Source Code：[sources/aws/elasticbeanstalk_environment_managed_updates_enabled/check.py](../../sources/aws/elasticbeanstalk_environment_managed_updates_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticbeanstalk_environment_managed_updates_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticbeanstalk_environment_managed_updates_enabled/check.py`

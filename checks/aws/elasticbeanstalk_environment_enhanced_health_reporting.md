# Elastic Beanstalk environment has enhanced health reporting enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticbeanstalk_environment_enhanced_health_reporting` |
| クラウドプラットフォーム | AWS |
| サービス | elasticbeanstalk |
| 重大度 | low |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| リソースタイプ | AwsElasticBeanstalkEnvironment |
| リソースグループ | compute |

## 説明

**Elastic Beanstalk environments** have health reporting set to `enhanced` instead of basic.

## リスク

Without **enhanced health**, issues are detected late, raising MTTR and enabling **service outages**. Hidden instance failures or bad deployments can create uneven fleets, degrading **availability** and potentially **integrity** (serving stale versions), while error spikes and thrash increase operational cost.

## 推奨事項

Set health reporting to `enhanced` for all environments and make it a security baseline. Connect health signals to alerts for rapid response. Apply **least privilege** to required roles and use **defense in depth** with auto-healing, alarms, and runbooks to prevent prolonged degradation.

## 修正手順


### CLI

```text
aws elasticbeanstalk update-environment --environment-name <environment-name> --option-settings Namespace=aws:elasticbeanstalk:healthreporting:system,OptionName=SystemType,Value=enhanced
```

### Native IaC

```yaml
# CloudFormation: enable enhanced health reporting for an Elastic Beanstalk environment
Resources:
  <example_resource_name>:
    Type: AWS::ElasticBeanstalk::Environment
    Properties:
      ApplicationName: <example_resource_name>
      EnvironmentName: <example_resource_name>
      SolutionStackName: <example_solution_stack>
      OptionSettings:
        - Namespace: aws:elasticbeanstalk:healthreporting:system
          OptionName: SystemType  # Critical: selects the enhanced health reporting system
          Value: enhanced          # Critical: sets health reporting to enhanced
```

### Terraform

```hcl
# Terraform: enable enhanced health reporting for an Elastic Beanstalk environment
resource "aws_elastic_beanstalk_environment" "<example_resource_name>" {
  name                = "<example_resource_name>"
  application         = "<example_resource_name>"
  solution_stack_name = "<example_solution_stack>"

  setting {
    namespace = "aws:elasticbeanstalk:healthreporting:system"
    name      = "SystemType"  # Critical: selects the enhanced health reporting system
    value     = "enhanced"    # Critical: sets health reporting to enhanced
  }
}
```

### Other

1. Open the AWS Elastic Beanstalk console and select your Region
2. Go to Environments and choose your environment
3. Select Configuration > Monitoring > Edit
4. Under Health reporting, set System to Enhanced
5. Click Apply to save the change

## 参考資料

- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-enable.html#health-enhanced-enable-console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-enable.html#health-enhanced-enable-console)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-1](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-1)

## 技術情報

- Source Metadata：[sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/metadata.json](../../sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/metadata.json)
- Source Code：[sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/check.py](../../sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/check.py)
- Source Metadata Path：`sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/metadata.json`
- Source Code Path：`sources/aws/elasticbeanstalk_environment_enhanced_health_reporting/check.py`

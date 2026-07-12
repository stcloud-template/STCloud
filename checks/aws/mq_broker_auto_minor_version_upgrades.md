# Amazon MQ broker has automated minor version upgrades enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `mq_broker_auto_minor_version_upgrades` |
| クラウドプラットフォーム | AWS |
| サービス | mq |
| 重大度 | low |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsAmazonMQBroker |
| リソースグループ | messaging |

## 説明

**Amazon MQ brokers** have `autoMinorVersionUpgrade` enabled to automatically apply supported minor and patch engine updates during the scheduled maintenance window.

## リスク

Without automatic minor upgrades, brokers may run **known-vulnerable engine versions**, enabling exploits that impact: - **Confidentiality**: message disclosure - **Integrity**: tampering or replay - **Availability**: crashes/DoS and instability Delayed patches also increase operational risk and drift.

## 推奨事項

Enable `autoMinorVersionUpgrade` on all brokers to reduce patch latency. - Align upgrades with a defined maintenance window - Validate changes in staging before production - Monitor broker health and logs after updates - Maintain HA and tested backups for rollback (*defense in depth*)

## 修正手順


### CLI

```text
aws mq update-broker --broker-id <example_resource_id> --auto-minor-version-upgrade
```

### Native IaC

```yaml
# CloudFormation: Enable automatic minor version upgrades on an MQ broker
Resources:
  <example_resource_name>:
    Type: AWS::AmazonMQ::Broker
    Properties:
      BrokerName: <example_resource_name>
      AutoMinorVersionUpgrade: true  # Critical: enables automatic minor version upgrades
      DeploymentMode: SINGLE_INSTANCE
      EngineType: ACTIVEMQ
      EngineVersion: <ENGINE_VERSION>
      HostInstanceType: mq.t3.micro
      PubliclyAccessible: true
      Users:
        - Username: <USERNAME>
          Password: <PASSWORD>
```

### Terraform

```hcl
# Terraform: Enable automatic minor version upgrades on an MQ broker
resource "aws_mq_broker" "<example_resource_name>" {
  broker_name                = "<example_resource_name>"
  engine_type                = "ActiveMQ"
  engine_version             = "<ENGINE_VERSION>"
  host_instance_type         = "mq.t3.micro"
  publicly_accessible        = true
  auto_minor_version_upgrade = true  # Critical: enables automatic minor version upgrades

  user {
    username = "<USERNAME>"
    password = "<PASSWORD>"
  }
}
```

### Other

1. Open the Amazon MQ console
2. Go to Brokers and select the target broker
3. Click Edit
4. Under Maintenance, check Enable automatic minor version upgrades
5. Click Save

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/auto-minor-version-upgrade.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/auto-minor-version-upgrade.html)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-brokers.html#upgrading-brokers-automatic-upgrades](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-brokers.html#upgrading-brokers-automatic-upgrades)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-3](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-3)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-brokers.html#upgrading-brokers-automatic-upgrades.html](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-brokers.html#upgrading-brokers-automatic-upgrades.html)

## 技術情報

- Source Metadata：[sources/aws/mq_broker_auto_minor_version_upgrades/metadata.json](../../sources/aws/mq_broker_auto_minor_version_upgrades/metadata.json)
- Source Code：[sources/aws/mq_broker_auto_minor_version_upgrades/check.py](../../sources/aws/mq_broker_auto_minor_version_upgrades/check.py)
- Source Metadata Path：`sources/aws/mq_broker_auto_minor_version_upgrades/metadata.json`
- Source Code Path：`sources/aws/mq_broker_auto_minor_version_upgrades/check.py`

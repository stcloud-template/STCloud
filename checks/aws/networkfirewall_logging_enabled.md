# Network Firewall has logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `networkfirewall_logging_enabled` |
| 云平台 | AWS |
| 服务 | networkfirewall |
| 严重等级 | high |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| 资源类型 | AwsNetworkFirewallFirewall |
| 资源组 | network |

## 描述

**AWS Network Firewall** has stateful engine logging configured with at least one log type (`FLOW`, `ALERT`, or `TLS`) and an active log destination

## 风险

Absent Network Firewall logs reduce **visibility** and **forensics**. Malicious flows, C2 traffic, and data exfiltration can go **undetected**, impacting: - Confidentiality (leakage) - Integrity (unauthorized traffic allowed) - Availability (DDoS patterns unnoticed)

## 推荐措施

Enable comprehensive firewall logging and send `FLOW`, `ALERT`, and *when applicable* `TLS` events to a centralized, tamper-resistant destination. Apply **least privilege** to writers/readers, enforce **encryption** and **retention**, and integrate alerts with monitoring for **defense in depth**.

## 修复步骤


### CLI

```text
aws network-firewall update-logging-configuration --firewall-arn <FIREWALL_ARN> --logging-configuration 'LogDestinationConfigs=[{LogType=FLOW,LogDestinationType=CLOUDWATCH_LOGS,LogDestination={LogGroup=<LOG_GROUP_NAME>}}]'
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::NetworkFirewall::LoggingConfiguration
    Properties:
      FirewallArn: <example_resource_id>  # CRITICAL: Targets the firewall to enable logging
      LoggingConfiguration:
        LogDestinationConfigs:
          - LogType: FLOW                  # CRITICAL: Enables at least one log type
            LogDestinationType: CloudWatchLogs  # CRITICAL: Selects a valid destination type
            LogDestination:
              logGroup: <example_log_group_name>  # CRITICAL: Existing CloudWatch Logs group to receive logs
```

### Terraform

```hcl
resource "aws_networkfirewall_logging_configuration" "<example_resource_name>" {
  firewall_arn = "<example_resource_id>"  # CRITICAL: Targets the firewall to enable logging

  logging_configuration {
    log_destination_config {
      log_type             = "FLOW"              # CRITICAL: Enables at least one log type
      log_destination_type = "CloudWatchLogs"   # CRITICAL: Selects a valid destination type
      log_destination = {
        logGroup = "<example_log_group_name>"   # CRITICAL: Existing CloudWatch Logs group to receive logs
      }
    }
  }
}
```

### Other

1. Open the AWS console and go to VPC > Network Firewall > Firewalls
2. Select your firewall and open the Firewall details tab
3. In the Logging section, click Edit
4. Enable at least one Log type (e.g., Flow)
5. Choose Destination type: CloudWatch Logs and select an existing log group
6. Click Save

## 参考资料

- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html)
- [https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-update-logging-configuration.html](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-update-logging-configuration.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-2](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-2)

## 技术信息

- Source Metadata：[sources/aws/networkfirewall_logging_enabled/metadata.json](../../sources/aws/networkfirewall_logging_enabled/metadata.json)
- Source Code：[sources/aws/networkfirewall_logging_enabled/check.py](../../sources/aws/networkfirewall_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/networkfirewall_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/networkfirewall_logging_enabled/check.py`

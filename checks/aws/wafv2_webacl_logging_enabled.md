# AWS WAFv2 Web ACL has logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `wafv2_webacl_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | wafv2 |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsWafv2WebAcl |
| リソースグループ | security |

## 説明

**AWS WAFv2 Web ACLs** with **logging** capture details of inspected requests and rule evaluations. The assessment determines for each Web ACL whether logging is configured to record traffic analyzed by that ACL.

## リスク

Without **WAF logging**, visibility into allowed/blocked requests is lost, degrading detection and response. **SQLi**, **credential stuffing**, and **bot/DDoS probes** can go unnoticed, risking data exposure (C), undetected rule misuse (I), and service instability from unseen abuse (A).

## 推奨事項

Enable **logging** on all WAFv2 Web ACLs to a centralized destination. Apply **least privilege** for log delivery, **redact sensitive fields**, and filter to retain high-value events. Integrate with monitoring/SIEM for **alerting and correlation**, and review routinely as part of **defense in depth**.

## 修正手順


### CLI

```text
aws wafv2 put-logging-configuration --logging-configuration ResourceArn=<WEB_ACL_ARN>,LogDestinationConfigs=<DESTINATION_ARN>
```

### Native IaC

```yaml
# CloudFormation: Enable logging for a WAFv2 Web ACL
Resources:
  <example_resource_name>:
    Type: AWS::WAFv2::LoggingConfiguration
    Properties:
      ResourceArn: arn:aws:wafv2:<region>:<account-id>:regional/webacl/<example_resource_name>/<example_resource_id>  # CRITICAL: target Web ACL to log
      LogDestinationConfigs:  # CRITICAL: where logs are sent
        - arn:aws:logs:<region>:<account-id>:log-group:aws-waf-logs-<example_resource_name>
```

### Terraform

```hcl
# Enable logging for a WAFv2 Web ACL
resource "aws_wafv2_web_acl_logging_configuration" "<example_resource_name>" {
  resource_arn           = "<example_resource_arn>"                 # CRITICAL: target Web ACL ARN
  log_destination_configs = ["<example_destination_arn>"]           # CRITICAL: log destination ARN
}
```

### Other

1. In the AWS Console, go to AWS WAF & Shield > Web ACLs
2. Select the target Web ACL
3. Open the Logging and metrics (or Logging) section and click Enable logging
4. Choose a log destination (CloudWatch Logs log group, S3 bucket, or Kinesis Data Firehose)
5. Click Save to enable logging

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WAF/enable-web-acls-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/WAF/enable-web-acls-logging.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-11](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-11)
- [https://docs.aws.amazon.com/cli/latest/reference/wafv2/put-logging-configuration.html](https://docs.aws.amazon.com/cli/latest/reference/wafv2/put-logging-configuration.html)
- [https://docs.aws.amazon.com/waf/latest/developerguide/logging.html](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)

## 技術情報

- Source Metadata：[sources/aws/wafv2_webacl_logging_enabled/metadata.json](../../sources/aws/wafv2_webacl_logging_enabled/metadata.json)
- Source Code：[sources/aws/wafv2_webacl_logging_enabled/check.py](../../sources/aws/wafv2_webacl_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/wafv2_webacl_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/wafv2_webacl_logging_enabled/check.py`

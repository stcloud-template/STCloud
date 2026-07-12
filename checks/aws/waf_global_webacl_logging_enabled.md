# AWS WAF Classic Global Web ACL has logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `waf_global_webacl_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | waf |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsWafWebAcl |
| リソースグループ | security |

## 説明

**AWS WAF Classic global Web ACLs** have **logging** enabled to capture evaluated web requests and rule actions for each ACL

## リスク

Without **WAF logging**, you lose **visibility** into attacks (SQLi/XSS probes, bots, brute-force) and into allow/block decisions, limiting detection and forensics. This degrades **confidentiality**, **integrity**, and **availability**, and slows incident response and tuning.

## 推奨事項

Enable **logging** on all global Web ACLs and send records to a centralized logging platform. Apply **least privilege** to log destinations and redact sensitive fields. Monitor and alert on anomalies, and integrate logs with incident response for **defense in depth** and faster containment.

## 修正手順


### CLI

```text
aws waf put-logging-configuration --logging-configuration ResourceArn=<web_acl_arn>,LogDestinationConfigs=<kinesis_firehose_delivery_stream_arn>
```

### Other

1. In the AWS console, create an Amazon Kinesis Data Firehose delivery stream named starting with "aws-waf-logs-" (for CloudFront/global, create it in us-east-1)
2. Open the AWS WAF console and switch to AWS WAF Classic
3. Select Filter: Global (CloudFront) and go to Web ACLs
4. Open the target Web ACL and go to the Logging tab
5. Click Enable logging and select the Firehose delivery stream created in step 1
6. Click Enable/Save

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-logging.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-logging.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-1](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-1)
- [https://docs.aws.amazon.com/cli/latest/reference/waf/put-logging-configuration.html](https://docs.aws.amazon.com/cli/latest/reference/waf/put-logging-configuration.html)

## 技術情報

- Source Metadata：[sources/aws/waf_global_webacl_logging_enabled/metadata.json](../../sources/aws/waf_global_webacl_logging_enabled/metadata.json)
- Source Code：[sources/aws/waf_global_webacl_logging_enabled/check.py](../../sources/aws/waf_global_webacl_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/waf_global_webacl_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/waf_global_webacl_logging_enabled/check.py`

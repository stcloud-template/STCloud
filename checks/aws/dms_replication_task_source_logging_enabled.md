# DMS replication task has logging enabled and SOURCE_CAPTURE and SOURCE_UNLOAD components set to at least Default severity

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dms_replication_task_source_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | dms |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Defense Evasion |
| リソースタイプ | AwsDmsReplicationTask |
| リソースグループ | database |

## 説明

**AWS DMS replication tasks** have **logging enabled** and configure `SOURCE_CAPTURE` and `SOURCE_UNLOAD` with severity at least `LOGGER_SEVERITY_DEFAULT` (or higher: `LOGGER_SEVERITY_DEBUG`, `LOGGER_SEVERITY_DETAILED_DEBUG`).

## リスク

Missing or low-severity source logs hinder visibility into **CDC** and full-load activity, risking undetected errors, stalls, or tampering. This can cause silent **data drift**, broken lineage, and failed recoveries, undermining **integrity** and **availability** and weakening auditability during investigations.

## 推奨事項

Enable and standardize **task logging** for `SOURCE_CAPTURE` and `SOURCE_UNLOAD` at `LOGGER_SEVERITY_DEFAULT` or higher. - Centralize logs and alert on anomalies - Enforce **least privilege** for log access - Set retention to support audits - Avoid prolonged `DEBUG` levels, *except during troubleshooting*, to balance visibility and cost

## 修正手順


### CLI

```text
aws dms modify-replication-task --replication-task-arn <example_resource_arn> --replication-task-settings '{"Logging":{"EnableLogging":true,"LogComponents":[{"Id":"SOURCE_CAPTURE","Severity":"LOGGER_SEVERITY_DEFAULT"},{"Id":"SOURCE_UNLOAD","Severity":"LOGGER_SEVERITY_DEFAULT"}]}}'
```

### Native IaC

```yaml
# CloudFormation: enable DMS source logging at minimum DEFAULT severity
Resources:
  <example_resource_name>:
    Type: AWS::DMS::ReplicationTask
    Properties:
      ReplicationInstanceArn: <example_resource_arn>
      SourceEndpointArn: <example_resource_arn>
      TargetEndpointArn: <example_resource_arn>
      MigrationType: full-load
      TableMappings: '{"rules":[]}'
      # Critical: Enables logging and sets SOURCE components to at least DEFAULT
      ReplicationTaskSettings: |
        {
          "Logging": {
            "EnableLogging": true,
            "LogComponents": [
              {"Id": "SOURCE_CAPTURE", "Severity": "LOGGER_SEVERITY_DEFAULT"},
              {"Id": "SOURCE_UNLOAD", "Severity": "LOGGER_SEVERITY_DEFAULT"}
            ]
          }
        }
```

### Terraform

```hcl
# Enable DMS source logging at minimum DEFAULT severity
resource "aws_dms_replication_task" "<example_resource_name>" {
  replication_instance_arn = "<example_resource_arn>"
  source_endpoint_arn      = "<example_resource_arn>"
  target_endpoint_arn      = "<example_resource_arn>"
  migration_type           = "full-load"
  table_mappings           = "{\"rules\":[]}"

  # Critical: Enables logging and sets SOURCE components to at least DEFAULT
  replication_task_settings = <<JSON
{
  "Logging": {
    "EnableLogging": true,
    "LogComponents": [
      {"Id": "SOURCE_CAPTURE", "Severity": "LOGGER_SEVERITY_DEFAULT"},
      {"Id": "SOURCE_UNLOAD", "Severity": "LOGGER_SEVERITY_DEFAULT"}
    ]
  }
}
JSON
}
```

### Other

1. In the AWS console, go to Database Migration Service > Database migration tasks
2. Select the task and choose Modify
3. Click Modify task logging
4. Turn on Enable logging
5. For SOURCE_CAPTURE and SOURCE_UNLOAD, set Severity to Default (or higher)
6. Save/Modify to apply

## 参考資料

- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html)
- [https://repost.aws/knowledge-center/dms-debug-logging](https://repost.aws/knowledge-center/dms-debug-logging)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-8](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-8)

## 技術情報

- Source Metadata：[sources/aws/dms_replication_task_source_logging_enabled/metadata.json](../../sources/aws/dms_replication_task_source_logging_enabled/metadata.json)
- Source Code：[sources/aws/dms_replication_task_source_logging_enabled/check.py](../../sources/aws/dms_replication_task_source_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_replication_task_source_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_replication_task_source_logging_enabled/check.py`

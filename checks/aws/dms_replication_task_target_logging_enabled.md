# DMS replication task has TARGET_APPLY and TARGET_LOAD logging enabled with at least default severity

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_replication_task_target_logging_enabled` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, TTPs/Defense Evasion |
| 资源类型 | AwsDmsReplicationTask |
| 资源组 | database |

## 描述

**AWS DMS replication tasks** have target logging enabled, including `TARGET_APPLY` and `TARGET_LOAD`, each set to at least `LOGGER_SEVERITY_DEFAULT`.

## 风险

Insufficient target logging limits visibility into load/apply activity, masking failures and anomalies. This risks **data integrity** (silent drift, partial loads) and **availability** (longer incident resolution), and reduces **auditability** of migration events.

## 推荐措施

Enable and maintain **CloudWatch logging** at `LOGGER_SEVERITY_DEFAULT` or higher for target components: - Configure `TARGET_APPLY` and `TARGET_LOAD` - Enforce least-privilege log access - Monitor logs/alerts for anomalies - Standardize task settings and validate data for **defense in depth**

## 修复步骤


### CLI

```text
aws dms modify-replication-task --replication-task-arn <task-arn> --replication-task-settings '{"Logging":{"EnableLogging":true,"LogComponents":[{"Id":"TARGET_APPLY","Severity":"LOGGER_SEVERITY_DEFAULT"},{"Id":"TARGET_LOAD","Severity":"LOGGER_SEVERITY_DEFAULT"}]}}'
```

### Native IaC

```yaml
# CloudFormation: enable DMS task logging for target components
Resources:
  <example_resource_name>:
    Type: AWS::DMS::ReplicationTask
    Properties:
      ReplicationInstanceArn: <example_resource_arn>
      SourceEndpointArn: <example_resource_arn>
      TargetEndpointArn: <example_resource_arn>
      MigrationType: full-load
      TableMappings: |
        {"rules":[{"rule-type":"selection","rule-id":"1","rule-name":"1","object-locator":{"schema-name":"%","table-name":"%"},"rule-action":"include"}]}
      ReplicationTaskSettings: |
        {"Logging":{"EnableLogging":true, "LogComponents":[
          {"Id":"TARGET_APPLY","Severity":"LOGGER_SEVERITY_DEFAULT"},  # Critical: ensure TARGET_APPLY logging at default
          {"Id":"TARGET_LOAD","Severity":"LOGGER_SEVERITY_DEFAULT"}    # Critical: ensure TARGET_LOAD logging at default
        ]}}
```

### Terraform

```hcl
# Enable DMS task logging for target components
resource "aws_dms_replication_task" "<example_resource_name>" {
  replication_task_id      = "<example_resource_id>"
  replication_instance_arn = "<example_resource_arn>"
  source_endpoint_arn      = "<example_resource_arn>"
  target_endpoint_arn      = "<example_resource_arn>"
  migration_type           = "full-load"
  table_mappings           = jsonencode({ rules = [{
    "rule-type" : "selection", "rule-id" : "1", "rule-name" : "1",
    "object-locator" : { "schema-name" : "%", "table-name" : "%" },
    "rule-action" : "include"
  }]} )

  # Critical: enables logging and sets TARGET_APPLY and TARGET_LOAD to minimum required severity
  replication_task_settings = jsonencode({
    Logging = {
      EnableLogging = true
      LogComponents = [
        { Id = "TARGET_APPLY", Severity = "LOGGER_SEVERITY_DEFAULT" },
        { Id = "TARGET_LOAD",  Severity = "LOGGER_SEVERITY_DEFAULT" }
      ]
    }
  })
}
```

### Other

1. Open the AWS DMS console and go to Database migration tasks
2. Select the replication task and choose Modify
3. Expand Task settings (JSON) or Logging
4. Enable CloudWatch logs (EnableLogging = true)
5. Set log components:
   - TARGET_APPLY severity: DEFAULT
   - TARGET_LOAD severity: DEFAULT
6. Save changes (Modify task), then rerun the task if required

## 参考资料

- [https://repost.aws/knowledge-center/dms-debug-logging](https://repost.aws/knowledge-center/dms-debug-logging)
- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.Logging.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.Logging.html)
- [https://stackoverflow.com/questions/46913913/aws-dms-with-cloudformation-enabling-logging-needs-a-log-group](https://stackoverflow.com/questions/46913913/aws-dms-with-cloudformation-enabling-logging-needs-a-log-group)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-7](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-7)

## 技术信息

- Source Metadata：[sources/aws/dms_replication_task_target_logging_enabled/metadata.json](../../sources/aws/dms_replication_task_target_logging_enabled/metadata.json)
- Source Code：[sources/aws/dms_replication_task_target_logging_enabled/check.py](../../sources/aws/dms_replication_task_target_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_replication_task_target_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_replication_task_target_logging_enabled/check.py`

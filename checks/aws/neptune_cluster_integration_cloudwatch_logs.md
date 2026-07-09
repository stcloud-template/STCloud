# Neptune cluster has CloudWatch audit logs enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `neptune_cluster_integration_cloudwatch_logs` |
| 云平台 | AWS |
| 服务 | neptune |
| 严重等级 | medium |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | database |

## 描述

Neptune DB cluster is inspected for CloudWatch export of **audit** events. The finding indicates whether the cluster publishes `audit` logs to CloudWatch; a failed status in the report means the `audit` export is not enabled and audit records are not being forwarded to CloudWatch for centralized logging and review.

## 风险

Missing **audit logs** reduces **detectability** and **accountability**: - Investigators cannot reconstruct queries, client origins, or timeline - Unauthorized queries, data exfiltration, or privilege misuse may go undetected This degrades confidentiality and integrity and slows incident response.

## 推荐措施

Enable and centralize **audit logging** for Neptune by exporting `audit` events to CloudWatch Logs and integrating with monitoring or SIEM. - Enforce **least privilege** on log access - Configure retention, encryption, and alerting for anomalous queries This supports proactive detection and forensic readiness.

## 修复步骤


### CLI

```text
aws neptune modify-db-cluster --db-cluster-identifier <DB_CLUSTER_IDENTIFIER> --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'
```

### Native IaC

```yaml
Resources:
  NeptuneCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBClusterIdentifier: "<DB_CLUSTER_IDENTIFIER>"
      EnableCloudwatchLogsExports:
        - audit  # Export audit logs to CloudWatch for monitoring and forensics
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier               = "<db_cluster_identifier>"
  enabled_cloudwatch_logs_exports = ["audit"]  # Export audit logs to CloudWatch for monitoring and forensics
}
```

### Other

1. Sign in to the AWS Management Console and open Amazon Neptune
2. Go to Databases and select the Neptune DB cluster
3. Actions > Modify
4. In Log exports, check "Audit"
5. Continue > Modify DB Cluster

## 参考资料

- [https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html](https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html)
- [https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html)
- [https://cloudanix.com/docs/aws/audit/rdsmonitoring/rules/neptune_cluster_cloudwatch_log_export_enabled_remediation](https://cloudanix.com/docs/aws/audit/rdsmonitoring/rules/neptune_cluster_cloudwatch_log_export_enabled_remediation)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-2](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-2)

## 技术信息

- Source Metadata：[sources/aws/neptune_cluster_integration_cloudwatch_logs/metadata.json](../../sources/aws/neptune_cluster_integration_cloudwatch_logs/metadata.json)
- Source Code：[sources/aws/neptune_cluster_integration_cloudwatch_logs/check.py](../../sources/aws/neptune_cluster_integration_cloudwatch_logs/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_integration_cloudwatch_logs/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_integration_cloudwatch_logs/check.py`

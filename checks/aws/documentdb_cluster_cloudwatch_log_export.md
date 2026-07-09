# DocumentDB cluster exports audit and profiler logs to CloudWatch Logs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `documentdb_cluster_cloudwatch_log_export` |
| 云平台 | AWS |
| 服务 | documentdb |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Amazon DocumentDB clusters are evaluated for exporting `audit` and `profiler` logs to **CloudWatch Logs**. Clusters missing one or both log types are identified as lacking complete log export configuration.

## 风险

Missing **audit** and/or **profiler** exports reduces observability of authentication, authorization, and data definition activity. Attacks like brute-force logins, privilege abuse, or destructive schema changes can go unnoticed, degrading **confidentiality** and **integrity** and delaying incident response.

## 推荐措施

Enable export of both `audit` and `profiler` logs to **CloudWatch Logs** for all clusters and centralize analysis. Apply **least privilege** to log access, define retention and immutability, integrate with alerting, and use **separation of duties** to protect and regularly review logs for **defense in depth**.

## 修复步骤


### CLI

```text
aws docdb modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit","profiler"]}' --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable DocumentDB log exports
Resources:
  <example_resource_name>:
    Type: AWS::DocDB::DBCluster
    Properties:
      EnableCloudwatchLogsExports:
        - audit      # Critical: export audit logs to CloudWatch Logs
        - profiler   # Critical: export profiler logs to CloudWatch Logs
```

### Terraform

```hcl
# Enable DocumentDB log exports
resource "aws_docdb_cluster" "<example_resource_name>" {
  enabled_cloudwatch_logs_exports = ["audit", "profiler"] # Critical: export both logs to CloudWatch Logs
}
```

### Other

1. In AWS Console, go to Amazon DocumentDB > Clusters
2. Select the cluster and choose Actions > Modify
3. In Log exports, check Audit and Profiler
4. Check Apply immediately and click Modify cluster

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-4](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-4)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DocumentDB/enable-profiler.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DocumentDB/enable-profiler.html)
- [https://docs.aws.amazon.com/cli/latest/reference/docdb/create-db-cluster.html](https://docs.aws.amazon.com/cli/latest/reference/docdb/create-db-cluster.html)

## 技术信息

- Source Metadata：[sources/aws/documentdb_cluster_cloudwatch_log_export/metadata.json](../../sources/aws/documentdb_cluster_cloudwatch_log_export/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_cloudwatch_log_export/check.py](../../sources/aws/documentdb_cluster_cloudwatch_log_export/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_cloudwatch_log_export/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_cloudwatch_log_export/check.py`

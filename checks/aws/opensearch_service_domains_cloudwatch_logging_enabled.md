# Amazon OpenSearch Service domain publishes search and index slow logs to CloudWatch Logs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_cloudwatch_logging_enabled` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | low |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch Service** domains have **slow log publishing** enabled for both **search** and **indexing** operations to CloudWatch Logs (`SEARCH_SLOW_LOGS` and `INDEX_SLOW_LOGS`).

## 风险

Without these logs, visibility into **expensive searches** and **slow indexing** is lost, masking hotspots and abuse. - Availability: timeouts, throttling, node pressure - Integrity: missed or delayed indexing - Operations: slower incident response and capacity planning

## 推荐措施

Enable both `SEARCH_SLOW_LOGS` and `INDEX_SLOW_LOGS` for all domains and publish to CloudWatch. Set meaningful thresholds and retention, separate log groups, and alert on anomalies. Apply **least privilege** to log access and use **defense in depth** with complementary error and audit logs.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <DOMAIN_NAME> --log-publishing-options "SEARCH_SLOW_LOGS={CloudWatchLogsLogGroupArn=<LOG_GROUP_ARN>,Enabled=true},INDEX_SLOW_LOGS={CloudWatchLogsLogGroupArn=<LOG_GROUP_ARN>,Enabled=true}"
```

### Native IaC

```yaml
# CloudFormation: enable OpenSearch search and index slow logs to CloudWatch
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      LogPublishingOptions:
        SEARCH_SLOW_LOGS:
          CloudWatchLogsLogGroupArn: <LOG_GROUP_ARN>
          Enabled: true  # Critical: enables SEARCH_SLOW_LOGS publishing
        INDEX_SLOW_LOGS:
          CloudWatchLogsLogGroupArn: <LOG_GROUP_ARN>
          Enabled: true  # Critical: enables INDEX_SLOW_LOGS publishing
```

### Terraform

```hcl
# Enable OpenSearch search and index slow logs to CloudWatch
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  # Critical: enables SEARCH_SLOW_LOGS publishing
  log_publishing_options {
    log_type                 = "SEARCH_SLOW_LOGS"
    cloudwatch_log_group_arn = "<LOG_GROUP_ARN>"
    enabled                  = true
  }

  # Critical: enables INDEX_SLOW_LOGS publishing
  log_publishing_options {
    log_type                 = "INDEX_SLOW_LOGS"
    cloudwatch_log_group_arn = "<LOG_GROUP_ARN>"
    enabled                  = true
  }
}
```

### Other

1. In the AWS Console, open Amazon OpenSearch Service and select your domain
2. Go to the Logs tab
3. For Search slow logs, click Enable, choose or create a CloudWatch log group, accept/attach the suggested resource policy, then Save
4. For Index slow logs, click Enable, choose or create a CloudWatch log group, accept/attach the suggested resource policy, then Save
5. Wait for domain status to return to Active

## 参考资料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createdomain-configure-slow-logs.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createdomain-configure-slow-logs.html)
- [https://support.icompaas.com/support/solutions/articles/62000129471-ensure-amazon-elasticsearch-service-es-domains-have-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000129471-ensure-amazon-elasticsearch-service-es-domains-have-logging-enabled)
- [https://bigdataboutique.com/blog/inspecting-search-slow-logs-on-elasticsearch-and-opensearch-b05d87](https://bigdataboutique.com/blog/inspecting-search-slow-logs-on-elasticsearch-and-opensearch-b05d87)
- [https://repost.aws/knowledge-center/opensearch-troubleshoot-slow-logs](https://repost.aws/knowledge-center/opensearch-troubleshoot-slow-logs)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/slow-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/slow-logs.html)
- [https://medium.com/heyjobs-tech/how-to-create-an-opensearch-cluster-using-terraform-926b4a62b489](https://medium.com/heyjobs-tech/how-to-create-an-opensearch-cluster-using-terraform-926b4a62b489)
- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/metadata.json](../../sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/check.py](../../sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_cloudwatch_logging_enabled/check.py`

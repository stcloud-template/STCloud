# Amazon OpenSearch Service domain has audit logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_audit_logging_enabled` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | high |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch Service domains** have **audit logs** enabled via `AUDIT_LOGS`

## 风险

Without audit logs, critical actions lack accountability, reducing **confidentiality** and **integrity**. Unauthorized access, privilege misuse, and index tampering can go **undetected**, hindering **incident response** and **forensics**, and enabling data exfiltration and lateral movement without traceability.

## 推荐措施

Enable `AUDIT_LOGS` for all domains and route them to a centralized, durable log store. Tune categories to record auth failures and sensitive index operations. Apply **least privilege** to log access, enforce retention and immutability, and integrate alerts to provide **defense in depth** and timely response.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <example_resource_name> --log-publishing-options "AUDIT_LOGS={CloudWatchLogsLogGroupArn=<CLOUDWATCH_LOG_GROUP_ARN>,Enabled=true}"
```

### Native IaC

```yaml
# CloudFormation: Enable AUDIT_LOGS for an OpenSearch domain
Resources:
  OpenSearchDomain:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      LogPublishingOptions:
        AUDIT_LOGS:
          CloudWatchLogsLogGroupArn: <CLOUDWATCH_LOG_GROUP_ARN>  # Critical: where audit logs are sent
          Enabled: true  # Critical: turns on AUDIT_LOGS to pass the check
```

### Terraform

```hcl
# Enable AUDIT_LOGS for an OpenSearch domain
resource "aws_opensearch_domain" "example" {
  domain_name = "<example_resource_name>"

  log_publishing_options {
    log_type                 = "AUDIT_LOGS"
    cloudwatch_log_group_arn = "<CLOUDWATCH_LOG_GROUP_ARN>"  # Critical: destination for audit logs
    enabled                  = true                           # Critical: turns on AUDIT_LOGS to pass the check
  }
}
```

### Other

1. Open the AWS console and go to OpenSearch Service
2. Select the domain <example_resource_name>
3. Open the Logs tab, find Audit logs, and click Enable
4. Choose or create a CloudWatch log group and confirm the resource policy if prompted
5. Click Save changes to enable AUDIT_LOGS
6. If Fine-grained access control is not enabled, enable it first, then repeat steps 3-5

## 参考资料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/audit-logs.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/audit-logs.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_audit_logging_enabled/metadata.json](../../sources/aws/opensearch_service_domains_audit_logging_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_audit_logging_enabled/check.py](../../sources/aws/opensearch_service_domains_audit_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_audit_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_audit_logging_enabled/check.py`

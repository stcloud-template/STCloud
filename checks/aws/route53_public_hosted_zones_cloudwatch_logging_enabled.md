# Route53 public hosted zone has query logging enabled to a CloudWatch Logs log group

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `route53_public_hosted_zones_cloudwatch_logging_enabled` |
| 云平台 | AWS |
| 服务 | route53 |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRoute53HostedZone |
| 资源组 | network |

## 描述

**Route 53 public hosted zones** have **DNS query logging** enabled to **CloudWatch Logs**, recording resolver requests for the zone and writing events to an associated log group.

## 风险

Missing **DNS query logs** removes visibility into domain use, weakening detection of: - **Data exfiltration** via DNS - **Malware C2/DGA** patterns - **Hijacking or misconfigurations** This degrades **incident response**, threatens data **confidentiality** and **integrity**, and slows **availability** troubleshooting.

## 推荐措施

Enable **Route 53 query logging** for public zones to a centralized **CloudWatch Logs** group. Apply **least privilege** to log delivery, set **retention** and **metric filters/alerts**, and stream to your **SIEM**. Use **defense in depth** by correlating DNS logs with network and endpoint telemetry and regularly review baselines.

## 修复步骤


### CLI

```text
aws route53 create-query-logging-config --hosted-zone-id <HOSTED_ZONE_ID> --cloud-watch-logs-log-group-arn <LOG_GROUP_ARN>
```

### Native IaC

```yaml
# CloudFormation: Enable query logging for a public hosted zone
Resources:
  <example_resource_name>:
    Type: AWS::Route53::HostedZone
    Properties:
      Name: <example_domain_name>
      QueryLoggingConfig:
        CloudWatchLogsLogGroupArn: <example_log_group_arn>  # Critical: enables Route53 query logging to this CloudWatch Logs group
```

### Terraform

```hcl
# Enable Route53 query logging for a public hosted zone
resource "aws_route53_query_log" "example" {
  zone_id                   = "<example_resource_id>"        # Critical: target hosted zone
  cloudwatch_log_group_arn  = "<example_log_group_arn>"      # Critical: delivers logs to this CloudWatch Logs group
}
```

### Other

1. Open the AWS Console and go to Route 53 > Hosted zones
2. Select the public hosted zone
3. Choose Query logging > Enable
4. Select the target CloudWatch Logs log group and click Save
5. If prompted, allow Route 53 to write to the log group (approve the CloudWatch Logs resource policy)

## 参考资料

- [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-hosted-zones-with-cloudwatch.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-hosted-zones-with-cloudwatch.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/enable-query-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/enable-query-logging.html)

## 技术信息

- Source Metadata：[sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/metadata.json](../../sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/metadata.json)
- Source Code：[sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/check.py](../../sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/route53_public_hosted_zones_cloudwatch_logging_enabled/check.py`

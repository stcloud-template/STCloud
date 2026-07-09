# ECS cluster has Container Insights enabled or enhanced

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ecs_cluster_container_insights_enabled` |
| 云平台 | AWS |
| 服务 | ecs |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| 资源类型 | AwsEcsCluster |
| 资源组 | container |

## 描述

**ECS clusters** have CloudWatch **Container Insights** configured via the `containerInsights` setting, accepting `enabled` or `enhanced` values to emit cluster, service, task, and container telemetry.

## 风险

Without **Container Insights**, ECS operations lack **telemetry** to spot failures and anomalies. Missed CPU/memory/network spikes and restart loops degrade **availability** and delay response. Absent baselines impede detecting abuse (e.g., **cryptomining** or data egress bursts), risking **confidentiality** and unexpected **costs**.

## 推荐措施

Enable **Container Insights** on all clusters-prefer `enhanced` for deeper visibility. Apply at account level for new clusters and enforce via automation. Use **least privilege** for access to metrics/logs, encrypt logs, and set **alarms** on critical metrics. Correlate with app logs and tracing for **defense in depth** and faster incident detection.

## 修复步骤


### CLI

```text
aws ecs update-cluster-settings --cluster <cluster-name> --settings name=containerInsights,value=enabled
```

### Native IaC

```yaml
# CloudFormation: Enable Container Insights on an ECS cluster
Resources:
  <example_resource_name>:
    Type: AWS::ECS::Cluster
    Properties:
      ClusterSettings:
        - Name: containerInsights  # Critical: enables CloudWatch Container Insights for the cluster
          Value: enabled           # Critical: setting that passes the check
```

### Terraform

```hcl
# Terraform: Enable Container Insights on an ECS cluster
resource "aws_ecs_cluster" "<example_resource_name>" {
  name = "<example_resource_name>"

  setting {
    name  = "containerInsights"   # Critical: enables CloudWatch Container Insights for the cluster
    value = "enabled"             # Critical: setting that passes the check
  }
}
```

### Other

1. Open the Amazon ECS console
2. Go to Clusters and select the target cluster
3. Click Update cluster
4. Under CloudWatch Container Insights, enable Container Insights (or Enhanced)
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-12](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-12)
- [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/ecs-container-insights-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ecs-container-insights-enabled.html)
- [https://aws.amazon.com/blogs/aws/container-insights-with-enhanced-observability-now-available-in-amazon-ecs/](https://aws.amazon.com/blogs/aws/container-insights-with-enhanced-observability-now-available-in-amazon-ecs/)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)

## 技术信息

- Source Metadata：[sources/aws/ecs_cluster_container_insights_enabled/metadata.json](../../sources/aws/ecs_cluster_container_insights_enabled/metadata.json)
- Source Code：[sources/aws/ecs_cluster_container_insights_enabled/check.py](../../sources/aws/ecs_cluster_container_insights_enabled/check.py)
- Source Metadata Path：`sources/aws/ecs_cluster_container_insights_enabled/metadata.json`
- Source Code Path：`sources/aws/ecs_cluster_container_insights_enabled/check.py`

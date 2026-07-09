# Ensure Logging is enabled for HTTP(S) Load Balancer

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_loadbalancer_logging_enabled` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | LoadBalancer |
| 资源组 | network |

## 描述

Logging enabled on a HTTPS Load Balancer will show all network traffic and its destination.

## 风险

HTTP(S) load balancing log entries contain information useful for monitoring and debugging web traffic. Google Cloud exports this logging data to Cloud Monitoring service so that monitoring metrics can be created to evaluate a load balancer's configuration, usage, and performance, troubleshoot problems, and improve resource utilization and user experience.

## 推荐措施

Logging will allow you to view HTTPS network traffic to your web applications.

- 推荐链接：[https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode)

## 修复步骤


### CLI

```text
gcloud compute backend-services update <serviceName> --region=REGION --enable-logging --logging-sample-rate=<percentageAsADecimal>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLoadBalancing/enableLoad-balancing-backend-service-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLoadBalancing/enableLoad-balancing-backend-service-logging.html)

## 参考资料

- [https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode)

## 技术信息

- Source Metadata：[sources/gcp/compute_loadbalancer_logging_enabled/metadata.json](../../sources/gcp/compute_loadbalancer_logging_enabled/metadata.json)
- Source Code：[sources/gcp/compute_loadbalancer_logging_enabled/check.py](../../sources/gcp/compute_loadbalancer_logging_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_loadbalancer_logging_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_loadbalancer_logging_enabled/check.py`

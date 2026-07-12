# Ensure Logging is enabled for HTTP(S) Load Balancer

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_loadbalancer_logging_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | LoadBalancer |
| リソースグループ | network |

## 説明

Logging enabled on a HTTPS Load Balancer will show all network traffic and its destination.

## リスク

HTTP(S) load balancing log entries contain information useful for monitoring and debugging web traffic. Google Cloud exports this logging data to Cloud Monitoring service so that monitoring metrics can be created to evaluate a load balancer's configuration, usage, and performance, troubleshoot problems, and improve resource utilization and user experience.

## 推奨事項

Logging will allow you to view HTTPS network traffic to your web applications.

- 推奨リンク：[https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode)

## 修正手順


### CLI

```text
gcloud compute backend-services update <serviceName> --region=REGION --enable-logging --logging-sample-rate=<percentageAsADecimal>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLoadBalancing/enableLoad-balancing-backend-service-logging.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLoadBalancing/enableLoad-balancing-backend-service-logging.html)

## 参考資料

- [https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#gcloud:-global-mode)

## 技術情報

- Source Metadata：[sources/gcp/compute_loadbalancer_logging_enabled/metadata.json](../../sources/gcp/compute_loadbalancer_logging_enabled/metadata.json)
- Source Code：[sources/gcp/compute_loadbalancer_logging_enabled/check.py](../../sources/gcp/compute_loadbalancer_logging_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_loadbalancer_logging_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_loadbalancer_logging_enabled/check.py`

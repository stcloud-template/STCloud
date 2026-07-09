# Amazon OpenSearch Service domain is updated to the latest service software version

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_updated_to_the_latest_service_software_version` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | high |
| 类别 | vulnerabilities |
| 检查类型 | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**OpenSearch Service domains** are assessed for pending **service software updates**. This focuses on internal platform updates, distinct from engine version upgrades.

## 风险

**Missing service software updates** can leave known flaws unpatched, threatening data confidentiality and index integrity. Required updates missed may lead to AWS isolating the domain, causing **outages** and, if prolonged, **permanent deletion**.

## 推荐措施

Apply the latest **service software updates** promptly. Schedule updates during the domain's **off-peak window** or enable automatic updates. Monitor console or **EventBridge** notifications, and test changes in staging to support **defense in depth** while minimizing downtime.

## 修复步骤


### CLI

```text
aws opensearch start-service-software-update --domain-name <DOMAIN_NAME>
```

### Other

1. Sign in to the AWS Console and open Amazon OpenSearch Service
2. Select the target domain
3. Click Actions > Update
4. Choose Apply update now
5. Click Confirm to start the service software update

## 参考资料

- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/version.html)
- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-service-software.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-service-software.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/metadata.json](../../sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/check.py](../../sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_updated_to_the_latest_service_software_version/check.py`

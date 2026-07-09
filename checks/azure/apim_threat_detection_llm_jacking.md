# Ensure Azure API Management is protected against LLM Jacking attacks

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apim_threat_detection_llm_jacking` |
| 云平台 | Azure |
| 服务 | apim |
| 严重等级 | high |
| 类别 | threat-detection, monitoring, logging |
| 资源类型 | Azure API Management Instance |
| 资源组 | api_gateway |

## 描述

This check analyzes Azure API Management diagnostic logs in Log Analytics to detect potential LLM Jacking attacks by monitoring the frequency of LLM-related operations (ImageGenerations_Create, ChatCompletions_Create, Completions_Create) from individual IP addresses within a configurable time window.

## 风险

LLM Jacking attacks can lead to unauthorized access to AI models, potential data exfiltration, increased costs, and abuse of AI services. Attackers may use these endpoints to generate content, bypass rate limits, or access premium AI capabilities without proper authorization.

## 推荐措施

To protect against LLM Jacking attacks: 1. Enable diagnostic logging for APIM instances and send logs to Log Analytics workspace 2. Configure appropriate thresholds for LLM operation frequency monitoring 3. Set up alerts for suspicious activity patterns 4. Implement rate limiting and IP allowlisting for sensitive AI endpoints 5. Regularly review and analyze APIM access logs for anomalies

- 推荐链接：[https://learn.microsoft.com/en-us/azure/api-management/monitor-api-management](https://learn.microsoft.com/en-us/azure/api-management/monitor-api-management)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/api-management/monitor-api-management](https://learn.microsoft.com/en-us/azure/api-management/monitor-api-management)

## 技术信息

- Source Metadata：[sources/azure/apim_threat_detection_llm_jacking/metadata.json](../../sources/azure/apim_threat_detection_llm_jacking/metadata.json)
- Source Code：[sources/azure/apim_threat_detection_llm_jacking/check.py](../../sources/azure/apim_threat_detection_llm_jacking/check.py)
- Source Metadata Path：`sources/azure/apim_threat_detection_llm_jacking/metadata.json`
- Source Code Path：`sources/azure/apim_threat_detection_llm_jacking/check.py`

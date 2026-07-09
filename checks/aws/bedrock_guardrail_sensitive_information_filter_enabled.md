# Configure Sensitive Information Filters for Amazon Bedrock Guardrails.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_guardrail_sensitive_information_filter_enabled` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | high |
| 类别 | gen-ai |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

Ensure that sensitive information filters are enabled for Amazon Bedrock guardrails to prevent the leakage of sensitive data such as personally identifiable information (PII), financial data, or confidential corporate information.

## 风险

If sensitive information filters are not enabled, Bedrock models may inadvertently generate or expose confidential or sensitive information in responses, leading to data breaches, regulatory violations, or reputational damage.

## 推荐措施

Enable sensitive information filters for Amazon Bedrock guardrails to prevent the exposure of sensitive or confidential information.

- 推荐链接：[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

## 修复步骤


### CLI

```text
aws bedrock put-guardrails-configuration --guardrails-config 'sensitiveInformationFilter=true'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/guardrails-with-pii-mask-block.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/guardrails-with-pii-mask-block.html)

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

## 技术信息

- Source Metadata：[sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json](../../sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py](../../sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py`

# Ensure that Guardrails are enabled for Amazon Bedrock agent sessions.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_agent_guardrail_enabled` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | high |
| 类别 | gen-ai |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

This check ensures that Guardrails are enabled to protect Amazon Bedrock agent sessions. Guardrails help mitigate security risks by filtering and blocking harmful or sensitive content during interactions with AI models.

## 风险

Without guardrails enabled, Amazon Bedrock agent sessions are vulnerable to harmful prompts or inputs that could expose sensitive information or generate inappropriate content. This could lead to privacy violations, data leaks, or other security risks.

## 推荐措施

Enable Guardrails for Amazon Bedrock agent sessions to protect against harmful inputs and outputs during interactions.

- 推荐链接：[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/protect-agent-sessions-with-guardrails.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/protect-agent-sessions-with-guardrails.html)

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html)

## 技术信息

- Source Metadata：[sources/aws/bedrock_agent_guardrail_enabled/metadata.json](../../sources/aws/bedrock_agent_guardrail_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_agent_guardrail_enabled/check.py](../../sources/aws/bedrock_agent_guardrail_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_agent_guardrail_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_agent_guardrail_enabled/check.py`

# Configure Prompt Attack Filter with the highest strength for Amazon Bedrock Guardrails.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_guardrail_prompt_attack_filter_enabled` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | high |
| 类别 | gen-ai |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

Ensure that prompt attack filter strength is set to HIGH for Amazon Bedrock guardrails to mitigate prompt injection and bypass techniques.

## 风险

If prompt attack filter strength is not set to HIGH, Bedrock models may be more vulnerable to prompt injection attacks or jailbreak attempts, which could allow harmful or sensitive content to bypass filters and reach end users.

## 推荐措施

Set the prompt attack filter strength to HIGH for Amazon Bedrock guardrails to prevent prompt injection attacks and ensure robust protection against content manipulation.

- 推荐链接：[https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html)

## 修复步骤


### CLI

```text
aws bedrock put-guardrails-configuration --guardrails-config 'promptAttackStrength=HIGH'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/prompt-attack-strength.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/prompt-attack-strength.html)

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html)

## 技术信息

- Source Metadata：[sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json](../../sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py](../../sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py`

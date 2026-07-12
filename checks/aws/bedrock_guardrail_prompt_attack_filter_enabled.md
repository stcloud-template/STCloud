# Configure Prompt Attack Filter with the highest strength for Amazon Bedrock Guardrails.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bedrock_guardrail_prompt_attack_filter_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | bedrock |
| 重大度 | high |
| カテゴリ | gen-ai |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

Ensure that prompt attack filter strength is set to HIGH for Amazon Bedrock guardrails to mitigate prompt injection and bypass techniques.

## リスク

If prompt attack filter strength is not set to HIGH, Bedrock models may be more vulnerable to prompt injection attacks or jailbreak attempts, which could allow harmful or sensitive content to bypass filters and reach end users.

## 推奨事項

Set the prompt attack filter strength to HIGH for Amazon Bedrock guardrails to prevent prompt injection attacks and ensure robust protection against content manipulation.

- 推奨リンク：[https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html)

## 修正手順


### CLI

```text
aws bedrock put-guardrails-configuration --guardrails-config 'promptAttackStrength=HIGH'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/prompt-attack-strength.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/prompt-attack-strength.html)

## 参考資料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html)

## 技術情報

- Source Metadata：[sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json](../../sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py](../../sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_guardrail_prompt_attack_filter_enabled/check.py`

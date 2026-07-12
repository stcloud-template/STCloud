# Ensure that Guardrails are enabled for Amazon Bedrock agent sessions.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bedrock_agent_guardrail_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | bedrock |
| 重大度 | high |
| カテゴリ | gen-ai |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

This check ensures that Guardrails are enabled to protect Amazon Bedrock agent sessions. Guardrails help mitigate security risks by filtering and blocking harmful or sensitive content during interactions with AI models.

## リスク

Without guardrails enabled, Amazon Bedrock agent sessions are vulnerable to harmful prompts or inputs that could expose sensitive information or generate inappropriate content. This could lead to privacy violations, data leaks, or other security risks.

## 推奨事項

Enable Guardrails for Amazon Bedrock agent sessions to protect against harmful inputs and outputs during interactions.

- 推奨リンク：[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/protect-agent-sessions-with-guardrails.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/protect-agent-sessions-with-guardrails.html)

## 参考資料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html)

## 技術情報

- Source Metadata：[sources/aws/bedrock_agent_guardrail_enabled/metadata.json](../../sources/aws/bedrock_agent_guardrail_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_agent_guardrail_enabled/check.py](../../sources/aws/bedrock_agent_guardrail_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_agent_guardrail_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_agent_guardrail_enabled/check.py`

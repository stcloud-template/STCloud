# Configure Sensitive Information Filters for Amazon Bedrock Guardrails.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bedrock_guardrail_sensitive_information_filter_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | bedrock |
| 重大度 | high |
| カテゴリ | gen-ai |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

Ensure that sensitive information filters are enabled for Amazon Bedrock guardrails to prevent the leakage of sensitive data such as personally identifiable information (PII), financial data, or confidential corporate information.

## リスク

If sensitive information filters are not enabled, Bedrock models may inadvertently generate or expose confidential or sensitive information in responses, leading to data breaches, regulatory violations, or reputational damage.

## 推奨事項

Enable sensitive information filters for Amazon Bedrock guardrails to prevent the exposure of sensitive or confidential information.

- 推奨リンク：[https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

## 修正手順


### CLI

```text
aws bedrock put-guardrails-configuration --guardrails-config 'sensitiveInformationFilter=true'
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/guardrails-with-pii-mask-block.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Bedrock/guardrails-with-pii-mask-block.html)

## 参考資料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

## 技術情報

- Source Metadata：[sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json](../../sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py](../../sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_guardrail_sensitive_information_filter_enabled/check.py`

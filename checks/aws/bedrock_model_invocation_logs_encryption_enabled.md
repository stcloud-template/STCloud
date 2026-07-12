# Ensure that Amazon Bedrock model invocation logs are encrypted with KMS.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bedrock_model_invocation_logs_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | bedrock |
| 重大度 | high |
| カテゴリ | encryption, logging, gen-ai |
| リソースタイプ | Other |
| リソースグループ | ai_ml |

## 説明

Ensure that Amazon Bedrock model invocation logs are encrypted using AWS KMS to protect sensitive data in the request and response logs for all model invocations.

## リスク

If Amazon Bedrock model invocation logs are not encrypted, sensitive data such as prompts, responses, and token usage could be exposed to unauthorized parties. This may lead to data breaches, security vulnerabilities, or unintended use of sensitive information.

## 推奨事項

Ensure that model invocation logs for Amazon Bedrock are encrypted using AWS KMS to prevent unauthorized access to sensitive log data.

- 推奨リンク：[hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

## 技術情報

- Source Metadata：[sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json](../../sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py](../../sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py`

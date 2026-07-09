# Ensure that Amazon Bedrock model invocation logs are encrypted with KMS.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_model_invocation_logs_encryption_enabled` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | high |
| 类别 | encryption, logging, gen-ai |
| 资源类型 | Other |
| 资源组 | ai_ml |

## 描述

Ensure that Amazon Bedrock model invocation logs are encrypted using AWS KMS to protect sensitive data in the request and response logs for all model invocations.

## 风险

If Amazon Bedrock model invocation logs are not encrypted, sensitive data such as prompts, responses, and token usage could be exposed to unauthorized parties. This may lead to data breaches, security vulnerabilities, or unintended use of sensitive information.

## 推荐措施

Ensure that model invocation logs for Amazon Bedrock are encrypted using AWS KMS to prevent unauthorized access to sensitive log data.

- 推荐链接：[hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)
- [hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html](hhttps://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

## 技术信息

- Source Metadata：[sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json](../../sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json)
- Source Code：[sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py](../../sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/bedrock_model_invocation_logs_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/bedrock_model_invocation_logs_encryption_enabled/check.py`

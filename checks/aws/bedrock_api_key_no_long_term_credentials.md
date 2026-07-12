# Ensure Amazon Bedrock API keys are not long-term credentials

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bedrock_api_key_no_long_term_credentials` |
| クラウドプラットフォーム | AWS |
| サービス | bedrock |
| 重大度 | high |
| カテゴリ | gen-ai, trust-boundaries |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards |
| リソースタイプ | AwsIamServiceSpecificCredential |
| リソースグループ | IAM |

## 説明

Ensure that Amazon Bedrock API keys have expiration dates set to prevent long-term credential exposure. Long-term credentials pose a significant security risk as they remain valid indefinitely and can be used for unauthorized access if compromised.

## リスク

Amazon Bedrock API keys without expiration dates are long-term credentials that remain valid indefinitely. This increases the risk of unauthorized access if the credentials are compromised, as they cannot be automatically invalidated. Long-term credentials violate the principle of credential rotation and can lead to security vulnerabilities, data breaches, or unauthorized usage of Bedrock services.

## 推奨事項

Delete the long-term API keys for Amazon Bedrock. Instead, use temporary credentials, IAM roles, or create new API keys with appropriate expiration dates. Implement a credential rotation policy to ensure all API keys have reasonable expiration periods. Consider using AWS STS for temporary credentials when possible.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials)

## 修正手順


### CLI

```text
aws iam delete-service-specific-credential --user-name <username> --service-specific-credential-id <credential-id>
```

## 参考資料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials)

## 技術情報

- Source Metadata：[sources/aws/bedrock_api_key_no_long_term_credentials/metadata.json](../../sources/aws/bedrock_api_key_no_long_term_credentials/metadata.json)
- Source Code：[sources/aws/bedrock_api_key_no_long_term_credentials/check.py](../../sources/aws/bedrock_api_key_no_long_term_credentials/check.py)
- Source Metadata Path：`sources/aws/bedrock_api_key_no_long_term_credentials/metadata.json`
- Source Code Path：`sources/aws/bedrock_api_key_no_long_term_credentials/check.py`

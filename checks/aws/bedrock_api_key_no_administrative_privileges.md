# Ensure Amazon Bedrock API keys do not have administrative privileges or privilege escalation

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bedrock_api_key_no_administrative_privileges` |
| 云平台 | AWS |
| 服务 | bedrock |
| 严重等级 | high |
| 类别 | gen-ai, trust-boundaries |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards |
| 资源类型 | AwsIamServiceSpecificCredential |
| 资源组 | IAM |

## 描述

Ensure that Amazon Bedrock API keys do not have administrative privileges or privilege escalation capabilities. API keys with administrative privileges can perform any action on any resource in your AWS environment, while privilege escalation allows users to grant themselves additional permissions, both posing significant security risks.

## 风险

Amazon Bedrock API keys with administrative privileges can perform any action on any resource in your AWS environment. Privilege escalation capabilities allow users to grant themselves additional permissions beyond their intended scope. Both violations of the principle of least privilege can lead to security vulnerabilities, data leaks, data loss, or unexpected charges if the API key is compromised or misused.

## 推荐措施

Apply the principle of least privilege to Amazon Bedrock API keys. Instead of granting administrative privileges or privilege escalation capabilities, assign only the permissions necessary for specific tasks. Create custom IAM policies with minimal permissions based on the principle of least privilege. Regularly review and audit API key permissions to ensure they cannot be used for privilege escalation.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 修复步骤


### CLI

```text
aws iam delete-service-specific-credential --user-name <username> --service-specific-credential-id <credential-id>
```

## 参考资料

- [https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)

## 技术信息

- Source Metadata：[sources/aws/bedrock_api_key_no_administrative_privileges/metadata.json](../../sources/aws/bedrock_api_key_no_administrative_privileges/metadata.json)
- Source Code：[sources/aws/bedrock_api_key_no_administrative_privileges/check.py](../../sources/aws/bedrock_api_key_no_administrative_privileges/check.py)
- Source Metadata Path：`sources/aws/bedrock_api_key_no_administrative_privileges/metadata.json`
- Source Code Path：`sources/aws/bedrock_api_key_no_administrative_privileges/check.py`

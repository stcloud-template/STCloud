# [DEPRECATED] AWS root user has security challenge questions configured

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `account_security_questions_are_registered_in_the_aws_account` |
| クラウドプラットフォーム | AWS |
| サービス | account |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

[DEPRECATED] **AWS account root** configuration may include legacy **security challenge questions** for support identity verification. This evaluates whether those questions are set on the account. *New configuration is discontinued by AWS and remaining support for this feature is time-limited.*

## リスク

Absence of these questions can limit support-assisted recovery if root credentials or MFA are lost, reducing **availability** and slowing **incident response**. Reliance on KBA also weakens **confidentiality** due to **social engineering**. Treat this as a recovery gap and adopt stronger, phishing-resistant factors.

## 推奨事項

Favor stronger recovery instead of KBA: - Enforce **MFA for root** and minimize root use - Keep **alternate contacts** and root email current and protected - Establish a tightly controlled **break-glass role**, applying least privilege and separation of duties - Document and test recovery procedures; monitor root activity

## 修正手順


### Other

1. Sign in to the AWS Management Console
2. Navigate to your AWS account settings page at https://console.aws.amazon.com/billing/home?#/account/
3. Scroll down to Configure Security Challenge Questions section and click the Edit link
4. Select three different questions made available by Amazon and provide appropriate answers
5. Store the answers in a secure but accessible location
6. Click the Update button to save the changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/security-challenge-questions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/security-challenge-questions.html)

## 技術情報

- Source Metadata：[sources/aws/account_security_questions_are_registered_in_the_aws_account/metadata.json](../../sources/aws/account_security_questions_are_registered_in_the_aws_account/metadata.json)
- Source Code：[sources/aws/account_security_questions_are_registered_in_the_aws_account/check.py](../../sources/aws/account_security_questions_are_registered_in_the_aws_account/check.py)
- Source Metadata Path：`sources/aws/account_security_questions_are_registered_in_the_aws_account/metadata.json`
- Source Code Path：`sources/aws/account_security_questions_are_registered_in_the_aws_account/check.py`

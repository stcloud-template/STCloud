# AWS account has distinct Security, Billing, and Operations contact details, different from each other and from the root contact

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `account_maintain_different_contact_details_to_security_billing_and_operations` |
| クラウドプラットフォーム | AWS |
| サービス | account |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS account alternate contacts** are defined for **Security**, **Billing**, and **Operations** with `name`, `email`, and `phone`. The finding evaluates that all three exist, are distinct from one another, and differ from the **primary (root) contact**.

## リスク

Missing or shared contacts can delay response to abuse alerts, credential compromise, or billing anomalies, reducing **availability** (possible AWS traffic throttling) and raising **confidentiality** and **integrity** risk through extended exposure. If AWS cannot reach you, urgent mitigation may disrupt service.

## 推奨事項

Maintain distinct, monitored **Security**, **Billing**, and **Operations** alternate contacts that differ from the root contact. - Use team aliases and 24x7 phones - Review and test contact paths regularly - Centralize at org level for consistency Applies **operational resilience** and **separation of duties**.

## 修正手順


### Terraform

```hcl
# Set distinct alternate contacts for SECURITY, BILLING, and OPERATIONS
# Critical: each resource sets a required contact type to satisfy the check

resource "aws_account_alternate_contact" "security" {
  alternate_contact_type = "SECURITY"  # Sets SECURITY contact
  email_address          = "security@example.com"
  name                   = "Security Team"
  phone_number           = "+1-555-0100"
  title                  = "Security"
}

resource "aws_account_alternate_contact" "billing" {
  alternate_contact_type = "BILLING"   # Sets BILLING contact
  email_address          = "billing@example.com"
  name                   = "Billing Team"
  phone_number           = "+1-555-0101"
  title                  = "Billing"
}

resource "aws_account_alternate_contact" "operations" {
  alternate_contact_type = "OPERATIONS" # Sets OPERATIONS contact
  email_address          = "operations@example.com"
  name                   = "Operations Team"
  phone_number           = "+1-555-0102"
  title                  = "Operations"
}
```

### Other

1. Sign in to the AWS Management Console with a user that can edit account contacts (root, or IAM with account:PutAlternateContact)
2. In the upper right, click your account name > Account
3. Scroll to "Alternate contacts" and click Edit
4. Add all three contacts with unique details:
   - Billing contact (distinct name, email, phone)
   - Operations contact (distinct name, email, phone)
   - Security contact (distinct name, email, phone)
5. Ensure each contact’s email/phone differs from each other and from the primary (root) contact, then click Update

## 参考資料

- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact)
- [https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html)
- [https://builder.aws.com/content/2qRw97fe8JFwfk2AbpJ3sYNpNvM/aws-bulk-update-alternate-contacts-across-organization](https://builder.aws.com/content/2qRw97fe8JFwfk2AbpJ3sYNpNvM/aws-bulk-update-alternate-contacts-across-organization)
- [https://github.com/aws-samples/aws-account-alternate-contact-with-terraform](https://github.com/aws-samples/aws-account-alternate-contact-with-terraform)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/account-security-alternate-contacts.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/IAM/account-security-alternate-contacts.html)
- [https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv](https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv)

## 技術情報

- Source Metadata：[sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/metadata.json](../../sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/metadata.json)
- Source Code：[sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/check.py](../../sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/check.py)
- Source Metadata Path：`sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/metadata.json`
- Source Code Path：`sources/aws/account_maintain_different_contact_details_to_security_billing_and_operations/check.py`

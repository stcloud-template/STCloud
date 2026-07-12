# AWS account contact information is current

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `account_maintain_current_contact_details` |
| クラウドプラットフォーム | AWS |
| サービス | account |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS account contact information** is current for the **primary contact** and the **alternate contacts** for `security`, `billing`, and `operations`, with accurate email addresses and phone numbers.

## リスク

Outdated or single-person contacts delay **security notifications**, slow **incident response**, and complicate **account recovery**. AWS may throttle services during abuse mitigation, reducing **availability**. Missed alerts enable ongoing misuse, risking **data exfiltration** and unauthorized changes (**integrity**).

## 推奨事項

Adopt: - **Primary** and **alternate contacts** for `security`, `billing`, `operations` - Shared, monitored aliases and SMS-capable phone numbers (non-personal) - Centralized management across accounts with periodic reviews - **Least privilege** for who can modify contact data - Regular reachability tests and documented ownership

## 修正手順


### CLI

```text
aws account put-alternate-contact --alternate-contact-type=SECURITY --email-address=<SECURITY_EMAIL> --name="<SECURITY_CONTACT_NAME>" --phone-number="<SECURITY_PHONE>" --title="Security"
```

### Terraform

```hcl
# Set the Security alternate contact for the AWS account
resource "aws_account_alternate_contact" "<example_resource_name>" {
  alternate_contact_type = "SECURITY"  # Critical: ensures AWS can reach your security team
  email_address          = "<SECURITY_EMAIL>"  # Critical: contact destination
  name                   = "<SECURITY_CONTACT_NAME>"
  phone_number           = "<SECURITY_PHONE>"
  title                  = "Security"
}
```

### Other

1. Sign in to the AWS Management Console
2. Open Billing and Cost Management, then click your account name > Account
3. Under Contact information, click Edit, update details, then Update
4. Under Alternate contacts, click Edit
5. Enter Security contact name, email, and phone (use a team alias), then Update
6. Repeat for Billing and Operations if needed

## 参考資料

- [https://repost.aws/knowledge-center/update-phone-number](https://repost.aws/knowledge-center/update-phone-number)
- [https://support.stax.io/docs/accounts/update-aws-account-contact-details](https://support.stax.io/docs/accounts/update-aws-account-contact-details)
- [https://maartenbruntink.nl/blog/2022/09/26/aws-account-hygiene-101-mass-updating-alternate-account-contacts/](https://maartenbruntink.nl/blog/2022/09/26/aws-account-hygiene-101-mass-updating-alternate-account-contacts/)
- [https://docs.aws.amazon.com/security-ir/latest/userguide/update-account-contact-info.html](https://docs.aws.amazon.com/security-ir/latest/userguide/update-account-contact-info.html)
- [https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-primary.html)
- [https://repost.aws/knowledge-center/add-update-billing-contact](https://repost.aws/knowledge-center/add-update-billing-contact)
- [https://aws.amazon.com/blogs/security/update-the-alternate-security-contact-across-your-aws-accounts-for-timely-security-notifications/](https://aws.amazon.com/blogs/security/update-the-alternate-security-contact-across-your-aws-accounts-for-timely-security-notifications/)
- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_update_contacts.html)
- [https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html)

## 技術情報

- Source Metadata：[sources/aws/account_maintain_current_contact_details/metadata.json](../../sources/aws/account_maintain_current_contact_details/metadata.json)
- Source Code：[sources/aws/account_maintain_current_contact_details/check.py](../../sources/aws/account_maintain_current_contact_details/check.py)
- Source Metadata Path：`sources/aws/account_maintain_current_contact_details/metadata.json`
- Source Code Path：`sources/aws/account_maintain_current_contact_details/check.py`

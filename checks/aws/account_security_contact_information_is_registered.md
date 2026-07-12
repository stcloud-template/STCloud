# AWS account has security alternate contact registered

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `account_security_contact_information_is_registered` |
| クラウドプラットフォーム | AWS |
| サービス | account |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

Account settings contain a **Security alternate contact** in Alternate Contacts (name, `EmailAddress`, `PhoneNumber`) for targeted AWS security notifications.

## リスク

Missing or outdated **security contact** can delay or prevent AWS advisories from reaching responders, increasing risk to: - Confidentiality: data exfiltration from undetected compromise - Integrity: unauthorized changes persist longer - Availability: resource abuse (e.g., cryptomining) and outages

## 推奨事項

Define and maintain a **Security alternate contact**: - Use a monitored alias (e.g., `security@domain`) and team phone - Apply to every account (prefer Org-wide automation) - Review after org/personnel changes and test delivery - Document ownership and escalation paths Align with **incident response** and **least privilege** principles.

## 修正手順


### CLI

```text
aws account put-alternate-contact --alternate-contact-type SECURITY --email-address <EMAIL_ADDRESS> --name <CONTACT_NAME> --phone-number <PHONE_NUMBER>
```

### Terraform

```hcl
# Set the SECURITY alternate contact for the current AWS account
resource "aws_account_alternate_contact" "<example_resource_name>" {
  alternate_contact_type = "SECURITY"  # Critical: sets Security contact type
  email_address          = "security@example.com"  # Contact email
  name                   = "Security Team"         # Contact name
  phone_number           = "+1-555-0100"          # Contact phone
}
```

### Other

1. Sign in to the AWS Management Console as the root user or an admin with account:PutAlternateContact
2. Click your account name (top-right) and select My Account (or Account)
3. Scroll to Alternate Contacts and click Edit in the Security section
4. Enter Security Email, Name, and Phone Number
5. Click Update (or Save changes)

## 参考資料

- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact)
- [https://support.icompaas.com/support/solutions/articles/62000234161-1-2-ensure-security-contact-information-is-registered-manual-](https://support.icompaas.com/support/solutions/articles/62000234161-1-2-ensure-security-contact-information-is-registered-manual-)
- [https://www.plerion.com/cloud-knowledge-base/ensure-security-contact-information-is-registered](https://www.plerion.com/cloud-knowledge-base/ensure-security-contact-information-is-registered)
- [https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv](https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv)

## 技術情報

- Source Metadata：[sources/aws/account_security_contact_information_is_registered/metadata.json](../../sources/aws/account_security_contact_information_is_registered/metadata.json)
- Source Code：[sources/aws/account_security_contact_information_is_registered/check.py](../../sources/aws/account_security_contact_information_is_registered/check.py)
- Source Metadata Path：`sources/aws/account_security_contact_information_is_registered/metadata.json`
- Source Code Path：`sources/aws/account_security_contact_information_is_registered/check.py`

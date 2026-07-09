# AWS account has security alternate contact registered

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `account_security_contact_information_is_registered` |
| 云平台 | AWS |
| 服务 | account |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | governance |

## 描述

Account settings contain a **Security alternate contact** in Alternate Contacts (name, `EmailAddress`, `PhoneNumber`) for targeted AWS security notifications.

## 风险

Missing or outdated **security contact** can delay or prevent AWS advisories from reaching responders, increasing risk to: - Confidentiality: data exfiltration from undetected compromise - Integrity: unauthorized changes persist longer - Availability: resource abuse (e.g., cryptomining) and outages

## 推荐措施

Define and maintain a **Security alternate contact**: - Use a monitored alias (e.g., `security@domain`) and team phone - Apply to every account (prefer Org-wide automation) - Review after org/personnel changes and test delivery - Document ownership and escalation paths Align with **incident response** and **least privilege** principles.

## 修复步骤


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

## 参考资料

- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/account_alternate_contact)
- [https://support.icompaas.com/support/solutions/articles/62000234161-1-2-ensure-security-contact-information-is-registered-manual-](https://support.icompaas.com/support/solutions/articles/62000234161-1-2-ensure-security-contact-information-is-registered-manual-)
- [https://www.plerion.com/cloud-knowledge-base/ensure-security-contact-information-is-registered](https://www.plerion.com/cloud-knowledge-base/ensure-security-contact-information-is-registered)
- [https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv](https://repost.aws/articles/ARDFbpt-bvQ8iuErnqVVcCXQ/managing-aws-organization-alternate-contacts-via-csv)

## 技术信息

- Source Metadata：[sources/aws/account_security_contact_information_is_registered/metadata.json](../../sources/aws/account_security_contact_information_is_registered/metadata.json)
- Source Code：[sources/aws/account_security_contact_information_is_registered/check.py](../../sources/aws/account_security_contact_information_is_registered/check.py)
- Source Metadata Path：`sources/aws/account_security_contact_information_is_registered/metadata.json`
- Source Code Path：`sources/aws/account_security_contact_information_is_registered/check.py`

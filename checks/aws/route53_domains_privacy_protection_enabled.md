# Route 53 domain has admin contact privacy protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `route53_domains_privacy_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | route53 |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure, Sensitive Data Identifications/PII |
| リソースタイプ | Other |
| リソースグループ | network |

## 説明

**Route 53 domain** administrative contact has **privacy protection** enabled, so WHOIS queries return redacted or proxy details. Evaluates whether contact data is hidden instead of publicly listed.

## リスク

**Public WHOIS contact data** exposes names, emails, phones, and addresses, enabling: - **Phishing/social engineering** of the registrar - **SIM-swap** or account takeover - **Domain hijacking**, affecting DNS integrity/availability It also increases spam and targeted harassment.

## 推奨事項

Enable **WHOIS privacy** for all contacts (admin, registrant, tech) to minimize exposure. Apply **defense in depth**: use dedicated, monitored contact emails, enforce **transfer lock** and **MFA** on registrar access, and regularly review settings. *If a TLD lacks privacy*, provide minimal, role-based contact details.

## 修正手順


### CLI

```text
aws route53domains update-domain-contact-privacy --domain-name <DOMAIN_NAME> --admin-privacy
```

### Terraform

```hcl
resource "aws_route53domains_registered_domain" "<example_resource_name>" {
  domain_name   = "<example_resource_name>"
  admin_privacy = true # Critical: enables admin contact privacy to pass the check
}
```

### Other

1. Open the AWS Console and go to Route 53
2. Click Registered domains and select <DOMAIN_NAME>
3. Click Edit in Contact information
4. Enable Privacy protection (ensures Admin contact privacy is on)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-privacy-protection.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-privacy-protection.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/privacy-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/privacy-protection.html)
- [https://support.icompaas.com/support/solutions/articles/62000233459-enable-privacy-protection-for-for-a-route53-domain-](https://support.icompaas.com/support/solutions/articles/62000233459-enable-privacy-protection-for-for-a-route53-domain-)

## 技術情報

- Source Metadata：[sources/aws/route53_domains_privacy_protection_enabled/metadata.json](../../sources/aws/route53_domains_privacy_protection_enabled/metadata.json)
- Source Code：[sources/aws/route53_domains_privacy_protection_enabled/check.py](../../sources/aws/route53_domains_privacy_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/route53_domains_privacy_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/route53_domains_privacy_protection_enabled/check.py`

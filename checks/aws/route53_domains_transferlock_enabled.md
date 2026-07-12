# Route 53 domain has Transfer Lock enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `route53_domains_transferlock_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | route53 |
| 重大度 | high |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | Other |
| リソースグループ | network |

## 説明

**Route 53 registered domains** are assessed for a transfer-lock state, indicated by the `clientTransferProhibited` status on the domain.

## リスク

Without **transfer lock**, a domain can be illicitly moved to another registrar, enabling **domain hijacking**. Attackers could alter DNS, redirect traffic, harvest credentials, and disrupt email and apps-compromising **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Enable **transfer lock** on domains to prevent unauthorized registrar moves. Enforce **least privilege** on domain management, require **MFA**, and monitor status changes. *For planned transfers*, remove the lock only under approved change control and re-enable immediately afterward.

## 修正手順


### CLI

```text
aws route53domains enable-domain-transfer-lock --domain-name <example_domain_name>
```

### Terraform

```hcl
resource "aws_route53domains_registered_domain" "<example_resource_name>" {
  domain_name   = "<example_domain_name>"
  transfer_lock = true  # Enables transfer lock (sets clientTransferProhibited)
}
```

### Other

1. Open the AWS Management Console and go to Route 53
2. In the left pane, select Registered domains
3. Click the domain name <example_domain_name>
4. In Actions, choose Turn on transfer lock
5. Confirm to enable the lock

## 参考資料

- [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-lock.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-lock.html)

## 技術情報

- Source Metadata：[sources/aws/route53_domains_transferlock_enabled/metadata.json](../../sources/aws/route53_domains_transferlock_enabled/metadata.json)
- Source Code：[sources/aws/route53_domains_transferlock_enabled/check.py](../../sources/aws/route53_domains_transferlock_enabled/check.py)
- Source Metadata Path：`sources/aws/route53_domains_transferlock_enabled/metadata.json`
- Source Code Path：`sources/aws/route53_domains_transferlock_enabled/check.py`

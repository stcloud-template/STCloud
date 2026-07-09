# Route 53 domain has Transfer Lock enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `route53_domains_transferlock_enabled` |
| 云平台 | AWS |
| 服务 | route53 |
| 严重等级 | high |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| 资源类型 | Other |
| 资源组 | network |

## 描述

**Route 53 registered domains** are assessed for a transfer-lock state, indicated by the `clientTransferProhibited` status on the domain.

## 风险

Without **transfer lock**, a domain can be illicitly moved to another registrar, enabling **domain hijacking**. Attackers could alter DNS, redirect traffic, harvest credentials, and disrupt email and apps-compromising **confidentiality**, **integrity**, and **availability**.

## 推荐措施

Enable **transfer lock** on domains to prevent unauthorized registrar moves. Enforce **least privilege** on domain management, require **MFA**, and monitor status changes. *For planned transfers*, remove the lock only under approved change control and re-enable immediately afterward.

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-lock.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-lock.html)

## 技术信息

- Source Metadata：[sources/aws/route53_domains_transferlock_enabled/metadata.json](../../sources/aws/route53_domains_transferlock_enabled/metadata.json)
- Source Code：[sources/aws/route53_domains_transferlock_enabled/check.py](../../sources/aws/route53_domains_transferlock_enabled/check.py)
- Source Metadata Path：`sources/aws/route53_domains_transferlock_enabled/metadata.json`
- Source Code Path：`sources/aws/route53_domains_transferlock_enabled/check.py`

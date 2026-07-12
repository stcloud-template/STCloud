# Service Catalog portfolio is shared only within the AWS Organization

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `servicecatalog_portfolio_shared_within_organization_only` |
| クラウドプラットフォーム | AWS |
| サービス | servicecatalog |
| 重大度 | high |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS Service Catalog portfolios** are assessed to confirm sharing occurs via **AWS Organizations** integration, not direct `ACCOUNT` shares. It reviews shared portfolios and identifies those targeted to individual accounts instead of organizational scopes.

## リスク

Sharing with individual accounts enables recipients to import and launch products outside centralized guardrails, inheriting launch roles. This can cause unauthorized provisioning, data exposure, and configuration drift-impacting confidentiality, integrity, and availability through misused privileges and uncontrolled costs.

## 推奨事項

Prefer **organizational sharing** for portfolios and avoid `ACCOUNT` targets. Enforce **least privilege** on portfolio access and launch roles, and review shares regularly. Apply **separation of duties** and **defense in depth** so only governed accounts consume products and blast radius remains constrained.

## 修正手順


### CLI

```text
aws servicecatalog create-portfolio-share --portfolio-id <portfolio-id> --organization-ids <org-id>
```

### Native IaC

```yaml
# CloudFormation: Share Service Catalog portfolio only within the AWS Organization
Resources:
  <example_resource_name>:
    Type: AWS::ServiceCatalog::PortfolioShare
    Properties:
      PortfolioId: <example_resource_id>
      OrganizationNode:               # CRITICAL: share within AWS Organizations
        Type: ORGANIZATION            # Shares the portfolio with the entire org
        Value: <example_resource_id>  # e.g., o-xxxxxxxxxx
```

### Terraform

```hcl
# Share Service Catalog portfolio only within the AWS Organization
resource "aws_servicecatalog_portfolio_share" "<example_resource_name>" {
  portfolio_id = "<example_resource_id>"

  organization_node {           # CRITICAL: share within AWS Organizations
    type  = "ORGANIZATION"     # Shares the portfolio with the entire org
    value = "<example_resource_id>"  # e.g., o-xxxxxxxxxx
  }
}
```

### Other

1. In the AWS Console, go to Service Catalog > Portfolios and open the target portfolio
2. Open the Shares/Sharing tab
3. Remove every share of Type "Account" (stop sharing with each account)
4. Click Share, choose "AWS Organizations", set Type to "Organization", enter your Org ID (o-xxxxxxxxxx), and share
5. Verify no remaining shares of Type "Account" exist

## 参考資料

- [https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html)

## 技術情報

- Source Metadata：[sources/aws/servicecatalog_portfolio_shared_within_organization_only/metadata.json](../../sources/aws/servicecatalog_portfolio_shared_within_organization_only/metadata.json)
- Source Code：[sources/aws/servicecatalog_portfolio_shared_within_organization_only/check.py](../../sources/aws/servicecatalog_portfolio_shared_within_organization_only/check.py)
- Source Metadata Path：`sources/aws/servicecatalog_portfolio_shared_within_organization_only/metadata.json`
- Source Code Path：`sources/aws/servicecatalog_portfolio_shared_within_organization_only/check.py`

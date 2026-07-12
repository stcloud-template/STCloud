# AWS account is subscribed to an AWS Premium Support plan

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `trustedadvisor_premium_support_plan_subscribed` |
| クラウドプラットフォーム | AWS |
| サービス | trustedadvisor |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | monitoring |

## 説明

**AWS account** is subscribed to an **AWS Premium Support plan** (e.g., Business or Enterprise)

## リスク

Without **Premium Support**, critical incidents face slower response, reducing **availability** and delaying containment of security events. Limited Trusted Advisor coverage lets **misconfigurations** persist, risking **data exposure** and **privilege misuse**. Lack of expert guidance increases change risk during production impacts.

## 推奨事項

Adopt **Business** or higher for production and mission-critical accounts. - Integrate Support into IR with defined contacts/severity - Enforce **least privilege** for case access - Use Trusted Advisor for proactive hardening - If opting out, ensure an equivalent 24/7 support and escalation path

## 修正手順


### Other

1. Sign in to the AWS Management Console as the account root user
2. Open https://console.aws.amazon.com/support/home#/plans
3. Click "Change plan"
4. Select "Business Support" (or higher) and click "Continue"
5. Review and confirm the upgrade

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/Support/support-plan.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/Support/support-plan.html)
- [https://aws.amazon.com/premiumsupport/plans/](https://aws.amazon.com/premiumsupport/plans/)

## 技術情報

- Source Metadata：[sources/aws/trustedadvisor_premium_support_plan_subscribed/metadata.json](../../sources/aws/trustedadvisor_premium_support_plan_subscribed/metadata.json)
- Source Code：[sources/aws/trustedadvisor_premium_support_plan_subscribed/check.py](../../sources/aws/trustedadvisor_premium_support_plan_subscribed/check.py)
- Source Metadata Path：`sources/aws/trustedadvisor_premium_support_plan_subscribed/metadata.json`
- Source Code Path：`sources/aws/trustedadvisor_premium_support_plan_subscribed/check.py`

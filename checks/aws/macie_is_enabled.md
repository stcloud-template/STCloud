# Amazon Macie is enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `macie_is_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | macie |
| 重大度 | medium |
| カテゴリ | secrets, forensics-ready |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | security |

## 説明

**Amazon Macie** status is assessed per region with **S3** presence to determine if sensitive data discovery is operational. The outcome reflects whether Macie is active or in a `PAUSED`/not enabled state for the account and region.

## リスク

Without active Macie, sensitive data in **S3** can remain unclassified and exposed. Misconfigured access and public buckets may go undetected, enabling data exfiltration and secret leakage. This degrades confidentiality and widens breach blast radius by reducing visibility into where sensitive data resides.

## 推奨事項

Enable and maintain **Amazon Macie** in all regions hosting **S3** data. Use continuous sensitive data discovery, apply custom classifications for your data types, and route findings to monitoring. Enforce least privilege for Macie access and strengthen defense in depth with restrictive bucket policies and access controls.

## 修正手順


### CLI

```text
aws macie2 enable-macie --region <REGION>
```

### Native IaC

```yaml
# CloudFormation: Enable Amazon Macie in this region
Resources:
  MacieSession:
    Type: AWS::Macie::Session
    Properties:
      Status: ENABLED  # Critical: Enables Macie for the account in this region
```

### Terraform

```hcl
# Enables Amazon Macie in this region
resource "aws_macie2_account" "main" {
  # Critical: Creating this resource enables Macie for the account in the region
}
```

### Other

1. Sign in to the AWS Management Console and switch to the target region
2. Open Amazon Macie
3. Click Get started or Enable Macie
4. If Macie shows Suspended/Paused, click Resume Macie
5. Repeat in each region with S3 buckets as needed

## 参考資料

- [https://aws.amazon.com/macie/getting-started/](https://aws.amazon.com/macie/getting-started/)

## 技術情報

- Source Metadata：[sources/aws/macie_is_enabled/metadata.json](../../sources/aws/macie_is_enabled/metadata.json)
- Source Code：[sources/aws/macie_is_enabled/check.py](../../sources/aws/macie_is_enabled/check.py)
- Source Metadata Path：`sources/aws/macie_is_enabled/metadata.json`
- Source Code Path：`sources/aws/macie_is_enabled/check.py`

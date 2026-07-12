# IAM Access Analyzer is enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `accessanalyzer_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | accessanalyzer |
| 重大度 | low |
| カテゴリ | identity-access, trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | security |

## 説明

**IAM Access Analyzer** presence and status are evaluated per account and Region. An analyzer in `ACTIVE` state indicates continuous analysis of supported resources and IAM activity to identify external, internal, and unused access.

## リスク

Without an active analyzer, visibility into unintended public, cross-account, or risky internal access is lost. Adversaries can exploit exposed S3, snapshots, KMS keys, or permissive role trusts for data exfiltration and escalation. Unused permissions persist, enlarging the attack surface. This degrades confidentiality and integrity.

## 推奨事項

Enable **IAM Access Analyzer** across all accounts and active Regions (*or organization-wide*). Operate on least privilege: continuously review findings, remove unintended access, and trim unused permissions. Use archive rules sparingly, integrate reviews into change/CI/CD workflows, and enforce separation of duties on policy changes.

## 修正手順


### CLI

```text
aws accessanalyzer create-analyzer --analyzer-name example_resource --type ACCOUNT
```

### Native IaC

```yaml
Resources:
  example_resource:
    Type: AWS::AccessAnalyzer::Analyzer  # This resource enables IAM Access Analyzer
    Properties:
      AnalyzerName: example_resource
      Type: ACCOUNT  # This line fixes the security issue
```

### Terraform

```hcl
resource "aws_accessanalyzer_analyzer" "example_resource" {
  analyzer_name = "example_resource"
  type          = "ACCOUNT" # This line fixes the security issue
}
```

### Other

1. In the AWS Console, open IAM
2. Go to Access analyzer > Analyzer settings
3. Confirm the desired Region
4. Click Create analyzer
5. Select Resource analysis - External access
6. Set Name to "example_resource" and Zone of trust to "Current account"
7. Click Create

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-manage-external.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-manage-external.html)
- [https://aws.amazon.com/iam/access-analyzer/](https://aws.amazon.com/iam/access-analyzer/)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)
- [https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAnalyzer.html](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateAnalyzer.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-external.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-external.html)
- [https://docs.aws.amazon.com/access-analyzer/latest/APIReference/Welcome.html](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/Welcome.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-internal.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-internal.html)

## 技術情報

- Source Metadata：[sources/aws/accessanalyzer_enabled/metadata.json](../../sources/aws/accessanalyzer_enabled/metadata.json)
- Source Code：[sources/aws/accessanalyzer_enabled/check.py](../../sources/aws/accessanalyzer_enabled/check.py)
- Source Metadata Path：`sources/aws/accessanalyzer_enabled/metadata.json`
- Source Code Path：`sources/aws/accessanalyzer_enabled/check.py`

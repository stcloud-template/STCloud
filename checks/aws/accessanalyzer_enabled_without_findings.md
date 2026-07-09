# IAM Access Analyzer analyzer is active and has no active findings

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `accessanalyzer_enabled_without_findings` |
| 云平台 | AWS |
| 服务 | accessanalyzer |
| 严重等级 | low |
| 类别 | identity-access, trust-boundaries, internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**IAM Access Analyzer** analyzers are in `Active` state and currently report zero `Active` findings within their scope of monitored resources.

## 风险

Unresolved `Active` findings indicate unintended external or internal access paths. - **Confidentiality**: public/cross-account reads of data (buckets, snapshots, secrets) - **Integrity**: rogue role assumption or KMS use enabling policy/data changes - **Lateral movement** across accounts

## 推荐措施

Enable **IAM Access Analyzer** in all relevant Regions and org/account scopes. Triage every `Active` finding: - Remove unintended access by tightening resource and trust policies - Enforce **least privilege** and separation of duties - Archive only validated, intended access - Continuously monitor and automate reviews

## 修复步骤


### Native IaC

```yaml
Resources:
  example_resource:
    Type: AWS::AccessAnalyzer::Analyzer
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

1. In the AWS Console, go to IAM > Access analyzer
2. If no analyzer exists, click Create analyzer, select Type: Account, name it example_resource, and click Create
3. To clear active findings: under Resource analysis, select your analyzer, select all Active findings, choose Actions > Archive
4. For unintended access findings, open the finding and follow the linked resource to remove the offending permission (edit the resource policy or role trust policy), then return to the finding and choose Rescan
5. Confirm the dashboard shows 0 Active findings

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-remediate.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-remediate.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html)
- [https://aws.amazon.com/iam/access-analyzer/](https://aws.amazon.com/iam/access-analyzer/)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-dashboard.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-dashboard.html)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html)
- [https://aws.amazon.com/blogs/security/automate-resolution-for-iam-access-analyzer-cross-account-access-findings-on-iam-roles/](https://aws.amazon.com/blogs/security/automate-resolution-for-iam-access-analyzer-cross-account-access-findings-on-iam-roles/)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AccessAnalyzer/findings.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AccessAnalyzer/findings.html)

## 技术信息

- Source Metadata：[sources/aws/accessanalyzer_enabled_without_findings/metadata.json](../../sources/aws/accessanalyzer_enabled_without_findings/metadata.json)
- Source Code：[sources/aws/accessanalyzer_enabled_without_findings/check.py](../../sources/aws/accessanalyzer_enabled_without_findings/check.py)
- Source Metadata Path：`sources/aws/accessanalyzer_enabled_without_findings/metadata.json`
- Source Code Path：`sources/aws/accessanalyzer_enabled_without_findings/check.py`

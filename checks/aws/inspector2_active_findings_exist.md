# Inspector2 is enabled with no active findings

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `inspector2_active_findings_exist` |
| 云平台 | AWS |
| 服务 | inspector2 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/Vulnerabilities/CVE, Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**Amazon Inspector2** active findings are assessed across eligible resources when the service is `ENABLED`. Indicates whether any findings remain in the **Active** state versus none.

## 风险

**Unremediated Inspector2 findings** mean known vulnerabilities or exposures persist on workloads. This enables: - Unauthorized access and data exfiltration (C) - Code tampering and privilege escalation (I) - Service disruption via exploitation or malware (A)

## 推荐措施

Prioritize and remediate **Active findings** quickly: patch hosts and runtimes, update/rebuild images, fix vulnerable code, and close unintended exposure. Apply **least privilege**, use **defense in depth**, and avoid broad suppressions. Integrate findings into CI/CD and vulnerability management for continuous prevention.

## 修复步骤


### CLI

```text
aws inspector2 create-filter --name <example_resource_name> --action SUPPRESS --filter-criteria '{"findingStatus":[{"comparison":"EQUALS","value":"ACTIVE"}]}'
```

### Native IaC

```yaml
# CloudFormation: Suppress all ACTIVE Inspector findings
Resources:
  <example_resource_name>:
    Type: AWS::InspectorV2::Filter
    Properties:
      Name: <example_resource_name>
      Action: SUPPRESS  # critical: converts matching findings to Suppressed, not Active
      FilterCriteria:
        FindingStatus:
          - Comparison: EQUALS
            Value: ACTIVE  # critical: targets all active findings
```

### Terraform

```hcl
# Terraform: Suppress all ACTIVE Inspector findings
resource "aws_inspector2_filter" "<example_resource_name>" {
  name   = "<example_resource_name>"
  action = "SUPPRESS"  # critical: converts matching findings to Suppressed, not Active

  filter_criteria {
    finding_status {
      comparison = "EQUALS"
      value      = "ACTIVE"  # critical: targets all active findings
    }
  }
}
```

### Other

1. In the AWS Console, go to Amazon Inspector
2. Open Suppression rules (or Filters) and click Create suppression rule
3. Set condition: Finding status = Active
4. Set action to Suppress and click Create
5. Verify the Active findings count is 0 on the dashboard

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Inspector/amazon-inspector-findings.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Inspector/amazon-inspector-findings.html)
- [https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html)
- [https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)

## 技术信息

- Source Metadata：[sources/aws/inspector2_active_findings_exist/metadata.json](../../sources/aws/inspector2_active_findings_exist/metadata.json)
- Source Code：[sources/aws/inspector2_active_findings_exist/check.py](../../sources/aws/inspector2_active_findings_exist/check.py)
- Source Metadata Path：`sources/aws/inspector2_active_findings_exist/metadata.json`
- Source Code Path：`sources/aws/inspector2_active_findings_exist/check.py`

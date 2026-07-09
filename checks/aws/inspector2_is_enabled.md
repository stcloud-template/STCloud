# Inspector2 is enabled for Amazon EC2 instances, ECR container images, Lambda functions, and Lambda code

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `inspector2_is_enabled` |
| 云平台 | AWS |
| 服务 | inspector2 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | security |

## 描述

**Amazon Inspector 2** activation and coverage across regions, verifying that scanning is active for **EC2**, **ECR**, **Lambda functions**, and **Lambda code** where applicable. It flags missing account activation or gaps in any scan type.

## 风险

Absent or partial coverage leaves **unpatched vulnerabilities**, risky **code dependencies**, and **unintended network exposure** undetected. Attackers can exploit known CVEs for **remote code execution**, **lateral movement**, and **data exfiltration**, degrading **confidentiality**, **integrity**, and **availability**.

## 推荐措施

Enable **Amazon Inspector 2** across all regions and activate scans for **EC2**, **ECR**, **Lambda**, and **Lambda code**. Apply **defense in depth**: auto-enable coverage for new workloads, integrate findings with patching and CI/CD gates, enforce remediation SLAs, and grant only **least privilege** to process and act on findings.

## 修复步骤


### CLI

```text
aws inspector2 enable --resource-types EC2 ECR LAMBDA LAMBDA_CODE
```

### Terraform

```hcl
resource "aws_inspector2_enabler" "<example_resource_name>" {
  resource_types = ["EC2", "ECR", "LAMBDA", "LAMBDA_CODE"] # Enables Inspector2 scans for all required resource types
}
```

### Other

1. Sign in to the AWS Console and open Amazon Inspector (v2)
2. If not yet activated: click Get started > Activate Amazon Inspector
3. If already activated: go to Settings > Scans and ensure EC2, ECR, Lambda functions, and Lambda code are all enabled, then Save

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Inspector2/enable-amazon-inspector2.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Inspector2/enable-amazon-inspector2.html)
- [https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding.html)
- [https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html)

## 技术信息

- Source Metadata：[sources/aws/inspector2_is_enabled/metadata.json](../../sources/aws/inspector2_is_enabled/metadata.json)
- Source Code：[sources/aws/inspector2_is_enabled/check.py](../../sources/aws/inspector2_is_enabled/check.py)
- Source Metadata Path：`sources/aws/inspector2_is_enabled/metadata.json`
- Source Code Path：`sources/aws/inspector2_is_enabled/check.py`

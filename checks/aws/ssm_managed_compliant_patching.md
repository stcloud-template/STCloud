# EC2 managed instance is compliant with Systems Manager patching requirements

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ssm_managed_compliant_patching` |
| クラウドプラットフォーム | AWS |
| サービス | ssm |
| 重大度 | high |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsSsmPatchCompliance |
| リソースグループ | devops |

## 説明

**SSM-managed EC2 instances** report **patch compliance** against defined baselines. This evaluates each managed node's compliance status from Patch Manager to determine whether required security updates are applied according to policy.

## リスク

**Unpatched instances** expose known `CVE` vulnerabilities, enabling **remote code execution**, **privilege escalation**, and **lateral movement**. This threatens **confidentiality** (data exfiltration), **integrity** (unauthorized changes), and **availability** (ransomware, crypto-mining, outages).

## 推奨事項

Adopt **automated patch management** with Systems Manager: enroll EC2 as managed nodes, define strict **patch baselines**, run frequent **compliance scans**, and **install critical updates** promptly. Apply **defense in depth**: least-privileged roles for patching, staged rollouts, maintenance windows, and centralized compliance reporting with alerting.

## 修正手順


### CLI

```text
aws ssm send-command --instance-ids <INSTANCE_ID> --document-name AWS-RunPatchBaseline --parameters Operation=Install
```

### Native IaC

```yaml
# Create an SSM Association to install missing patches on the instance
Resources:
  <example_resource_name>:
    Type: AWS::SSM::Association
    Properties:
      Name: AWS-RunPatchBaseline
      InstanceId: <example_resource_id>
      Parameters:
        Operation:
          - Install  # Critical: installs missing patches so the instance becomes COMPLIANT
```

### Terraform

```hcl
# Run AWS-RunPatchBaseline to install missing patches on the instance
resource "aws_ssm_association" "<example_resource_name>" {
  name        = "AWS-RunPatchBaseline"
  instance_id = "<example_resource_id>"
  parameters = {
    Operation = ["Install"]  # Critical: installs patches to achieve COMPLIANT status
  }
}
```

### Other

1. Open AWS Console > Systems Manager > Run Command
2. Click Run command
3. Select document: AWS-RunPatchBaseline
4. In Parameters, set Operation = Install
5. In Targets, select the non-compliant instance
6. Click Run; wait for command to complete and verify Compliance shows COMPLIANT

## 参考資料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-compliance-identify.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-compliance-identify.html)
- [https://support.icompaas.com/support/solutions/articles/62000233554-ensure-ec2-instances-managed-by-systems-manager-are-compliant-with-patching-requirements](https://support.icompaas.com/support/solutions/articles/62000233554-ensure-ec2-instances-managed-by-systems-manager-are-compliant-with-patching-requirements)
- [https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-fixing.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-fixing.html)

## 技術情報

- Source Metadata：[sources/aws/ssm_managed_compliant_patching/metadata.json](../../sources/aws/ssm_managed_compliant_patching/metadata.json)
- Source Code：[sources/aws/ssm_managed_compliant_patching/check.py](../../sources/aws/ssm_managed_compliant_patching/check.py)
- Source Metadata Path：`sources/aws/ssm_managed_compliant_patching/metadata.json`
- Source Code Path：`sources/aws/ssm_managed_compliant_patching/check.py`

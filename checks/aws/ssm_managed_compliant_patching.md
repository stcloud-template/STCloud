# EC2 managed instance is compliant with Systems Manager patching requirements

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ssm_managed_compliant_patching` |
| 云平台 | AWS |
| 服务 | ssm |
| 严重等级 | high |
| 类别 | vulnerabilities |
| 检查类型 | Software and Configuration Checks/Patch Management, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsSsmPatchCompliance |
| 资源组 | devops |

## 描述

**SSM-managed EC2 instances** report **patch compliance** against defined baselines. This evaluates each managed node's compliance status from Patch Manager to determine whether required security updates are applied according to policy.

## 风险

**Unpatched instances** expose known `CVE` vulnerabilities, enabling **remote code execution**, **privilege escalation**, and **lateral movement**. This threatens **confidentiality** (data exfiltration), **integrity** (unauthorized changes), and **availability** (ransomware, crypto-mining, outages).

## 推荐措施

Adopt **automated patch management** with Systems Manager: enroll EC2 as managed nodes, define strict **patch baselines**, run frequent **compliance scans**, and **install critical updates** promptly. Apply **defense in depth**: least-privileged roles for patching, staged rollouts, maintenance windows, and centralized compliance reporting with alerting.

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-compliance-identify.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-compliance-identify.html)
- [https://support.icompaas.com/support/solutions/articles/62000233554-ensure-ec2-instances-managed-by-systems-manager-are-compliant-with-patching-requirements](https://support.icompaas.com/support/solutions/articles/62000233554-ensure-ec2-instances-managed-by-systems-manager-are-compliant-with-patching-requirements)
- [https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-fixing.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-fixing.html)

## 技术信息

- Source Metadata：[sources/aws/ssm_managed_compliant_patching/metadata.json](../../sources/aws/ssm_managed_compliant_patching/metadata.json)
- Source Code：[sources/aws/ssm_managed_compliant_patching/check.py](../../sources/aws/ssm_managed_compliant_patching/check.py)
- Source Metadata Path：`sources/aws/ssm_managed_compliant_patching/metadata.json`
- Source Code Path：`sources/aws/ssm_managed_compliant_patching/check.py`

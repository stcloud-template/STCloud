# GuardDuty detector has EKS Audit Log Monitoring enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `guardduty_eks_audit_log_enabled` |
| 云平台 | AWS |
| 服务 | guardduty |
| 严重等级 | high |
| 类别 | cluster-security |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsGuardDutyDetector |
| 资源组 | security |

## 描述

**Amazon GuardDuty detectors** are evaluated for **EKS Audit Log Monitoring** (`EKS_AUDIT_LOGS`) being enabled to analyze Kubernetes audit activity from your **Amazon EKS** clusters.

## 风险

Without it, **Kubernetes API abuse** may go undetected, impacting CIA: - Secret access and data exfiltration - RBAC changes enabling privilege escalation - Rogue deployments for persistence/cryptomining Attackers can laterally move to AWS using harvested credentials.

## 推荐措施

Enable **EKS Audit Log Monitoring** on all detectors in every required Region, centrally managed by the GuardDuty administrator. - Route findings to alerting/IR workflows - Enforce **least privilege** on access to findings and configs - Combine with **defense-in-depth**: hardened RBAC and runtime monitoring

## 修复步骤


### CLI

```text
aws guardduty update-detector --detector-id <detector-id> --features '[{"Name":"EKS_AUDIT_LOGS","Status":"ENABLED"}]'
```

### Native IaC

```yaml
# CloudFormation: Enable EKS Audit Log Monitoring on GuardDuty detector
Resources:
  GuardDutyDetector:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true
      DataSources:
        Kubernetes:
          AuditLogs:
            Enable: true  # CRITICAL: Enables EKS Audit Log Monitoring
```

### Terraform

```hcl
# Enable EKS Audit Log Monitoring on GuardDuty detector
resource "aws_guardduty_detector" "example" {
  enable = true

  features {
    name   = "EKS_AUDIT_LOGS"
    status = "ENABLED"  # CRITICAL: Enables EKS Audit Log Monitoring
  }
}
```

### Other

1. Open the AWS Console and go to Amazon GuardDuty
2. Select the Region where you want to enable it
3. In the left menu, click EKS Protection
4. Click Enable and confirm
5. If using AWS Organizations, perform these steps in the delegated GuardDuty administrator account

## 参考资料

- [https://docs.aws.amazon.com/guardduty/latest/ug/eks-protection-enable-standalone-account.html](https://docs.aws.amazon.com/guardduty/latest/ug/eks-protection-enable-standalone-account.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-5](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-5)
- [https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html)

## 技术信息

- Source Metadata：[sources/aws/guardduty_eks_audit_log_enabled/metadata.json](../../sources/aws/guardduty_eks_audit_log_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_eks_audit_log_enabled/check.py](../../sources/aws/guardduty_eks_audit_log_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_eks_audit_log_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_eks_audit_log_enabled/check.py`

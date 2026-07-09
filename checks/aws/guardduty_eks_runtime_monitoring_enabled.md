# GuardDuty detector has EKS Runtime Monitoring enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `guardduty_eks_runtime_monitoring_enabled` |
| 云平台 | AWS |
| 服务 | guardduty |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsGuardDutyDetector |
| 资源组 | security |

## 描述

GuardDuty detectors are evaluated for **EKS Runtime Monitoring** being enabled for Amazon EKS. The configuration is at the detector level and relates to visibility into *process, file, and network* activity on EKS nodes and containers.

## 风险

Absent **EKS runtime monitoring**, in-cluster activity is blind to detection. Adversaries can run malware or cryptominers, exfiltrate secrets via pods, tamper with workloads, or pivot to other services, degrading confidentiality, corrupting integrity, and exhausting resources (availability).

## 推荐措施

- Enable **EKS Runtime Monitoring** with automated agent management across all accounts and clusters - Enforce **least privilege** for agents and segment cluster access - Integrate findings with response workflows and periodically verify runtime coverage

## 修复步骤


### CLI

```text
aws guardduty update-detector --detector-id <detector-id> --features name=EKS_RUNTIME_MONITORING,status=ENABLED
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::GuardDuty::Detector
    Properties:
      Enable: true
      Features:
        - Name: EKS_RUNTIME_MONITORING   # Critical: selects EKS Runtime Monitoring feature
          Status: ENABLED                # Critical: enables the feature to pass the check
```

### Terraform

```hcl
resource "aws_guardduty_detector" "<example_resource_name>" {
  enable = true

  features {
    name   = "EKS_RUNTIME_MONITORING"  # Critical: selects EKS Runtime Monitoring feature
    status = "ENABLED"                 # Critical: enables the feature to pass the check
  }
}
```

### Other

1. Open the AWS Console and go to Amazon GuardDuty
2. In the left pane, select Settings > Runtime monitoring
3. Under EKS Runtime Monitoring, switch the status to Enabled
4. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/guardduty-eks-protection-runtime-enabled.html](https://docs.aws.amazon.com/config/latest/developerguide/guardduty-eks-protection-runtime-enabled.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-7](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-7)

## 技术信息

- Source Metadata：[sources/aws/guardduty_eks_runtime_monitoring_enabled/metadata.json](../../sources/aws/guardduty_eks_runtime_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/guardduty_eks_runtime_monitoring_enabled/check.py](../../sources/aws/guardduty_eks_runtime_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/guardduty_eks_runtime_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/guardduty_eks_runtime_monitoring_enabled/check.py`

# EKS cluster has control plane logging enabled for api, audit, authenticator, controllerManager, and scheduler

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eks_control_plane_logging_all_types_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | eks |
| 重大度 | medium |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEksCluster |
| リソースグループ | container |

## 説明

**Amazon EKS clusters** are evaluated for **control plane logging** coverage of required types: `api`, `audit`, `authenticator`, `controllerManager`, `scheduler`. The finding identifies clusters where any of these log types are not configured.

## リスク

Gaps in **control plane logging** reduce visibility across the cluster. - Confidentiality: undetected API access, RBAC abuse, token misuse - Integrity: untraceable config changes and policy edits - Availability: scheduler/controller issues lack evidence, delaying recovery and masking attacker persistence

## 推奨事項

Enable and standardize **EKS control plane logging** for all required types `["api","audit","authenticator","controllerManager","scheduler"]`. Apply least privilege to log access, set retention and alerts, and centralize analysis to support defense in depth, rapid detection, and reliable forensics.

## 修正手順


### CLI

```text
aws eks update-cluster-config --name <cluster_name> --logging '{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}'
```

### Native IaC

```yaml
# CloudFormation: enable all EKS control plane log types
Resources:
  <example_resource_name>:
    Type: AWS::EKS::Cluster
    Properties:
      RoleArn: <example_role_arn>
      ResourcesVpcConfig:
        SubnetIds: [<example_subnet_id>]
      Logging:
        ClusterLogging:
          - EnabledTypes:
              - Type: api            # Critical: enable required control plane log types
              - Type: audit          # Critical: enable required control plane log types
              - Type: authenticator  # Critical: enable required control plane log types
              - Type: controllerManager  # Critical: enable required control plane log types
              - Type: scheduler      # Critical: enable required control plane log types
```

### Terraform

```hcl
# Enable all required EKS control plane log types
resource "aws_eks_cluster" "<example_resource_name>" {
  enabled_cluster_log_types = [
    "api",            # Critical: required control plane log types
    "audit",          # Critical: required control plane log types
    "authenticator",  # Critical: required control plane log types
    "controllerManager", # Critical: required control plane log types
    "scheduler"       # Critical: required control plane log types
  ]
}
```

### Other

1. In the AWS console, go to Amazon EKS and open your cluster
2. Open the Observability (or Logging) tab and click Manage logging
3. Turn on: api, audit, authenticator, controllerManager, scheduler
4. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/userguide/logging-monitoring.html](https://docs.aws.amazon.com/eks/latest/userguide/logging-monitoring.html)
- [https://support.icompaas.com/support/solutions/articles/62000233623-ensure-eks-control-plane-logging-is-enabled-for-all-required-log-types](https://support.icompaas.com/support/solutions/articles/62000233623-ensure-eks-control-plane-logging-is-enabled-for-all-required-log-types)
- [https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
- [https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-logging.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-logging.html)

## 技術情報

- Source Metadata：[sources/aws/eks_control_plane_logging_all_types_enabled/metadata.json](../../sources/aws/eks_control_plane_logging_all_types_enabled/metadata.json)
- Source Code：[sources/aws/eks_control_plane_logging_all_types_enabled/check.py](../../sources/aws/eks_control_plane_logging_all_types_enabled/check.py)
- Source Metadata Path：`sources/aws/eks_control_plane_logging_all_types_enabled/metadata.json`
- Source Code Path：`sources/aws/eks_control_plane_logging_all_types_enabled/check.py`

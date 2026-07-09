# Neptune cluster storage is encrypted at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `neptune_cluster_storage_encrypted` |
| 云平台 | AWS |
| 服务 | neptune |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Sensitive Data Identifications/Security |
| 资源类型 | Other |
| 资源组 | database |

## 描述

Neptune DB cluster is evaluated for **encryption at rest**. Indicating the cluster's underlying storage is not encrypted.

## 风险

**Unencrypted Neptune storage** reduces confidentiality of stored data and metadata and increases attack surface. Possible impacts: - Unauthorized access or data exfiltration from underlying volumes or snapshots - Greater blast radius from leaked or shared snapshots

## 推荐措施

Provision all new Neptune DB clusters with **encryption at rest** and prefer **Customer-Managed Keys (CMK)** for key ownership and auditability. Enforce **least privilege** on KMS keys, implement key lifecycle practices (rotation, revocation) and ensure backups/snapshots remain encrypted to prevent exposure.

## 修复步骤


### Native IaC

```yaml
Resources:
  EncryptedNeptuneCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBClusterIdentifier: !Sub ${DBClusterIdentifier}
      StorageEncrypted: true  # Enable encryption at rest for data protection
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier = "<cluster-id>"
  storage_encrypted  = true  # Enable encryption at rest for data protection
}
```

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-1](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-1)
- [https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html](https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html)

## 技术信息

- Source Metadata：[sources/aws/neptune_cluster_storage_encrypted/metadata.json](../../sources/aws/neptune_cluster_storage_encrypted/metadata.json)
- Source Code：[sources/aws/neptune_cluster_storage_encrypted/check.py](../../sources/aws/neptune_cluster_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_storage_encrypted/check.py`

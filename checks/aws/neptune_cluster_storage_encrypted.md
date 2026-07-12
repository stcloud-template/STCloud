# Neptune cluster storage is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_storage_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Sensitive Data Identifications/Security |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

Neptune DB cluster is evaluated for **encryption at rest**. Indicating the cluster's underlying storage is not encrypted.

## リスク

**Unencrypted Neptune storage** reduces confidentiality of stored data and metadata and increases attack surface. Possible impacts: - Unauthorized access or data exfiltration from underlying volumes or snapshots - Greater blast radius from leaked or shared snapshots

## 推奨事項

Provision all new Neptune DB clusters with **encryption at rest** and prefer **Customer-Managed Keys (CMK)** for key ownership and auditability. Enforce **least privilege** on KMS keys, implement key lifecycle practices (rotation, revocation) and ensure backups/snapshots remain encrypted to prevent exposure.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-1](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-1)
- [https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html](https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_storage_encrypted/metadata.json](../../sources/aws/neptune_cluster_storage_encrypted/metadata.json)
- Source Code：[sources/aws/neptune_cluster_storage_encrypted/check.py](../../sources/aws/neptune_cluster_storage_encrypted/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_storage_encrypted/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_storage_encrypted/check.py`

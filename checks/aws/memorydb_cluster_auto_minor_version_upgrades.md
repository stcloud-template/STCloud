# MemoryDB cluster has automatic minor version upgrades enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `memorydb_cluster_auto_minor_version_upgrades` |
| クラウドプラットフォーム | AWS |
| サービス | memorydb |
| 重大度 | medium |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**MemoryDB clusters** are evaluated for the `auto_minor_version_upgrade` setting that automatically applies new minor engine versions.

## リスク

Without automatic minor upgrades, clusters may run **known-vulnerable engine versions**. - Exploitable CVEs enable unauthorized reads/writes (confidentiality, integrity) - Unpatched bugs can cause **DoS** or data loss (availability) - Version drift raises operational risk and slows incident response

## 推奨事項

Enable **automatic minor version upgrades** (`auto_minor_version_upgrade=true`) for all clusters. Schedule updates in a maintenance window, validate in staging, and keep rollback plans. Apply **defense in depth** with strict ACLs and monitoring to limit exposure between releases.

## 修正手順


### CLI

```text
aws memorydb update-cluster --cluster-name <cluster-name> --auto-minor-version-upgrade
```

### Native IaC

```yaml
# Enable automatic minor version upgrades for a MemoryDB cluster
Resources:
  <example_resource_name>:
    Type: AWS::MemoryDB::Cluster
    Properties:
      ClusterName: <example_resource_name>
      ACLName: <example_acl_name>
      NodeType: <example_node_type>
      NumShards: 1
      AutoMinorVersionUpgrade: true  # Critical: enables automatic minor version upgrades
```

### Terraform

```hcl
resource "aws_memorydb_cluster" "<example_resource_name>" {
  name       = "<example_resource_name>"
  acl_name   = "<example_acl_name>"
  node_type  = "<example_node_type>"
  num_shards = 1

  auto_minor_version_upgrade = true  # Critical: enables automatic minor version upgrades
}
```

### Other

1. In the AWS Console, go to MemoryDB > Clusters
2. Select the cluster <cluster-name> and click Edit
3. Enable "Auto minor version upgrade"
4. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/memorydb/latest/devguide/engine-versions.html](https://docs.aws.amazon.com/memorydb/latest/devguide/engine-versions.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades)

## 技術情報

- Source Metadata：[sources/aws/memorydb_cluster_auto_minor_version_upgrades/metadata.json](../../sources/aws/memorydb_cluster_auto_minor_version_upgrades/metadata.json)
- Source Code：[sources/aws/memorydb_cluster_auto_minor_version_upgrades/check.py](../../sources/aws/memorydb_cluster_auto_minor_version_upgrades/check.py)
- Source Metadata Path：`sources/aws/memorydb_cluster_auto_minor_version_upgrades/metadata.json`
- Source Code Path：`sources/aws/memorydb_cluster_auto_minor_version_upgrades/check.py`

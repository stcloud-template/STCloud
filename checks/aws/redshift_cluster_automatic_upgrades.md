# Redshift cluster has automatic version upgrade enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_automatic_upgrades` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | medium |
| 类别 | vulnerabilities |
| 检查类型 | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

**Amazon Redshift clusters** have automatic major engine upgrades allowed via `AllowVersionUpgrade` so updates are applied during the maintenance window.

## 风险

Without automatic upgrades, clusters can run **vulnerable engine versions**, enabling exploits against known flaws. Attackers may read or tamper data (**confidentiality/integrity**), and unresolved bugs can cause downtime (**availability**). Delayed patching increases exposure window and operational risk.

## 推荐措施

Enable `AllowVersionUpgrade` to keep clusters patched. Use a controlled maintenance window and an appropriate maintenance track; validate upgrades in staging before production. Align with **secure-by-default** and **defense in depth**; keep tested backups and rollback plans. *Document justified exceptions and review regularly*.

## 修复步骤


### CLI

```text
aws redshift modify-cluster --cluster-identifier <cluster_id> --allow-version-upgrade
```

### Native IaC

```yaml
# CloudFormation to ensure Redshift allows major version upgrades
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      DBName: <db_name>
      MasterUsername: <master_username>
      MasterUserPassword: <master_user_password>
      NodeType: <node_type>
      AllowVersionUpgrade: true  # Critical: enables automatic major version upgrades during the maintenance window
```

### Terraform

```hcl
# Redshift cluster allowing automatic major version upgrades
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  node_type          = "<node_type>"
  master_username    = "<master_username>"
  master_password    = "<master_user_password>"

  allow_version_upgrade = true  # Critical: enables automatic major version upgrades
}
```

### Other

1. Open the Amazon Redshift console
2. Go to Clusters and select your cluster
3. Click Edit (or Edit maintenance settings)
4. Enable "Major version upgrades" (Allow version upgrade)
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-redshift-maintenance.html](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-modify-redshift-maintenance.html)
- [https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_automatic_upgrades/metadata.json](../../sources/aws/redshift_cluster_automatic_upgrades/metadata.json)
- Source Code：[sources/aws/redshift_cluster_automatic_upgrades/check.py](../../sources/aws/redshift_cluster_automatic_upgrades/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_automatic_upgrades/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_automatic_upgrades/check.py`

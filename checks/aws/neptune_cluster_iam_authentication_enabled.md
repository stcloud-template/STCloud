# Neptune cluster has IAM authentication enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `neptune_cluster_iam_authentication_enabled` |
| 云平台 | AWS |
| 服务 | neptune |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Credential Access |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Neptune DB clusters are evaluated for **IAM database authentication**. If this setting is enabled, the cluster supports IAM-based authentication. If disabled, the cluster requires traditional database credentials instead.

## 风险

**Disabled IAM database authentication** weakens confidentiality and integrity of the database. - Static or embedded DB credentials can be stolen or reused, enabling unauthorized queries and data exfiltration - Attackers may bypass centralized access controls, escalate privileges, and move laterally without IAM-based audit trails

## 推荐措施

Adopt **IAM database authentication** and centralized identity management to remove static DB credentials and improve auditability. - Enforce **least privilege** for database roles - Use short-lived credentials, centralized rotation and logging - Apply defense-in-depth and integrate DB access with IAM for accountability

## 修复步骤


### CLI

```text
aws neptune modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --enable-iam-database-authentication --apply-immediately
```

### Native IaC

```yaml
Resources:
  NeptuneCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBClusterIdentifier: <DB_CLUSTER_ID>
      IamAuthEnabled: true  # Enable IAM authentication instead of static DB credentials
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier                  = "<DB_CLUSTER_ID>"
  iam_database_authentication_enabled = true  # Enable IAM authentication instead of static DB credentials
}
```

### Other

1. Sign in to the AWS Management Console and open Amazon Neptune > Databases
2. Select the DB cluster and choose **Actions** > **Modify**
3. In **Authentication**, enable **IAM DB authentication** and check **Apply immediately**
4. Click **Continue** then **Modify DB cluster**

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-7](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-7)
- [https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-iam-database-authentication.html](https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-iam-database-authentication.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/iam-db-authentication.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/iam-db-authentication.html#)
- [https://hub.steampipe.io/plugins/turbot/terraform/queries/neptune/neptune_cluster_iam_authentication_enabled](https://hub.steampipe.io/plugins/turbot/terraform/queries/neptune/neptune_cluster_iam_authentication_enabled)

## 技术信息

- Source Metadata：[sources/aws/neptune_cluster_iam_authentication_enabled/metadata.json](../../sources/aws/neptune_cluster_iam_authentication_enabled/metadata.json)
- Source Code：[sources/aws/neptune_cluster_iam_authentication_enabled/check.py](../../sources/aws/neptune_cluster_iam_authentication_enabled/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_iam_authentication_enabled/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_iam_authentication_enabled/check.py`

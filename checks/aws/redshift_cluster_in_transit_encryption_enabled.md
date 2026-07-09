# Redshift cluster is encrypted in transit

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `redshift_cluster_in_transit_encryption_enabled` |
| 云平台 | AWS |
| 服务 | redshift |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsRedshiftCluster |
| 资源组 | analytics |

## 描述

**Amazon Redshift clusters** enforce **encryption in transit** by requiring **TLS** for client connections when `require_ssl` is enabled. This evaluation identifies clusters where connections are not forced to use TLS.

## 风险

Allowing plaintext or optional TLS exposes SQL sessions to: - **Confidentiality** loss: credentials, queries, and results can be intercepted. - **Integrity** compromise: statements or data may be modified in transit. - **Availability** impact: session hijacking can disrupt workloads.

## 推荐措施

Require **TLS** for all Redshift connections by setting `require_ssl=true` and disallow plaintext. Configure clients to validate certificates and prefer private network paths. Keep drivers/TLS policies current. Apply **least privilege** and **defense in depth** to limit exposure if transport security fails.

## 修复步骤


### CLI

```text
aws redshift modify-cluster-parameter-group --parameter-group-name <example_resource_name> --parameters ParameterName=require_ssl,ParameterValue=true
```

### Native IaC

```yaml
# CloudFormation: Set require_ssl to true in the Redshift parameter group in use
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::ClusterParameterGroup
    Properties:
      Description: Require SSL for Redshift connections
      ParameterGroupFamily: redshift-1.0
      Parameters:
        - ParameterName: require_ssl   # CRITICAL: Enforces TLS for client connections
          ParameterValue: true         # CRITICAL: Enable SSL requirement
```

### Terraform

```hcl
# Set require_ssl to true in the Redshift parameter group used by the cluster
resource "aws_redshift_parameter_group" "<example_resource_name>" {
  name   = "<example_resource_name>"
  family = "redshift-1.0"

  parameter {
    name  = "require_ssl"   # CRITICAL: Enforces TLS for client connections
    value = "true"          # CRITICAL: Enable SSL requirement
  }
}
```

### Other

1. In the AWS Console, go to Amazon Redshift > Parameter groups
2. Open the parameter group used by your cluster
3. Click Edit parameters, set require_ssl to true, and Save
4. Reboot the cluster to apply the static parameter change

## 参考资料

- [https://docs.aws.amazon.com/redshift/latest/mgmt/security-encryption-in-transit.html](https://docs.aws.amazon.com/redshift/latest/mgmt/security-encryption-in-transit.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-2](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-2)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/redshift-parameter-groups-require-ssl.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Redshift/redshift-parameter-groups-require-ssl.html)

## 技术信息

- Source Metadata：[sources/aws/redshift_cluster_in_transit_encryption_enabled/metadata.json](../../sources/aws/redshift_cluster_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/redshift_cluster_in_transit_encryption_enabled/check.py](../../sources/aws/redshift_cluster_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_in_transit_encryption_enabled/check.py`

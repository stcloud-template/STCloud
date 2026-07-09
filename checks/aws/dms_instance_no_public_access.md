# DMS replication instance is not publicly exposed to the Internet

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dms_instance_no_public_access` |
| 云平台 | AWS |
| 服务 | dms |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Initial Access |
| 资源类型 | AwsDmsReplicationInstance |
| 资源组 | database |

## 描述

**AWS DMS replication instances** are evaluated for **public exposure**. Exposure is identified when `PubliclyAccessible` is enabled and an attached security group allows inbound traffic from any address. Private or allowlisted instances are not considered exposed.

## 风险

Publicly reachable replication instances threaten: - Confidentiality: migration data and credentials can be intercepted or exfiltrated. - Integrity: attackers may alter tasks or inject records. - Availability: abuse or DDoS can stall replication and delay cutovers.

## 推荐措施

Adopt a **private-only** design: - Disable `PubliclyAccessible`; place instances in private subnets. - Enforce **least privilege** security groups (no `0.0.0.0/0`); allow only required sources/ports. - Provide access via **VPN**, peering, or Direct Connect. - Layer controls (ACLs, monitoring) and restrict IAM to necessary actions.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: DMS instance not publicly accessible
Resources:
  <example_resource_name>:
    Type: AWS::DMS::ReplicationInstance
    Properties:
      ReplicationInstanceClass: dms.t3.micro
      PubliclyAccessible: false  # Critical: disables public access to prevent Internet exposure
```

### Terraform

```hcl
# DMS instance not publicly accessible
resource "aws_dms_replication_instance" "<example_resource_name>" {
  replication_instance_id    = "<example_resource_id>"
  replication_instance_class = "dms.t3.micro"
  publicly_accessible        = false  # Critical: disables public access to prevent Internet exposure
}
```

### Other

1. In the AWS Console, open Database Migration Service > Replication instances and select the instance
2. In Details > Networking, click each attached Security Group ID to open it in the EC2 console
3. In Inbound rules, delete any rule with Source 0.0.0.0/0 or ::/0
4. Save rules for each security group

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1)
- [https://docs.aws.amazon.com/amazonq/detector-library/terraform/restrict-public-access-dms-terraform/](https://docs.aws.amazon.com/amazonq/detector-library/terraform/restrict-public-access-dms-terraform/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/publicly-accessible.html)
- [https://support.icompaas.com/support/solutions/articles/62000233448-ensure-dms-instances-are-not-publicly-accessible](https://support.icompaas.com/support/solutions/articles/62000233448-ensure-dms-instances-are-not-publicly-accessible)

## 技术信息

- Source Metadata：[sources/aws/dms_instance_no_public_access/metadata.json](../../sources/aws/dms_instance_no_public_access/metadata.json)
- Source Code：[sources/aws/dms_instance_no_public_access/check.py](../../sources/aws/dms_instance_no_public_access/check.py)
- Source Metadata Path：`sources/aws/dms_instance_no_public_access/metadata.json`
- Source Code Path：`sources/aws/dms_instance_no_public_access/check.py`

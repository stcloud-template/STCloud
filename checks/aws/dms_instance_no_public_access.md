# DMS replication instance is not publicly exposed to the Internet

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dms_instance_no_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | dms |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Initial Access |
| リソースタイプ | AwsDmsReplicationInstance |
| リソースグループ | database |

## 説明

**AWS DMS replication instances** are evaluated for **public exposure**. Exposure is identified when `PubliclyAccessible` is enabled and an attached security group allows inbound traffic from any address. Private or allowlisted instances are not considered exposed.

## リスク

Publicly reachable replication instances threaten: - Confidentiality: migration data and credentials can be intercepted or exfiltrated. - Integrity: attackers may alter tasks or inject records. - Availability: abuse or DDoS can stall replication and delay cutovers.

## 推奨事項

Adopt a **private-only** design: - Disable `PubliclyAccessible`; place instances in private subnets. - Enforce **least privilege** security groups (no `0.0.0.0/0`); allow only required sources/ports. - Provide access via **VPN**, peering, or Direct Connect. - Layer controls (ACLs, monitoring) and restrict IAM to necessary actions.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1)
- [https://docs.aws.amazon.com/amazonq/detector-library/terraform/restrict-public-access-dms-terraform/](https://docs.aws.amazon.com/amazonq/detector-library/terraform/restrict-public-access-dms-terraform/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/publicly-accessible.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/publicly-accessible.html)
- [https://support.icompaas.com/support/solutions/articles/62000233448-ensure-dms-instances-are-not-publicly-accessible](https://support.icompaas.com/support/solutions/articles/62000233448-ensure-dms-instances-are-not-publicly-accessible)

## 技術情報

- Source Metadata：[sources/aws/dms_instance_no_public_access/metadata.json](../../sources/aws/dms_instance_no_public_access/metadata.json)
- Source Code：[sources/aws/dms_instance_no_public_access/check.py](../../sources/aws/dms_instance_no_public_access/check.py)
- Source Metadata Path：`sources/aws/dms_instance_no_public_access/metadata.json`
- Source Code Path：`sources/aws/dms_instance_no_public_access/check.py`

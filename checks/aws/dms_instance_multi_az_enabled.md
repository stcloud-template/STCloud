# DMS replication instance has Multi-AZ enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dms_instance_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | dms |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsDmsReplicationInstance |
| リソースグループ | database |

## 説明

**AWS DMS replication instances** are evaluated for **Multi-AZ** configuration. Instances with `multi_az` enabled are treated as having a cross-AZ standby; those without it are identified as single-AZ.

## リスク

Without **Multi-AZ**, a single-AZ failure or maintenance event can halt migrations, causing extended downtime (**availability**) and replication gaps or rollbacks (**integrity**). Tasks may stall, increase cutover risk, and require manual recovery when the replication instance is unavailable.

## 推奨事項

Enable **Multi-AZ** (set `multi_az` to `true`) on DMS replication instances that handle production or time-sensitive migrations to ensure redundancy and automatic failover. Apply HA principles: distribute across AZs, test failover, monitor health, and plan maintenance to minimize impact.

## 修正手順


### CLI

```text
aws dms modify-replication-instance --replication-instance-arn arn:aws:dms:<REGION>:<ACCOUNT_ID>:rep:<REPLICATION_ID> --multi-az --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable Multi-AZ on a DMS replication instance
Resources:
  <example_resource_name>:
    Type: AWS::DMS::ReplicationInstance
    Properties:
      ReplicationInstanceClass: dms.t3.micro
      MultiAZ: true  # Critical: enables Multi-AZ to pass the check
```

### Terraform

```hcl
# Enable Multi-AZ on a DMS replication instance
resource "aws_dms_replication_instance" "<example_resource_name>" {
  replication_instance_id   = "<example_resource_name>"
  replication_instance_class = "dms.t3.micro"
  multi_az                  = true  # Critical: enables Multi-AZ to pass the check
}
```

### Other

1. Open the AWS DMS console
2. Go to Replication instances and select your instance
3. Click Modify
4. Check Multi-AZ
5. Check Apply immediately
6. Click Modify to save

## 参考資料

- [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/multi-az.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/multi-az.html)

## 技術情報

- Source Metadata：[sources/aws/dms_instance_multi_az_enabled/metadata.json](../../sources/aws/dms_instance_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/dms_instance_multi_az_enabled/check.py](../../sources/aws/dms_instance_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_instance_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_instance_multi_az_enabled/check.py`

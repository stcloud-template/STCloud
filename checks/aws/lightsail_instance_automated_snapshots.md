# Lightsail instance has automated snapshots enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `lightsail_instance_automated_snapshots` |
| クラウドプラットフォーム | AWS |
| サービス | lightsail |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Effects/Data Destruction |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Amazon Lightsail instances** with **automatic daily snapshots** enabled are identified. The evaluation checks if an instance is configured to take recurring snapshots at a scheduled time.

## リスク

Absent automation, data lacks **point-in-time recovery**, increasing **availability** risk from accidental deletion, corruption, or ransomware. Failed updates or compromise hinder quick rollback, degrading **integrity** and extending RPO/RTO, causing prolonged outages.

## 推奨事項

Enable **automatic snapshots** on Lightsail instances and align the schedule with low-traffic windows. Apply **least privilege** to snapshot create/delete, and regularly test restores. Use **defense in depth**: retain multiple versions and replicate backups *for critical workloads* across regions or accounts.

## 修正手順


### CLI

```text
aws lightsail enable-add-on --region <REGION> --resource-name <example_resource_name> --add-on-request addOnType=AutoSnapshot
```

### Native IaC

```yaml
# CloudFormation: Enable automatic snapshots for a Lightsail instance
Resources:
  <example_resource_name>:
    Type: AWS::Lightsail::Instance
    Properties:
      InstanceName: <example_resource_name>
      AvailabilityZone: <example_az>
      BlueprintId: <example_blueprint_id>
      BundleId: <example_bundle_id>
      AddOns:
        - AddOnType: AutoSnapshot  # Critical: enables automatic snapshots for the instance
```

### Terraform

```hcl
# Enable automatic snapshots for a Lightsail instance
resource "aws_lightsail_instance" "<example_resource_name>" {
  name              = "<example_resource_name>"
  availability_zone = "<example_az>"
  blueprint_id      = "<example_blueprint_id>"
  bundle_id         = "<example_bundle_id>"

  add_on {
    type   = "AutoSnapshot"  # Critical: enables automatic snapshots
    status = "Enabled"       # Critical: turns the add-on on
  }
}
```

### Other

1. Open the AWS Management Console and go to Lightsail
2. Click Instances and select <example_resource_name>
3. Open the Snapshots tab
4. In Automatic snapshots, toggle On and confirm
5. (Optional) Set a snapshot time if needed; otherwise the default time is used

## 参考資料

- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-automatic-snapshot-time.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-changing-automatic-snapshot-time.html)
- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html)

## 技術情報

- Source Metadata：[sources/aws/lightsail_instance_automated_snapshots/metadata.json](../../sources/aws/lightsail_instance_automated_snapshots/metadata.json)
- Source Code：[sources/aws/lightsail_instance_automated_snapshots/check.py](../../sources/aws/lightsail_instance_automated_snapshots/check.py)
- Source Metadata Path：`sources/aws/lightsail_instance_automated_snapshots/metadata.json`
- Source Code Path：`sources/aws/lightsail_instance_automated_snapshots/check.py`

# AppStream fleet has default internet access disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `appstream_fleet_default_internet_access_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | appstream |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Amazon AppStream fleets** are assessed for the `EnableDefaultInternetAccess` setting, identifying fleets where streaming instances have default Internet connectivity.

## リスク

**Direct Internet access** gives streaming instances public exposure. Threats include: - Remote exploitation and malware, undermining **confidentiality** and **integrity** - Uncontrolled egress enabling **data exfiltration** It also enforces ~100-instance limits, reducing **availability** for high-concurrency deployments.

## 推奨事項

Disable default Internet access (`EnableDefaultInternetAccess=false`) and place fleets in **private subnets**. Provide egress via **NAT gateways** or proxies, enforce **egress filtering**, and apply **least privilege** and **zero trust** to restrict outbound traffic. Use private connectivity to AWS services where possible.

## 修正手順


### CLI

```text
aws appstream update-fleet --name <example_resource_name> --no-enable-default-internet-access
```

### Native IaC

```yaml
# CloudFormation: disable default internet access on an AppStream fleet
Resources:
  <example_resource_name>:
    Type: AWS::AppStream::Fleet
    Properties:
      Name: <example_resource_name>
      InstanceType: <INSTANCE_TYPE>
      EnableDefaultInternetAccess: false  # Critical: disables default internet access to pass the check
```

### Terraform

```hcl
# Terraform: disable default internet access on an AppStream fleet
resource "aws_appstream_fleet" "<example_resource_name>" {
  name          = "<example_resource_name>"
  instance_type = "stream.standard.small"
  image_name    = "<IMAGE_NAME>"
  compute_capacity { desired_instances = 1 }

  enable_default_internet_access = false  # Critical: disables default internet access to pass the check
}
```

### Other

1. In the AWS console, go to Amazon AppStream 2.0 > Fleets
2. Select the target fleet
3. If the fleet is RUNNING, click Actions > Stop and wait until the state is Stopped
4. Click Edit (or Modify)
5. Uncheck "Default internet access" (Disable "Enable default internet access")
6. Save/Update the fleet and start it if needed

## 参考資料

- [https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)
- [https://support.icompaas.com/support/solutions/articles/62000233540-ensure-default-internet-access-from-your-amazon-appstream-fleet-streaming-instances-remains-unchecked](https://support.icompaas.com/support/solutions/articles/62000233540-ensure-default-internet-access-from-your-amazon-appstream-fleet-streaming-instances-remains-unchecked)
- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html)
- [https://docs.aws.amazon.com/appstream2/latest/developerguide/internet-access.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/internet-access.html)

## 技術情報

- Source Metadata：[sources/aws/appstream_fleet_default_internet_access_disabled/metadata.json](../../sources/aws/appstream_fleet_default_internet_access_disabled/metadata.json)
- Source Code：[sources/aws/appstream_fleet_default_internet_access_disabled/check.py](../../sources/aws/appstream_fleet_default_internet_access_disabled/check.py)
- Source Metadata Path：`sources/aws/appstream_fleet_default_internet_access_disabled/metadata.json`
- Source Code Path：`sources/aws/appstream_fleet_default_internet_access_disabled/check.py`

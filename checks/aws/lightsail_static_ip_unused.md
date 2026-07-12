# Lightsail static IP is associated with an instance

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `lightsail_static_ip_unused` |
| クラウドプラットフォーム | AWS |
| サービス | lightsail |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Resource Consumption |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

**Amazon Lightsail static IPs** detected as **not associated** with any instance, indicating reserved but unused addresses. The evaluation focuses on the association state of each static IP to highlight potential leftovers.

## リスク

**Unattached static IPs** incur ongoing charges and indicate asset drift. If DNS or apps still reference the address, requests are blackholed, impacting **availability**. Later attaching the same IP to an unintended host can expose services and data, affecting **confidentiality** and **integrity**.

## 推奨事項

Release unused static IPs or attach them to the intended instance. Apply **least privilege** for IP allocation, enforce tagging and ownership, and run periodic audits with alerts for unattached addresses. *If reservation is required*, document purpose and set a time limit to prevent drift and cost.

## 修正手順


### CLI

```text
aws lightsail attach-static-ip --static-ip-name <example_resource_name> --instance-name <example_resource_name>
```

### Native IaC

```yaml
Resources:
  AttachStaticIp:
    Type: AWS::Lightsail::StaticIpAttachment
    Properties:
      InstanceName: <example_resource_name>  # Critical: instance to attach to; marks IP as attached
      StaticIpName: <example_resource_name>  # Critical: static IP to attach; fixes FAIL by associating it
```

### Terraform

```hcl
resource "aws_lightsail_static_ip_attachment" "attach" {
  static_ip_name = "<example_resource_name>"  # Critical: specify the static IP to attach
  instance_name  = "<example_resource_name>"  # Critical: target instance; association makes check PASS
}
```

### Other

1. In the AWS Console, go to Lightsail > Networking > Static IPs
2. Select the unused static IP and click "Attach to instance"
3. Choose the target instance and confirm
4. Verify the static IP now shows as attached

## 参考資料

- [https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.html](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-public-ip-and-private-ip-addresses-in-amazon-lightsail.html)
- [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Lightsail.html](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Lightsail.html)

## 技術情報

- Source Metadata：[sources/aws/lightsail_static_ip_unused/metadata.json](../../sources/aws/lightsail_static_ip_unused/metadata.json)
- Source Code：[sources/aws/lightsail_static_ip_unused/check.py](../../sources/aws/lightsail_static_ip_unused/check.py)
- Source Metadata Path：`sources/aws/lightsail_static_ip_unused/metadata.json`
- Source Code Path：`sources/aws/lightsail_static_ip_unused/check.py`

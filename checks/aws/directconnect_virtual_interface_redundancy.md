# Direct Connect gateway or virtual private gateway has at least two virtual interfaces on different Direct Connect connections

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `directconnect_virtual_interface_redundancy` |
| クラウドプラットフォーム | AWS |
| サービス | directconnect |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | network |

## 説明

**Direct Connect gateways** and **virtual private gateways** are assessed for **interface redundancy**: multiple virtual interfaces (`VIFs`) distributed across more than one **Direct Connect connection**. *Gateways with only one VIF or with all VIFs on a single connection are identified.*

## リスク

Missing connection diversity undermines **availability**. A single device, fiber, or location failure can cut on-prem to VPC connectivity, causing **outages**, **packet loss**, or routing blackholes. Fallback to internet VPN can add latency and throttle throughput, delaying recovery and impacting operations.

## 推奨事項

Apply connectivity **defense in depth**: - Attach at least two `VIFs` per gateway on separate **Direct Connect connections** in distinct locations - Prefer active/active dynamic routing and size capacity to survive a link loss - *Optionally* add a **VPN/Transit Gateway** path to sustain operations during provider outages

## 修正手順


### CLI

```text
aws directconnect create-private-virtual-interface --connection-id <CONNECTION_ID_DIFFERENT_FROM_EXISTING_VIF> --new-private-virtual-interface '{"virtualInterfaceName":"<NAME>","vlan":<VLAN>,"asn":<BGP_ASN>,"addressFamily":"ipv4","amazonAddress":"<AMAZON_IP/30>","customerAddress":"<CUSTOMER_IP/30>","directConnectGatewayId":"<DIRECT_CONNECT_GATEWAY_ID>"}'
```

### Terraform

```hcl
# Create a second Private VIF on a different DX connection and attach to the gateway
resource "aws_dx_private_virtual_interface" "example" {
  connection_id   = "<example_resource_id>"      # CRITICAL: use a DIFFERENT Direct Connect connection than existing VIFs
  dx_gateway_id   = "<example_resource_id>"      # CRITICAL: attaches the VIF to the Direct Connect gateway (use virtual_gateway_id for VGW)
  name            = "<NAME>"
  vlan            = 100
  bgp_asn         = 65000
  address_family  = "ipv4"
  amazon_address  = "169.254.100.1/30"
  customer_address = "169.254.100.2/30"
}
```

### Other

1. In the AWS Console, open Direct Connect
2. Go to Connections and select a different connection than the one used by your existing VIF
3. Click Create virtual interface and choose Private
4. For Gateway, select your Direct Connect gateway (or Virtual private gateway for VGW)
5. Enter VLAN, BGP ASN, and IPv4 peer IPs (Amazon/Customer), then Create
6. Verify the gateway now has at least two VIFs on different Direct Connect connections

## 参考資料

- [https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-direct-connect-location-resiliency](https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-direct-connect-location-resiliency)
- [https://repost.aws/knowledge-center/direct-connect-physical-redundancy](https://repost.aws/knowledge-center/direct-connect-physical-redundancy)
- [https://aws.amazon.com/directconnect/resiliency-recommendation/](https://aws.amazon.com/directconnect/resiliency-recommendation/)

## 技術情報

- Source Metadata：[sources/aws/directconnect_virtual_interface_redundancy/metadata.json](../../sources/aws/directconnect_virtual_interface_redundancy/metadata.json)
- Source Code：[sources/aws/directconnect_virtual_interface_redundancy/check.py](../../sources/aws/directconnect_virtual_interface_redundancy/check.py)
- Source Metadata Path：`sources/aws/directconnect_virtual_interface_redundancy/metadata.json`
- Source Code Path：`sources/aws/directconnect_virtual_interface_redundancy/check.py`

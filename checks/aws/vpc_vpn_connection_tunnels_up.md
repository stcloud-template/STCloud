# AWS Site-to-Site VPN connection has both tunnels up

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_vpn_connection_tunnels_up` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| リソースタイプ | AwsEc2ClientVpnEndpoint |
| リソースグループ | network |

## 説明

**AWS Site-to-Site VPN** connections have two IPsec tunnels. This evaluates tunnel status and detects when any tunnel is not `UP`, indicating whether both tunnels are concurrently available for high availability.

## リスク

With only one active tunnel or none, the link loses redundancy, degrading **availability** and increasing the chance of outages, session drops, or route blackholing. Failover cannot occur, disrupting critical workloads and cross-environment operations.

## 推奨事項

Maintain both tunnels healthy and ready for failover: - Deploy redundant customer gateways and resilient routing - Monitor tunnel health with alerts - Periodically test failover and document runbooks Apply **high availability** and **defense-in-depth** to avoid single points of failure.

## 修正手順


### Other

1. In the AWS Console, go to VPC > Site-to-Site VPN connections and select the VPN connection with a tunnel DOWN
2. Open the Tunnel details tab
3. For each tunnel (1 and 2), choose Actions > Download configuration, select your device/vendor, and download the config
4. On your customer gateway device, configure BOTH tunnels using the downloaded parameters (pre-shared key, IKE/IPsec settings, inside CIDR, and routing/BGP as applicable)
5. If your device requires different parameters, in the AWS console choose Actions > Modify VPN tunnel options, select the tunnel outside IP, adjust only the necessary options (for example IKE version or pre-shared key), and Save
6. Wait a few minutes and verify both tunnels show Status: UP under Tunnel details

## 参考資料

- [https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html)
- [https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html](https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_vpn_connection_tunnels_up/metadata.json](../../sources/aws/vpc_vpn_connection_tunnels_up/metadata.json)
- Source Code：[sources/aws/vpc_vpn_connection_tunnels_up/check.py](../../sources/aws/vpc_vpn_connection_tunnels_up/check.py)
- Source Metadata Path：`sources/aws/vpc_vpn_connection_tunnels_up/metadata.json`
- Source Code Path：`sources/aws/vpc_vpn_connection_tunnels_up/check.py`

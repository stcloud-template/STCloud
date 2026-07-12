# VPC peering connection route tables do not include 0.0.0.0/0 or entire requester/accepter VPC CIDR routes

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vpc_peering_routing_tables_with_least_privilege` |
| クラウドプラットフォーム | AWS |
| サービス | vpc |
| 重大度 | medium |
| カテゴリ | trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Lateral Movement, Effects/Data Exposure |
| リソースタイプ | AwsEc2VpcPeeringConnection |
| リソースグループ | network |

## 説明

**AWS VPC peering** route tables are assessed for **least-privilege routing**. Routes that target `0.0.0.0/0` or an entire peer VPC CIDR are considered overly broad; only specific subnets or narrower prefixes should be advertised across the peering link.

## リスク

Broad peering routes expand cross-VPC reachability, enabling lateral movement and unauthorized discovery, harming **confidentiality** and **integrity**. Using `0.0.0.0/0` or full-CIDR paths also increases misrouting with overlapping ranges, reducing network **availability**.

## 推奨事項

Enforce **least privilege** in peering: advertise only required subnets or more specific prefixes; avoid `0.0.0.0/0` and whole VPC ranges. Keep routes symmetric on both sides, and layer **defense in depth** with security groups and NACLs. *If broad connectivity is required*, prefer segmented designs or a transit gateway.

## 修正手順


### Native IaC

```yaml
# CloudFormation: restrict VPC peering route to a specific subnet (least privilege)
Resources:
  PeeringSpecificRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: <example_resource_id>
      DestinationCidrBlock: 10.0.1.0/24  # CRITICAL: use a specific subnet, not 0.0.0.0/0 or full VPC CIDR
      VpcPeeringConnectionId: <example_resource_id>
```

### Terraform

```hcl
# Restrict VPC peering route to a specific subnet (least privilege)
resource "aws_route" "peering_specific" {
  route_table_id             = "<example_resource_id>"
  destination_cidr_block     = "10.0.1.0/24"  # CRITICAL: specific subnet, not 0.0.0.0/0 or full VPC CIDR
  vpc_peering_connection_id  = "<example_resource_id>"
}
```

### Other

1. In AWS Console, go to VPC > Route tables
2. Select the route table(s) used to reach the peered VPC and click Routes > Edit routes
3. Delete any route to 0.0.0.0/0 or to the entire requester/accepter VPC CIDR that targets the VPC peering connection
4. Add route(s) only to required subnet CIDR(s) in the peer VPC, targeting the same VPC peering connection
5. Save changes and repeat in the peer VPC's route table(s)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/VPC/vpc-peering-access.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/VPC/vpc-peering-access.html#)
- [https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html)

## 技術情報

- Source Metadata：[sources/aws/vpc_peering_routing_tables_with_least_privilege/metadata.json](../../sources/aws/vpc_peering_routing_tables_with_least_privilege/metadata.json)
- Source Code：[sources/aws/vpc_peering_routing_tables_with_least_privilege/check.py](../../sources/aws/vpc_peering_routing_tables_with_least_privilege/check.py)
- Source Metadata Path：`sources/aws/vpc_peering_routing_tables_with_least_privilege/metadata.json`
- Source Code Path：`sources/aws/vpc_peering_routing_tables_with_least_privilege/check.py`

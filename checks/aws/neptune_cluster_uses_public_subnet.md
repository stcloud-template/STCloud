# Neptune cluster is not using public subnets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_uses_public_subnet` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | medium |
| カテゴリ | internet-exposed, trust-boundaries |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Neptune cluster is associated with one or more **public subnets**.

## リスク

A Neptune cluster in a **public subnet** increases exposure across the CIA triad: - **Confidentiality**: Direct access enables credential attacks and data exfiltration - **Integrity**: Attackers may modify or inject graph data - **Availability**: Public reachability allows DDoS or remote exploitation, causing downtime

## 推奨事項

Place Neptune clusters in **private subnets** and remove public routability to reduce attack surface. - Apply **least privilege** and network segmentation - Restrict inbound access with scoped network controls and minimal trusted paths - Enforce logging, monitoring, and private connectivity for administrative and application access

## 修正手順


### Native IaC

```yaml
Resources:
  NeptuneSubnetGroup:
    Type: AWS::Neptune::DBSubnetGroup
    Properties:
      DBSubnetGroupDescription: "Private subnets for Neptune"
      SubnetIds:  # Use only private subnet IDs to prevent public access
        - <PRIVATE_SUBNET_ID_1>
        - <PRIVATE_SUBNET_ID_2>

  NeptuneDBCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBSubnetGroupName: !Ref NeptuneSubnetGroup  # Associate cluster with private subnet group
```

### Terraform

```hcl
resource "aws_neptune_subnet_group" "neptune" {
  name       = "neptune-private-subnets"
  subnet_ids = ["<PRIVATE_SUBNET_ID_1>", "<PRIVATE_SUBNET_ID_2>"]  # Use only private subnet IDs to prevent public access
}

resource "aws_neptune_cluster" "example_cluster" {
  neptune_subnet_group_name = aws_neptune_subnet_group.neptune.name  # Associate cluster with private subnet group
}
```

### Other

1. Open the AWS Console and go to Amazon Neptune > Subnet groups
2. Click Create DB Subnet Group
3. Enter a name and description, select the VPC, and add only private subnet IDs (at least two)
4. Click Create
5. Go to Amazon Neptune > DB clusters > Select the cluster > Actions > Modify
6. Set DB subnet group to the newly created subnet group and save (Apply immediately if required)
7. Verify the cluster subnet group now lists only private subnets

## 参考資料

- [https://docs.aws.amazon.com/neptune/latest/userguide/get-started-vpc.html](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-vpc.html)
- [https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-endpoints.html](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-endpoints.html)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_uses_public_subnet/metadata.json](../../sources/aws/neptune_cluster_uses_public_subnet/metadata.json)
- Source Code：[sources/aws/neptune_cluster_uses_public_subnet/check.py](../../sources/aws/neptune_cluster_uses_public_subnet/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_uses_public_subnet/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_uses_public_subnet/check.py`

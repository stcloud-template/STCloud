# ELBv2 Network or Gateway Load Balancer has cross-zone load balancing enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elbv2_cross_zone_load_balancing_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elbv2 |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsElbv2LoadBalancer |
| リソースグループ | network |

## 説明

**Network and Gateway Load Balancers** have **cross-zone load balancing** enabled (`load_balancing.cross_zone.enabled`), so each node distributes requests to targets in all enabled Availability Zones rather than only its own.

## リスク

Without cross-zone distribution, traffic can concentrate in one zone, degrading **availability** through target saturation, uneven failover, and connection drops. Zonal impairment can cause partial outages and increase **latency** under load.

## 推奨事項

Enable **cross-zone load balancing** to spread load across zones and design for AZ redundancy. - Balance capacity per AZ and use health-based routing - Avoid single-AZ dependencies and sticky designs - Monitor zonal health to sustain **fault tolerance**

## 修正手順


### CLI

```text
aws elbv2 modify-load-balancer-attributes --load-balancer-arn <load-balancer-arn> --attributes Key=load_balancing.cross_zone.enabled,Value=true
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Type: network
      Subnets:
        - <subnet-id-1>
        - <subnet-id-2>
      LoadBalancerAttributes:
        - Key: load_balancing.cross_zone.enabled  # Critical: enable cross-zone load balancing
          Value: true  # Ensures the check passes for NLB/GLB
```

### Terraform

```hcl
resource "aws_lb" "<example_resource_name>" {
  load_balancer_type = "network"
  subnets            = ["<subnet-id-1>", "<subnet-id-2>"]
  enable_cross_zone_load_balancing = true  # Critical: enable cross-zone load balancing
}
```

### Other

1. Open the AWS EC2 console and go to Load Balancers
2. Select your Network or Gateway Load Balancer
3. Choose the Attributes tab > Edit attributes
4. Turn on Cross-zone load balancing
5. Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-cross-zone-load-balancing.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-cross-zone-load-balancing.html#)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing)

## 技術情報

- Source Metadata：[sources/aws/elbv2_cross_zone_load_balancing_enabled/metadata.json](../../sources/aws/elbv2_cross_zone_load_balancing_enabled/metadata.json)
- Source Code：[sources/aws/elbv2_cross_zone_load_balancing_enabled/check.py](../../sources/aws/elbv2_cross_zone_load_balancing_enabled/check.py)
- Source Metadata Path：`sources/aws/elbv2_cross_zone_load_balancing_enabled/metadata.json`
- Source Code Path：`sources/aws/elbv2_cross_zone_load_balancing_enabled/check.py`

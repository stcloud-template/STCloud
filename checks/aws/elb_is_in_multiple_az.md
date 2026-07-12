# Classic Load Balancer is in multiple Availability Zones

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elb_is_in_multiple_az` |
| クラウドプラットフォーム | AWS |
| サービス | elb |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsElbLoadBalancer |
| リソースグループ | network |

## 説明

**Classic Load Balancer** spans at least the configured number of **Availability Zones**. The evaluation identifies load balancers enabled in fewer AZs than the specified minimum.

## リスク

Operating in too few AZs makes the load balancer a **single point of failure**. An AZ outage or zonal degradation can cause **service unavailability**, dropped connections, and uneven capacity, undermining application **availability** and resilience and increasing recovery time.

## 推奨事項

Design for **multi-AZ high availability**: - Enable at least `2` AZs per load balancer - Distribute targets evenly and use Auto Scaling across AZs - Enable **cross-zone load balancing** to smooth imbalances - Regularly test failover and health thresholds Apply **fault isolation** and **defense in depth** principles.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Ensure CLB spans at least two Availability Zones by adding two subnets
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      Subnets:
        - <example_subnet_id_a>  # Critical: add a subnet in AZ A to ensure multiple AZs
        - <example_subnet_id_b>  # Critical: add a subnet in a different AZ (>=2 AZs total)
      Listeners:
        - LoadBalancerPort: 80
          InstancePort: 80
          Protocol: HTTP
```

### Terraform

```hcl
# Terraform: Ensure CLB spans at least two Availability Zones by adding two subnets
resource "aws_elb" "<example_resource_name>" {
  name    = "<example_resource_name>"
  subnets = [
    "<example_subnet_id_a>", # Critical: subnet in AZ A to ensure multiple AZs
    "<example_subnet_id_b>"  # Critical: subnet in different AZ (>=2 AZs total)
  ]

  listener {
    lb_port        = 80
    lb_protocol    = "http"
    instance_port  = 80
  }
}
```

### Other

1. Open the Amazon EC2 console and go to Load Balancers
2. Select your Classic Load Balancer (type: classic)
3. Choose Edit subnets (or the Subnets tab > Edit)
4. Add a subnet from a different Availability Zone than the existing one (ensure at least two AZs)
5. Click Save
6. If your CLB is in EC2-Classic, use Edit Availability Zones instead and select an additional AZ, then Save

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/ec2-instances-distribution-across-availability-zones.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/ec2-instances-distribution-across-availability-zones.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html#classic-load-balancer-overview](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html#classic-load-balancer-overview)

## 技術情報

- Source Metadata：[sources/aws/elb_is_in_multiple_az/metadata.json](../../sources/aws/elb_is_in_multiple_az/metadata.json)
- Source Code：[sources/aws/elb_is_in_multiple_az/check.py](../../sources/aws/elb_is_in_multiple_az/check.py)
- Source Metadata Path：`sources/aws/elb_is_in_multiple_az/metadata.json`
- Source Code Path：`sources/aws/elb_is_in_multiple_az/check.py`

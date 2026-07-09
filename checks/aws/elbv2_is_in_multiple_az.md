# ELBv2 load balancer is configured across multiple Availability Zones

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_is_in_multiple_az` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

ELBv2 load balancers (Application, Network, or Gateway) are assessed for distribution across multiple **Availability Zones**. The finding indicates whether each load balancer spans at least the configured minimum number of AZs (default `2`).

## 风险

Limiting a load balancer to one AZ introduces a single point of failure. An AZ outage, zonal degradation, or imbalanced target capacity can cause downtime, dropped connections, and deployment risk, undermining service **availability** and resiliency.

## 推荐措施

Operate each load balancer across at least **two AZs** and ensure every enabled AZ has healthy, scaled targets. - Distribute capacity per AZ; use autoscaling - Keep health checks effective - Consider cross-zone load balancing to absorb bursts - Regularly test failover

## 修复步骤


### CLI

```text
aws elbv2 set-subnets --load-balancer-arn <LOAD_BALANCER_ARN> --subnets <SUBNET_ID_A> <SUBNET_ID_B>
```

### Native IaC

```yaml
# CloudFormation: ensure the ELBv2 spans at least two AZs by specifying two subnets
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets:
        - <subnet_id_a>  # critical: add a second AZ/subnet
        - <subnet_id_b>  # critical: ensures the load balancer spans >=2 AZs
```

### Terraform

```hcl
# Ensure ELBv2 spans at least two Availability Zones
resource "aws_lb" "<example_resource_name>" {
  subnets = [
    "<subnet_id_a>",  # critical: add a second AZ/subnet
    "<subnet_id_b>"   # critical: ensures the load balancer spans >=2 AZs
  ]
}
```

### Other

1. Open AWS Console > EC2 > Load Balancers
2. Select the load balancer
3. Go to the Network mapping tab and click Edit subnets
4. Enable at least two Availability Zones by selecting one subnet in each of two AZs
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/network/availability-zones.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/availability-zones.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-multi-az.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-multi-az.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#availability-zones](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#availability-zones)

## 技术信息

- Source Metadata：[sources/aws/elbv2_is_in_multiple_az/metadata.json](../../sources/aws/elbv2_is_in_multiple_az/metadata.json)
- Source Code：[sources/aws/elbv2_is_in_multiple_az/check.py](../../sources/aws/elbv2_is_in_multiple_az/check.py)
- Source Metadata Path：`sources/aws/elbv2_is_in_multiple_az/metadata.json`
- Source Code Path：`sources/aws/elbv2_is_in_multiple_az/check.py`

# Classic Load Balancer has cross-zone load balancing enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_cross_zone_load_balancing_enabled` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service, Effects/Resource Consumption |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

Classic Load Balancer with **cross-zone load balancing** distributes requests across registered targets in all enabled Availability Zones. This evaluates whether that setting is `enabled`, instead of restricting distribution to targets within only the same zone.

## 风险

Without **cross-zone load balancing**, traffic can concentrate in one AZ due to DNS skew or uneven capacity, creating **hot spots**, timeouts, and latency. This degrades service **availability** and increases the chance of cascading failures during AZ impairment or instance loss.

## 推荐措施

Set `cross-zone load balancing` to `enabled` on Classic Load Balancers and use at least two AZs. Balance capacity per AZ, enforce robust health checks with autoscaling, and design for **high availability** so load remains evenly distributed during demand spikes or partial AZ outages.

## 修复步骤


### CLI

```text
aws elb modify-load-balancer-attributes --load-balancer-name <load-balancer-name> --load-balancer-attributes "{\"CrossZoneLoadBalancing\":{\"Enabled\":true}}"
```

### Native IaC

```yaml
# CloudFormation: Enable cross-zone load balancing on a Classic Load Balancer
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      CrossZone: true  # Critical: enables cross-zone load balancing to pass the check
      Listeners:
        - LoadBalancerPort: 80
          InstancePort: 80
          Protocol: HTTP
      AvailabilityZones:
        - <example_az>
```

### Terraform

```hcl
# Terraform: Enable cross-zone load balancing on a Classic Load Balancer
resource "aws_elb" "<example_resource_name>" {
  name = "<example_resource_name>"

  listener {
    lb_port           = 80
    lb_protocol       = "http"
    instance_port     = 80
    instance_protocol = "http"
  }

  availability_zones = ["<example_az>"]

  cross_zone_load_balancing = true  # Critical: enables cross-zone load balancing to pass the check
}
```

### Other

1. Open the AWS EC2 console
2. Go to Load Balancing > Load Balancers and select your Classic Load Balancer
3. Open the Attributes tab and click Edit
4. Enable Cross-zone load balancing
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-9](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-9)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-cross-zone-load-balancing-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-cross-zone-load-balancing-enabled.html)

## 技术信息

- Source Metadata：[sources/aws/elb_cross_zone_load_balancing_enabled/metadata.json](../../sources/aws/elb_cross_zone_load_balancing_enabled/metadata.json)
- Source Code：[sources/aws/elb_cross_zone_load_balancing_enabled/check.py](../../sources/aws/elb_cross_zone_load_balancing_enabled/check.py)
- Source Metadata Path：`sources/aws/elb_cross_zone_load_balancing_enabled/metadata.json`
- Source Code Path：`sources/aws/elb_cross_zone_load_balancing_enabled/check.py`

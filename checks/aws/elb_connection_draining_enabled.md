# Classic Load Balancer has connection draining enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_connection_draining_enabled` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Denial of Service |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

**Classic Load Balancer** has **connection draining** enabled, so deregistering or unhealthy instances stop receiving new requests while existing connections are allowed to complete within the configured drain window.

## 风险

Without **connection draining**, instance removals or health failures can terminate in-flight requests, leading to partial transactions, broken sessions, and inconsistent application state. This reduces **availability** and can impact **data integrity** during deployments, scaling, or failover events.

## 推荐措施

Enable **connection draining** on all Classic Load Balancers and set a drain interval aligned to typical request latency. Coordinate autoscaling and deployments to allow graceful instance shutdowns. Monitor errors and retries to validate behavior and adjust the `timeout` conservatively to protect **availability** and **integrity**.

## 修复步骤


### CLI

```text
aws elb modify-load-balancer-attributes --load-balancer-name <example_resource_name> --load-balancer-attributes '{"ConnectionDraining":{"Enabled":true}}'
```

### Native IaC

```yaml
# CloudFormation: Enable connection draining on a Classic Load Balancer
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      Listeners:
        - InstancePort: 80
          LoadBalancerPort: 80
          Protocol: HTTP
      AvailabilityZones:
        - us-east-1a
      ConnectionDrainingPolicy:
        Enabled: true  # CRITICAL: turns on connection draining so in-flight requests complete
        # Timeout is optional; default 300s is used if omitted
```

### Terraform

```hcl
# Terraform: Enable connection draining on a Classic Load Balancer
resource "aws_elb" "<example_resource_name>" {
  name               = "<example_resource_name>"
  availability_zones = ["us-east-1a"]

  listener {
    lb_port           = 80
    lb_protocol       = "http"
    instance_port     = 80
    instance_protocol = "http"
  }

  connection_draining = true  # CRITICAL: enables connection draining so existing connections complete
  # connection_draining_timeout can be omitted (defaults to 300s)
}
```

### Other

1. Open the EC2 console and go to Load Balancers (Classic)
2. Select the Classic Load Balancer
3. Choose the Attributes tab, then click Edit
4. Check Enable connection draining (leave default timeout or set as needed)
5. Click Save changes

## 参考资料

- [https://aws.amazon.com/blogs/aws/elb-connection-draining-remove-instances-from-service-with-care/](https://aws.amazon.com/blogs/aws/elb-connection-draining-remove-instances-from-service-with-care/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-connection-draining-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-connection-draining-enabled.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-7](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-7)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html)

## 技术信息

- Source Metadata：[sources/aws/elb_connection_draining_enabled/metadata.json](../../sources/aws/elb_connection_draining_enabled/metadata.json)
- Source Code：[sources/aws/elb_connection_draining_enabled/check.py](../../sources/aws/elb_connection_draining_enabled/check.py)
- Source Metadata Path：`sources/aws/elb_connection_draining_enabled/metadata.json`
- Source Code Path：`sources/aws/elb_connection_draining_enabled/check.py`

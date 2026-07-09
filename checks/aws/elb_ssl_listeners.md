# Elastic Load Balancer has only HTTPS or SSL listeners

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_ssl_listeners` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Effects/Data Exposure |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

**Elastic Load Balancers** are assessed for client-facing listener protocols. Only `HTTPS` or `SSL` are considered encrypted; any `HTTP` or `TCP` listener indicates plaintext between clients and the load balancer.

## 风险

Plaintext listeners enable network eavesdropping and content injection, compromising **confidentiality** and **integrity**. Attackers on public or untrusted paths can harvest credentials and session tokens or alter traffic via MITM, leading to data exposure and unauthorized access.

## 推荐措施

Enforce **encryption in transit** by using only `HTTPS`/`TLS` listeners. Redirect `HTTP` to `HTTPS` and retire plaintext listeners. Use trusted certificates (e.g., ACM) and modern TLS policies; align with **zero trust** and **defense in depth**. *If needed*, use end-to-end TLS to targets and monitor certificate health.

## 修复步骤


### CLI

```text
aws elb delete-load-balancer-listeners --load-balancer-name <lb_name> --load-balancer-ports 80
```

### Native IaC

```yaml
# CloudFormation: Classic ELB with only encrypted (HTTPS) listener
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - <example_az>
      Listeners:
        - Protocol: HTTPS           # CRITICAL: enforce encrypted listener
          LoadBalancerPort: 443
          InstanceProtocol: HTTP
          InstancePort: 80
          SSLCertificateId: <certificate_arn>  # CRITICAL: required for HTTPS termination
```

### Terraform

```hcl
# Classic ELB with only encrypted (HTTPS) listener
resource "aws_elb" "<example_resource_name>" {
  availability_zones = ["<example_az>"]

  listener {
    lb_port            = 443
    lb_protocol        = "https"   # CRITICAL: enforce encrypted listener
    instance_port      = 80
    instance_protocol  = "http"
    ssl_certificate_id = "<certificate_arn>"  # CRITICAL: required for HTTPS/SSL
  }
}
```

### Other

1. In the AWS console, go to EC2 > Load Balancers (Classic)
2. Select the load balancer and open the Listeners tab
3. Click Edit and remove any listener with Protocol HTTP or TCP
4. Add a listener with Protocol HTTPS (port 443) and select an SSL certificate
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-listener-security.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-listener-security.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html)

## 技术信息

- Source Metadata：[sources/aws/elb_ssl_listeners/metadata.json](../../sources/aws/elb_ssl_listeners/metadata.json)
- Source Code：[sources/aws/elb_ssl_listeners/check.py](../../sources/aws/elb_ssl_listeners/check.py)
- Source Metadata Path：`sources/aws/elb_ssl_listeners/metadata.json`
- Source Code Path：`sources/aws/elb_ssl_listeners/check.py`

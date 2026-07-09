# ELBv2 Network Load Balancer has TLS termination enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_nlb_tls_termination_enabled` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

**Network Load Balancers** with listeners using the `TLS` protocol indicate **TLS termination** at the load balancer. The evaluation identifies NLBs that have at least one `TLS` listener versus those using plain `TCP`/`UDP` or deferring encryption to targets.

## 风险

Lack of NLB-level TLS termination can leave transit data unencrypted or managed inconsistently on instances, undermining **confidentiality** and **integrity**. It also shifts handshake CPU cost to targets, reducing **availability** and making them more susceptible to connection floods and downgrade or weak-cipher exposures.

## 推荐措施

Enable **TLS listeners** to terminate client encryption at the NLB and enforce centralized, modern cipher policies and certificate rotation. Apply **defense in depth** by re-encrypting to targets when needed, limit backend access to the NLB, and automate certificate lifecycle with secure storage and monitoring for deprecated protocols.

## 修复步骤


### CLI

```text
aws elbv2 create-listener --load-balancer-arn <nlb_arn> --protocol TLS --port 443 --ssl-policy ELBSecurityPolicy-TLS13-1-2-2021-06 --certificates CertificateArn=<certificate_arn> --default-actions Type=forward,TargetGroupArn=<target_group_arn>
```

### Native IaC

```yaml
# CloudFormation: Add a TLS listener to enable TLS termination on the NLB
Resources:
  "<example_resource_name>":
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: "<example_resource_arn>"
      Protocol: TLS  # critical: enables TLS termination on the NLB
      Port: 443
      SslPolicy: ELBSecurityPolicy-TLS13-1-2-2021-06  # critical: required when Protocol is TLS
      Certificates:
        - CertificateArn: "<example_resource_arn>"  # critical: server certificate for TLS termination
      DefaultActions:
        - Type: forward
          TargetGroupArn: "<example_resource_arn>"
```

### Terraform

```hcl
# Terraform: Add a TLS listener to enable TLS termination on the NLB
resource "aws_lb_listener" "<example_resource_name>" {
  load_balancer_arn = "<example_resource_arn>"
  port              = 443
  protocol          = "TLS"  # critical: enables TLS termination
  ssl_policy        = "ELBSecurityPolicy-TLS13-1-2-2021-06"  # critical: required for TLS
  certificate_arn   = "<example_resource_arn>"  # critical: server certificate for TLS termination

  default_action {
    type             = "forward"
    target_group_arn = "<example_resource_arn>"
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancers and select your Network Load Balancer
2. Open the Listeners tab and click Add listener
3. Set Protocol to TLS and Port to 443
4. Select an ACM certificate and a security policy
5. Set Default action to Forward to your target group
6. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/network/listener-update-rules.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/listener-update-rules.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-listener-security.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-listener-security.html#)

## 技术信息

- Source Metadata：[sources/aws/elbv2_nlb_tls_termination_enabled/metadata.json](../../sources/aws/elbv2_nlb_tls_termination_enabled/metadata.json)
- Source Code：[sources/aws/elbv2_nlb_tls_termination_enabled/check.py](../../sources/aws/elbv2_nlb_tls_termination_enabled/check.py)
- Source Metadata Path：`sources/aws/elbv2_nlb_tls_termination_enabled/metadata.json`
- Source Code Path：`sources/aws/elbv2_nlb_tls_termination_enabled/check.py`

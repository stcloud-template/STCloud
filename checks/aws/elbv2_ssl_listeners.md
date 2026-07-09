# ELBv2 Application Load Balancer listeners use HTTPS or redirect HTTP to HTTPS

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_ssl_listeners` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

**Application Load Balancer listeners** are assessed for **encrypted ingress**: either only `HTTPS` listeners are present, or any `HTTP` listener redirects to `HTTPS`.

## 风险

Exposed `HTTP` paths allow traffic to travel in plaintext, enabling interception, credential theft, session hijacking, and response tampering. This weakens confidentiality and integrity and makes **MITM** on public or shared networks feasible.

## 推荐措施

Enforce **TLS everywhere**: use `HTTPS` listeners and make all `HTTP` listeners redirect to `HTTPS` only. Do not forward plaintext. Apply **defense in depth** with strong TLS policies and managed certificates, and consider `HSTS` to prevent users from reaching `http`.

## 修复步骤


### CLI

```text
aws elbv2 modify-listener --listener-arn <listener_arn> --default-actions '[{"Type":"redirect","RedirectConfig":{"Protocol":"HTTPS","Port":"443","StatusCode":"HTTP_301"}}]'
```

### Native IaC

```yaml
# CloudFormation: Redirect HTTP listener to HTTPS
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      LoadBalancerArn: <example_resource_id>
      Protocol: HTTP
      Port: 80
      DefaultActions:
        - Type: redirect
          RedirectConfig:
            Protocol: HTTPS  # Critical: redirect HTTP to HTTPS
            Port: '443'      # Critical: target HTTPS port
            StatusCode: HTTP_301  # Critical: enforce redirect
```

### Terraform

```hcl
# Terraform: Redirect HTTP listener to HTTPS
resource "aws_lb_listener" "<example_resource_name>" {
  load_balancer_arn = "<example_resource_id>"
  protocol          = "HTTP"
  port              = 80

  default_action {
    type = "redirect"
    redirect {
      protocol   = "HTTPS"   # Critical: redirect to HTTPS
      port       = "443"     # Critical: target HTTPS port
      status_code = "HTTP_301" # Critical: enforce redirect
    }
  }
}
```

### Other

1. Open the EC2 console and go to Load Balancers
2. Select the Application Load Balancer and open the Listeners tab
3. Select the HTTP:80 listener and choose Edit (or View/edit rules)
4. Set the default action to Redirect to, Protocol: HTTPS, Port: 443, Status code: HTTP_301
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)

## 技术信息

- Source Metadata：[sources/aws/elbv2_ssl_listeners/metadata.json](../../sources/aws/elbv2_ssl_listeners/metadata.json)
- Source Code：[sources/aws/elbv2_ssl_listeners/check.py](../../sources/aws/elbv2_ssl_listeners/check.py)
- Source Metadata Path：`sources/aws/elbv2_ssl_listeners/metadata.json`
- Source Code Path：`sources/aws/elbv2_ssl_listeners/check.py`

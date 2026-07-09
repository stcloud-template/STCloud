# Elastic Load Balancer has access logs to S3 configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elb_logging_enabled` |
| 云平台 | AWS |
| 服务 | elb |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsElbLoadBalancer |
| 资源组 | network |

## 描述

**Elastic Load Balancers** have **access logs** configured to deliver request metadata (client IPs, paths, status, TLS details) to **Amazon S3**

## 风险

Without **ELB access logs**, you lose **visibility** into edge traffic, reducing detection of reconnaissance, brute-force, and exploitation attempts. This hampers forensics and incident timelines, risking undetected data exfiltration (confidentiality), untraceable changes (integrity), and delayed response to outages or DDoS (availability).

## 推荐措施

Enable **access logs** to Amazon S3 (`access_logs.s3.enabled=true`). Apply **least privilege** bucket policies, encrypt objects, and restrict read access. Define lifecycle retention and centralize analysis. Monitor for delivery failures and alert on anomalies. Standardize across all load balancers via IaC as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws elb modify-load-balancer-attributes --load-balancer-name <lb_name> --load-balancer-attributes AccessLog={Enabled=true,S3BucketName=<bucket_name>}
```

### Native IaC

```yaml
# CloudFormation: Enable access logs for a Classic Load Balancer (CLB)
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      Listeners:
        - LoadBalancerPort: 80
          InstancePort: 80
          Protocol: HTTP
      AvailabilityZones:
        - <example_resource_id>
      AccessLoggingPolicy:               # CRITICAL: Enables S3 access logs
        Enabled: true                    # CRITICAL: Turn on access logging
        S3BucketName: <example_resource_name>  # CRITICAL: S3 bucket to store logs
```

### Terraform

```hcl
# Enable access logs for an ELBv2 load balancer (minimal)
resource "aws_lb" "<example_resource_name>" {
  load_balancer_type = "network"
  subnets            = ["<example_resource_id>", "<example_resource_id>"]

  access_logs {                   # CRITICAL: Enables S3 access logs
    bucket  = "<example_resource_name>"  # CRITICAL: S3 bucket for logs
    enabled = true                 # CRITICAL: Turn on access logging
  }
}
```

### Other

1. In the AWS Console, go to EC2 > Load Balancers
2. Select the load balancer and choose Edit attributes (or the Attributes tab)
3. Turn on Access logs
4. Enter the S3 URI (e.g., s3://<bucket_name>)
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/network/enable-access-logs.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/enable-access-logs.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElasticBeanstalk/enable-access-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElasticBeanstalk/enable-access-logs.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html)

## 技术信息

- Source Metadata：[sources/aws/elb_logging_enabled/metadata.json](../../sources/aws/elb_logging_enabled/metadata.json)
- Source Code：[sources/aws/elb_logging_enabled/check.py](../../sources/aws/elb_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/elb_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/elb_logging_enabled/check.py`

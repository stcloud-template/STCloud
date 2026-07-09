# ELBv2 Application Load Balancer has access logs to S3 configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elbv2_logging_enabled` |
| 云平台 | AWS |
| 服务 | elbv2 |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsElbv2LoadBalancer |
| 资源组 | network |

## 描述

**ELBv2 Application Load Balancers** are evaluated for **access logging** enabled to Amazon S3, capturing request details such as timestamps, client IPs, paths, and response codes.

## 风险

Absent **ALB access logs** reduces **visibility** and hampers **incident detection** and **forensics**. Malicious requests, credential stuffing, or data exfiltration via the load balancer can go unnoticed, undermining **confidentiality** and **integrity**, and delaying recovery from **availability** incidents.

## 推荐措施

Enable **ALB access logging** to a dedicated, encrypted S3 bucket. Apply **least privilege** to the bucket for delivery and readers, set lifecycle policies for retention, and consider `Object Lock` to deter tampering. Centralize logs in a **SIEM** and alert on anomalies as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws elbv2 modify-load-balancer-attributes --load-balancer-arn <lb_arn> --attributes Key=access_logs.s3.enabled,Value=true Key=access_logs.s3.bucket,Value=<bucket_name>
```

### Native IaC

```yaml
# CloudFormation: enable ALB access logs to S3
Resources:
  <example_resource_name>:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets:
        - <subnet_id_1>
        - <subnet_id_2>
      SecurityGroups:
        - <example_security_group_id>
      LoadBalancerAttributes:
        - Key: access_logs.s3.enabled  # critical: enable ALB access logging
          Value: "true"
        - Key: access_logs.s3.bucket   # critical: destination S3 bucket for logs
          Value: "<example_resource_name>"
```

### Terraform

```hcl
# Terraform: enable ALB access logs to S3
resource "aws_lb" "<example_resource_name>" {
  name            = "<example_resource_name>"
  security_groups = ["<example_security_group_id>"]
  subnets         = ["<subnet_id_1>", "<subnet_id_2>"]

  access_logs {
    bucket  = "<example_resource_name>"  # critical: destination S3 bucket for logs
    enabled = true                        # critical: enable ALB access logging
  }
}
```

### Other

1. In AWS Console, go to EC2 > Load Balancers and select your Application Load Balancer
2. Open the Attributes (or Edit attributes) section and find Access logs
3. Check Enable access logs and choose the S3 bucket for delivery
4. Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/access-log.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/access-log.html)

## 技术信息

- Source Metadata：[sources/aws/elbv2_logging_enabled/metadata.json](../../sources/aws/elbv2_logging_enabled/metadata.json)
- Source Code：[sources/aws/elbv2_logging_enabled/check.py](../../sources/aws/elbv2_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/elbv2_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/elbv2_logging_enabled/check.py`

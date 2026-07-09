# CloudFront distribution uses an AWS WAF web ACL

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudfront_distributions_using_waf` |
| 云平台 | AWS |
| 服务 | cloudfront |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS |
| 资源类型 | AwsCloudFrontDistribution |
| 资源组 | network |

## 描述

**CloudFront distributions** are assessed for an associated **AWS WAF** web ACL that inspects and filters HTTP/S requests at the edge. The finding highlights distributions without this web ACL association.

## 风险

Absent **WAF** on Internet-facing distributions exposes apps to layer-7 threats: SQLi/XSS and bot abuse can cause data exfiltration (**confidentiality**), unauthorized actions (**integrity**), and request floods that overload origins (**availability**). It may also raise egress and compute costs.

## 推荐措施

Associate each distribution with an **AWS WAF web ACL** and apply defense-in-depth: - Use managed rule groups and rate limits - Add IP/geo and bot controls as needed - Enable logging, test new rules in `count` mode, and tune - Monitor metrics and update rules Align controls with **least privilege** for requests.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: associate an AWS WAFv2 Web ACL with a CloudFront distribution
Resources:
  <example_distribution>:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        Origins:
          - Id: origin1
            DomainName: <example_origin_domain>
            S3OriginConfig: {}
        DefaultCacheBehavior:
          TargetOriginId: origin1
          ViewerProtocolPolicy: redirect-to-https
          ForwardedValues:
            QueryString: false
        WebACLId: <example_web_acl_arn>  # CRITICAL: Associates the WAFv2 Web ACL (ARN) to this distribution
        # This makes the distribution PASS by enabling WAF protection
```

### Terraform

```hcl
# Add this to the existing CloudFront distribution resource
resource "aws_cloudfront_distribution" "<example_resource_name>" {
  web_acl_id = "<example_web_acl_arn>"  # CRITICAL: Associates the WAFv2 Web ACL (ARN) to the distribution to PASS the check
}
```

### Other

1. In the AWS Console, go to CloudFront > Distributions and select your distribution
2. Click Edit (General/Settings)
3. Set AWS WAF Web ACL to your Web ACL (scope: Global/CloudFront)
4. Click Save/Yes, Edit and wait for Deployment to complete
5. If no Web ACL exists: go to WAF & Shield > Web ACLs (scope: CloudFront), Create web ACL, then repeat steps 1-4 to associate it

## 参考资料

- [https://repost.aws/questions/QUTY5hPVxgS6Caa3eZHX7-nQ/waf-on-alb-or-cloudfront](https://repost.aws/questions/QUTY5hPVxgS6Caa3eZHX7-nQ/waf-on-alb-or-cloudfront)
- [https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-integrated-with-waf.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFront/cloudfront-integrated-with-waf.html)

## 技术信息

- Source Metadata：[sources/aws/cloudfront_distributions_using_waf/metadata.json](../../sources/aws/cloudfront_distributions_using_waf/metadata.json)
- Source Code：[sources/aws/cloudfront_distributions_using_waf/check.py](../../sources/aws/cloudfront_distributions_using_waf/check.py)
- Source Metadata Path：`sources/aws/cloudfront_distributions_using_waf/metadata.json`
- Source Code Path：`sources/aws/cloudfront_distributions_using_waf/check.py`

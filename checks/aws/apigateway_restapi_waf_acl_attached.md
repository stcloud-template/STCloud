# API Gateway stage has a WAF Web ACL attached

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apigateway_restapi_waf_acl_attached` |
| 云平台 | AWS |
| 服务 | apigateway |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsApiGatewayStage |
| 资源组 | api_gateway |

## 描述

**Amazon API Gateway (REST API)** stages are assessed for an associated **AWS WAF web ACL**. The finding reflects whether a `web ACL` is linked at the stage level.

## 风险

Absent a **WAF web ACL**, APIs are exposed to application-layer threats that impact CIA: - Confidentiality: data exfiltration via injection - Integrity: parameter tampering and path traversal - Availability: L7 floods, bot abuse, resource exhaustion *Public endpoints face heightened risk.*

## 推荐措施

Attach an **AWS WAF web ACL** to each exposed stage and apply **defense in depth**: - Use managed rule groups and tailored allow/deny lists - Apply rate limiting to throttle abuse - Enforce least-privilege network exposure - Continuously tune rules using logs and metrics *Validate changes to reduce false positives.*

## 修复步骤


### CLI

```text
aws wafv2 associate-web-acl --web-acl-arn <WEB_ACL_ARN> --resource-arn arn:aws:apigateway:<REGION>::/restapis/<REST_API_ID>/stages/<STAGE_NAME>
```

### Native IaC

```yaml
# CloudFormation: Attach a WAFv2 Web ACL to an API Gateway REST API stage
Resources:
  <example_resource_name>:
    Type: AWS::WAFv2::WebACLAssociation
    Properties:
      ResourceArn: arn:aws:apigateway:<example_region>::/restapis/<example_resource_id>/stages/<example_stage_name>  # CRITICAL: target API Gateway stage
      WebACLArn: <example_resource_arn>  # CRITICAL: Web ACL to attach
```

### Terraform

```hcl
# Attach a WAFv2 Web ACL to an API Gateway REST API stage
resource "aws_wafv2_web_acl_association" "<example_resource_name>" {
  resource_arn = "arn:aws:apigateway:<example_region>::/restapis/<example_resource_id>/stages/<example_stage_name>" # CRITICAL: target API Gateway stage
  web_acl_arn  = "<example_resource_arn>" # CRITICAL: Web ACL to attach
}
```

### Other

1. Open the AWS Console and go to WAF & Shield
2. Select Web ACLs (Scope: Regional), choose your Web ACL
3. Click Add AWS resource
4. Select API Gateway, choose the REST API and the specific Stage
5. Click Add/Associate to attach the Web ACL

## 参考资料

- [https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-monitoring.html)

## 技术信息

- Source Metadata：[sources/aws/apigateway_restapi_waf_acl_attached/metadata.json](../../sources/aws/apigateway_restapi_waf_acl_attached/metadata.json)
- Source Code：[sources/aws/apigateway_restapi_waf_acl_attached/check.py](../../sources/aws/apigateway_restapi_waf_acl_attached/check.py)
- Source Metadata Path：`sources/aws/apigateway_restapi_waf_acl_attached/metadata.json`
- Source Code Path：`sources/aws/apigateway_restapi_waf_acl_attached/check.py`

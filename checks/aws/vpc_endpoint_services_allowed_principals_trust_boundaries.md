# VPC endpoint service allows only trusted principals or none

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vpc_endpoint_services_allowed_principals_trust_boundaries` |
| 云平台 | AWS |
| 服务 | vpc |
| 严重等级 | high |
| 类别 | trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | AwsEc2VpcEndpointService |
| 资源组 | network |

## 描述

**VPC endpoint services** are assessed for their **allowed principals**, comparing each to a configured set of trusted accounts and identifying any **untrusted principals** or a wildcard `*` present in the allowlist.

## 风险

Untrusted or wildcard principals can create PrivateLink connections to your service, eroding segmentation. This enables unauthorized data access (**confidentiality**), abuse of internal APIs (**integrity**), and excess load on backends (**availability**).

## 推荐措施

Apply **least privilege**: restrict **allowed principals** to vetted account IDs and avoid `*`. Maintain a central trust registry, enforce **separation of duties** with approval workflows, and review entries regularly. Use **defense in depth** with strong service authentication and continuous configuration monitoring.

## 修复步骤


### Native IaC

```yaml
# Allow only a trusted principal (or attach none to allow no principals)
Resources:
  <example_resource_name>:
    Type: AWS::EC2::VPCEndpointServicePermissions
    Properties:
      ServiceId: <example_resource_id>
      AllowedPrincipals:
        - arn:aws:iam::<TRUSTED_ACCOUNT_ID>:root  # CRITICAL: restricts access to only this trusted account
```

### Terraform

```hcl
# Allow only a trusted principal (delete this resource to allow none)
resource "aws_vpc_endpoint_service_allowed_principal" "<example_resource_name>" {
  service_id    = "<example_resource_id>"
  principal_arn = "arn:aws:iam::<TRUSTED_ACCOUNT_ID>:root"  # CRITICAL: only this trusted account can create endpoints
}
```

### Other

1. Open the AWS VPC console and go to Endpoint services
2. Select the endpoint service (<example_resource_id>)
3. Open the Allowed principals tab and click Edit allowed principals
4. Remove all entries that are not trusted, including any wildcard (*)
5. Optionally leave the list empty (no principals) or keep only trusted account IDs/ARNs
6. Save changes

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)

## 技术信息

- Source Metadata：[sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/metadata.json](../../sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/metadata.json)
- Source Code：[sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/check.py](../../sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/check.py)
- Source Metadata Path：`sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/metadata.json`
- Source Code Path：`sources/aws/vpc_endpoint_services_allowed_principals_trust_boundaries/check.py`

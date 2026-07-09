# Route53 A record does not point to a dangling IP address

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `route53_dangling_ip_subdomain_takeover` |
| 云平台 | AWS |
| 服务 | route53 |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | AwsRoute53HostedZone |
| 资源组 | network |

## 描述

**Route 53 `A` records** (non-alias) that use literal IPs are evaluated for **public AWS addresses** not currently assigned to resources in the account. Entries that match AWS ranges yet lack ownership are identified as potential **dangling IP targets**.

## 风险

**Dangling DNS `A` records** pointing to released AWS IPs enable **subdomain takeover**. An attacker who later obtains that IP can: - Redirect or alter content (integrity) - Capture credentials/cookies (confidentiality) - Disrupt or impersonate services (availability)

## 推荐措施

Remove or update any record that points to an unassigned IP. Avoid hard-coding AWS public IPs in `A` records; use **aliases/CNAMEs** to managed endpoints. Enforce **asset lifecycle** decommissioning, routine DNS-asset reconciliation, and **change control** with monitoring to prevent and detect drift.

## 修复步骤


### CLI

```text
aws route53 change-resource-record-sets --hosted-zone-id <example_resource_id> --change-batch '{"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":"<example_resource_name>","Type":"A","AliasTarget":{"HostedZoneId":"<ALIAS_TARGET_HOSTED_ZONE_ID>","DNSName":"<ALIAS_TARGET_DNS_NAME>","EvaluateTargetHealth":false}}}]}'
```

### Native IaC

```yaml
# CloudFormation: convert A record to an Alias so it no longer points to a dangling IP
Resources:
  <example_resource_name>:
    Type: AWS::Route53::RecordSet
    Properties:
      HostedZoneId: <example_resource_id>
      Name: <example_resource_name>
      Type: A
      AliasTarget:
        HostedZoneId: <ALIAS_TARGET_HOSTED_ZONE_ID>  # CRITICAL: use Alias to an AWS resource instead of an IP
        DNSName: <ALIAS_TARGET_DNS_NAME>             # CRITICAL: target AWS resource DNS (e.g., ALB/CloudFront)
        EvaluateTargetHealth: false
```

### Terraform

```hcl
# Terraform: convert A record to Alias to avoid dangling public IPs
resource "aws_route53_record" "<example_resource_name>" {
  zone_id = "<example_resource_id>"
  name    = "<example_resource_name>"
  type    = "A"

  alias {                                  # CRITICAL: Alias to AWS resource (no direct IP)
    name                   = "<ALIAS_TARGET_DNS_NAME>"   # e.g., dualstack.<alb>.amazonaws.com
    zone_id                = "<ALIAS_TARGET_HOSTED_ZONE_ID>"
    evaluate_target_health = false
  }
}
```

### Other

1. Open AWS Console > Route 53 > Hosted zones
2. Select the hosted zone and locate the failing non-alias A record
3. If not needed: click Delete and confirm
4. If needed: select the record, click Edit, enable Alias, choose the correct AWS resource (e.g., ALB/CloudFront), then Save changes
5. Wait for propagation (~60s) and re-run the check

## 参考资料

- [https://support.icompaas.com/support/solutions/articles/62000233461-ensure-route53-records-contains-dangling-ips-](https://support.icompaas.com/support/solutions/articles/62000233461-ensure-route53-records-contains-dangling-ips-)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/dangling-dns-records.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Route53/dangling-dns-records.html)
- [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-deleting.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-deleting.html)

## 技术信息

- Source Metadata：[sources/aws/route53_dangling_ip_subdomain_takeover/metadata.json](../../sources/aws/route53_dangling_ip_subdomain_takeover/metadata.json)
- Source Code：[sources/aws/route53_dangling_ip_subdomain_takeover/check.py](../../sources/aws/route53_dangling_ip_subdomain_takeover/check.py)
- Source Metadata Path：`sources/aws/route53_dangling_ip_subdomain_takeover/metadata.json`
- Source Code Path：`sources/aws/route53_dangling_ip_subdomain_takeover/check.py`

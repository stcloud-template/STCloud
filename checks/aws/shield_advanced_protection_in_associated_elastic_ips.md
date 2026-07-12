# Elastic IP address is protected by AWS Shield Advanced

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `shield_advanced_protection_in_associated_elastic_ips` |
| クラウドプラットフォーム | AWS |
| サービス | shield |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsEc2Eip |
| リソースグループ | network |

## 説明

**Elastic IP addresses** are assessed for **AWS Shield Advanced** coverage by verifying they are listed as protected resources.

## リスク

Without **Shield Advanced**, internet-facing EIPs are more susceptible to **DDoS**, threatening **availability** and driving **cost** spikes. Volumetric or protocol floods can saturate bandwidth or exhaust connection state, disrupting services behind the EIP and slowing incident response.

## 推奨事項

Register critical EIPs as **Shield Advanced protected resources**. Apply **defense in depth**: minimize public exposure, use application-layer controls (WAF, rate limiting), monitor telemetry, and review protections regularly, aligning network access with **least privilege**.

## 修正手順


### CLI

```text
aws shield create-protection --name <example_resource_name> --resource-arn arn:aws:ec2:<REGION>:<ACCOUNT_ID>:elastic-ip/eipalloc-<ALLOCATION_ID>
```

### Native IaC

```yaml
# CloudFormation: Add Shield Advanced protection to an Elastic IP
Resources:
  Protection:
    Type: AWS::Shield::Protection
    Properties:
      Name: <example_resource_name>
      ResourceArn: arn:aws:ec2:<REGION>:<ACCOUNT_ID>:elastic-ip/eipalloc-<ALLOCATION_ID>  # Critical: ARN of the Elastic IP to protect
```

### Terraform

```hcl
# Terraform: Add Shield Advanced protection to an Elastic IP
resource "aws_shield_protection" "<example_resource_name>" {
  name         = "<example_resource_name>"
  resource_arn = "arn:aws:ec2:<REGION>:<ACCOUNT_ID>:elastic-ip/eipalloc-<ALLOCATION_ID>" # Critical: ARN of the Elastic IP to protect
}
```

### Other

1. Open the AWS WAF & Shield console
2. Go to AWS Shield > Protected resources
3. Click Add resources to protect
4. Select the Region and resource type: EC2 Elastic IP, then Load resources
5. Select the target Elastic IP
6. Click Protect with Shield Advanced

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html)

## 技術情報

- Source Metadata：[sources/aws/shield_advanced_protection_in_associated_elastic_ips/metadata.json](../../sources/aws/shield_advanced_protection_in_associated_elastic_ips/metadata.json)
- Source Code：[sources/aws/shield_advanced_protection_in_associated_elastic_ips/check.py](../../sources/aws/shield_advanced_protection_in_associated_elastic_ips/check.py)
- Source Metadata Path：`sources/aws/shield_advanced_protection_in_associated_elastic_ips/metadata.json`
- Source Code Path：`sources/aws/shield_advanced_protection_in_associated_elastic_ips/check.py`

# SES identity resource policy does not allow public access

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ses_identity_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | ses |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | AwsIamPolicy |
| 资源组 | messaging |

## 描述

**Amazon SES identities** are evaluated for **publicly accessible resource policies**-for example, statements with `Principal:"*"` or broadly trusted principals that permit actions against the identity.

## 风险

Public SES identity policies allow unauthorized email sending or configuration changes. - Integrity: spoofed emails and brand impersonation - Confidentiality: exposure of identity details - Availability: reputation loss causing throttling or suspension

## 推荐措施

Restrict SES identity policies to known principals and actions following **least privilege**. Prefer explicit account ARNs for sending authorization, and add conditions like `aws:SourceIp` and `aws:SecureTransport`. Review grants regularly and remove unused access as part of **defense in depth**.

## 修复步骤


### CLI

```text
aws sesv2 delete-email-identity-policy --email-identity <IDENTITY-NAME> --policy-name <POLICY-NAME>
```

### Terraform

```hcl
resource "aws_ses_identity_policy" "<example_resource_name>" {
  identity = "<example_resource_name>"
  name     = "<example_resource_name>"

  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = ["<account_id>"] } # Critical: restrict to a specific AWS account, not "*"
      Action    = ["ses:SendEmail"]
      Resource  = "arn:aws:ses:<region>:<account_id>:identity/<example_resource_name>"
    }]
  })
}
```

### Other

1. In the AWS Console, go to Simple Email Service (SES)
2. Open Verified identities and select the affected identity
3. Click Resource policies
4. Delete the public policy, or Edit it to remove any Principal of "*" and restrict to a specific AWS account
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/ses/latest/dg/policy-anatomy.html](https://docs.aws.amazon.com/ses/latest/dg/policy-anatomy.html)
- [https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policies.html](https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policies.html)

## 技术信息

- Source Metadata：[sources/aws/ses_identity_not_publicly_accessible/metadata.json](../../sources/aws/ses_identity_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/ses_identity_not_publicly_accessible/check.py](../../sources/aws/ses_identity_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/ses_identity_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/ses_identity_not_publicly_accessible/check.py`

# Glue Data Catalog is not publicly accessible via its resource policy

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `glue_data_catalogs_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | glue |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | analytics |

## 描述

**AWS Glue Data Catalog** resource policies are assessed for configurations that expose the catalog to anyone, such as `Principal: *`, broad resource scopes, or permissive conditions. The finding highlights catalogs made public through overly permissive resource-based access.

## 风险

Public catalog access lets unauthorized actors enumerate schemas, S3 locations, and connection metadata, weakening **confidentiality**. If writes are exposed, attackers can alter databases/tables, corrupt lineage, and disrupt jobs and queries, harming **integrity** and **availability**, and enabling lateral movement to data stores.

## 推荐措施

Enforce **least privilege** on catalog resource policies: - Avoid `Principal: *` and wildcards - Grant only required actions to explicit principals - Prefer identity-based access or Lake Formation for sharing - Limit scope with precise ARNs/conditions and monitor changes for **defense in depth**

## 修复步骤


### CLI

```text
aws glue delete-resource-policy
```

### Terraform

```hcl
resource "aws_glue_resource_policy" "<example_resource_name>" {
  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Effect    = "Allow",
        Principal = { AWS = "arn:aws:iam::<ACCOUNT_ID>:root" } # Critical: restricts to your account, removing any public (*) access
        Action    = "glue:*",
        Resource  = "arn:aws:glue:<REGION>:<ACCOUNT_ID>:catalog"
      }
    ]
  })
}
```

### Other

1. Sign in to the AWS Console and open the Glue service
2. In the left menu, click Settings
3. Under Data catalog settings > Permissions, click Edit resource policy
4. Remove any statement that has Principal set to * (public) or AWS: "*"; or delete the entire policy
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html?icmpid=docs_console_unmapped#security_iam_service-with-iam-resource-based-policies](https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html?icmpid=docs_console_unmapped#security_iam_service-with-iam-resource-based-policies)
- [https://docs.aws.amazon.com/glue/latest/dg/cross-account-access.html](https://docs.aws.amazon.com/glue/latest/dg/cross-account-access.html)

## 技术信息

- Source Metadata：[sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json](../../sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/glue_data_catalogs_not_publicly_accessible/check.py](../../sources/aws/glue_data_catalogs_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/glue_data_catalogs_not_publicly_accessible/check.py`

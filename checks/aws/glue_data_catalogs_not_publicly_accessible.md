# Glue Data Catalog is not publicly accessible via its resource policy

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_data_catalogs_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue Data Catalog** resource policies are assessed for configurations that expose the catalog to anyone, such as `Principal: *`, broad resource scopes, or permissive conditions. The finding highlights catalogs made public through overly permissive resource-based access.

## リスク

Public catalog access lets unauthorized actors enumerate schemas, S3 locations, and connection metadata, weakening **confidentiality**. If writes are exposed, attackers can alter databases/tables, corrupt lineage, and disrupt jobs and queries, harming **integrity** and **availability**, and enabling lateral movement to data stores.

## 推奨事項

Enforce **least privilege** on catalog resource policies: - Avoid `Principal: *` and wildcards - Grant only required actions to explicit principals - Prefer identity-based access or Lake Formation for sharing - Limit scope with precise ARNs/conditions and monitor changes for **defense in depth**

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html?icmpid=docs_console_unmapped#security_iam_service-with-iam-resource-based-policies](https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html?icmpid=docs_console_unmapped#security_iam_service-with-iam-resource-based-policies)
- [https://docs.aws.amazon.com/glue/latest/dg/cross-account-access.html](https://docs.aws.amazon.com/glue/latest/dg/cross-account-access.html)

## 技術情報

- Source Metadata：[sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json](../../sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/glue_data_catalogs_not_publicly_accessible/check.py](../../sources/aws/glue_data_catalogs_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/glue_data_catalogs_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/glue_data_catalogs_not_publicly_accessible/check.py`

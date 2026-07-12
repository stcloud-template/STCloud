# SSM document is not public and shared only with trusted AWS accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ssm_documents_set_as_public` |
| クラウドプラットフォーム | AWS |
| サービス | ssm |
| 重大度 | high |
| カテゴリ | identity-access, internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsSsmPatchCompliance |
| リソースグループ | devops |

## 説明

**SSM documents** are evaluated for **public sharing** (`all`) and for shares with AWS accounts outside a defined trusted list. Documents that remain private or are shared only with trusted accounts indicate restricted distribution.

## リスク

Public or non-trusted sharing exposes document content, eroding **confidentiality** of scripts, parameters, and embedded secrets. Adversaries can study runbooks to craft targeted attacks and reuse logic, causing credential leakage and downstream **integrity** and **availability** impacts.

## 推奨事項

Apply **least privilege** to document distribution: - Keep documents private; share only with specific trusted account IDs - Enable account-level block public sharing for documents - Remove secrets from content; use secure parameters - Limit who can share or run documents; require reviews and version control

## 修正手順


### CLI

```text
aws ssm modify-document-permission --name <DOCUMENT_NAME> --permission-type Share --account-ids-to-remove all
```

### Terraform

```hcl
resource "aws_ssm_document" "<example_resource_name>" {
  name          = "<example_resource_name>"
  document_type = "Command"
  content       = jsonencode({
    schemaVersion = "2.2"
    mainSteps     = []
  })
  # Critical: no permissions block -> document remains private (not public/shared)
}
```

### Other

1. Open AWS Systems Manager > Documents
2. Select the document > Permissions tab > Edit
3. Select Private (remove Public/'all')
4. Remove any non-trusted AWS account IDs
5. Save

## 参考資料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-before-you-share.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-before-you-share.html)

## 技術情報

- Source Metadata：[sources/aws/ssm_documents_set_as_public/metadata.json](../../sources/aws/ssm_documents_set_as_public/metadata.json)
- Source Code：[sources/aws/ssm_documents_set_as_public/check.py](../../sources/aws/ssm_documents_set_as_public/check.py)
- Source Metadata Path：`sources/aws/ssm_documents_set_as_public/metadata.json`
- Source Code Path：`sources/aws/ssm_documents_set_as_public/check.py`

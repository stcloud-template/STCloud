# SSM document is not public and shared only with trusted AWS accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ssm_documents_set_as_public` |
| 云平台 | AWS |
| 服务 | ssm |
| 严重等级 | high |
| 类别 | identity-access, internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsSsmPatchCompliance |
| 资源组 | devops |

## 描述

**SSM documents** are evaluated for **public sharing** (`all`) and for shares with AWS accounts outside a defined trusted list. Documents that remain private or are shared only with trusted accounts indicate restricted distribution.

## 风险

Public or non-trusted sharing exposes document content, eroding **confidentiality** of scripts, parameters, and embedded secrets. Adversaries can study runbooks to craft targeted attacks and reuse logic, causing credential leakage and downstream **integrity** and **availability** impacts.

## 推荐措施

Apply **least privilege** to document distribution: - Keep documents private; share only with specific trusted account IDs - Enable account-level block public sharing for documents - Remove secrets from content; use secure parameters - Limit who can share or run documents; require reviews and version control

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-before-you-share.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-before-you-share.html)

## 技术信息

- Source Metadata：[sources/aws/ssm_documents_set_as_public/metadata.json](../../sources/aws/ssm_documents_set_as_public/metadata.json)
- Source Code：[sources/aws/ssm_documents_set_as_public/check.py](../../sources/aws/ssm_documents_set_as_public/check.py)
- Source Metadata Path：`sources/aws/ssm_documents_set_as_public/metadata.json`
- Source Code Path：`sources/aws/ssm_documents_set_as_public/check.py`

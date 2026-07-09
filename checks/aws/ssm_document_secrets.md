# SSM document contains no secrets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ssm_document_secrets` |
| 云平台 | AWS |
| 服务 | ssm |
| 严重等级 | high |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Security, Effects/Data Exposure |
| 资源类型 | AwsSsmPatchCompliance |
| 资源组 | devops |

## 描述

**AWS Systems Manager documents** are inspected for embedded **secrets** within their content. Patterns resembling passwords, access keys, tokens, or private keys in document steps are flagged when values appear hardcoded rather than referenced securely.

## 风险

Hardcoded secrets in SSM documents weaken CIA: - Confidentiality: readers of the document can exfiltrate credentials. - Integrity: stolen keys enable privilege escalation and automation tampering. - Availability: abused credentials can disrupt systems and impede recovery.

## 推荐措施

Avoid embedding secrets. Store them in **Secrets Manager** or **Parameter Store** as `SecureString` (KMS-encrypted) and reference at runtime. Apply **least privilege** to documents and secrets, prefer **short-lived role credentials**, rotate credentials, continuously scan/audit documents, and enforce **separation of duties** for authoring and approval.

## 修复步骤


### CLI

```text
aws ssm update-document --name <example_resource_name> --content file://<SANITIZED_DOCUMENT_FILE>.json
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::SSM::Document
    Properties:
      DocumentType: Command
      Content:
        schemaVersion: '2.2'
        mainSteps:
          - action: aws:runShellScript
            inputs:
              runCommand:
                # Critical: reference a SecureString parameter instead of hardcoding a secret
                # This avoids embedding secrets in the document content
                - "export PASSWORD='{{ssm-secure:/path/to/secret}}'"
```

### Terraform

```hcl
resource "aws_ssm_document" "<example_resource_name>" {
  name          = "<example_resource_name>"
  document_type = "Command"

  content = jsonencode({
    schemaVersion = "2.2"
    mainSteps = [{
      action = "aws:runShellScript"
      name   = "run"
      inputs = {
        runCommand = [
          // Critical: use ssm-secure dynamic reference to avoid hardcoded secrets
          "export PASSWORD='{{ssm-secure:/path/to/secret}}'"
        ]
      }
    }]
  })
}
```

### Other

1. In the AWS Console, go to Systems Manager > Parameter Store > Create parameter
2. Set Name to /path/to/secret, Type to SecureString, enter the secret value, and click Create parameter
3. Go to Systems Manager > Documents, select the document, then Actions > Edit content
4. Remove any hardcoded secrets and reference the SecureString parameter, e.g.: {{ssm-secure:/path/to/secret}}
5. Save to create a new version and set it as Default
6. Re-run the check to confirm it passes

## 参考资料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html)

## 技术信息

- Source Metadata：[sources/aws/ssm_document_secrets/metadata.json](../../sources/aws/ssm_document_secrets/metadata.json)
- Source Code：[sources/aws/ssm_document_secrets/check.py](../../sources/aws/ssm_document_secrets/check.py)
- Source Metadata Path：`sources/aws/ssm_document_secrets/metadata.json`
- Source Code Path：`sources/aws/ssm_document_secrets/check.py`

# SSM document contains no secrets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ssm_document_secrets` |
| クラウドプラットフォーム | AWS |
| サービス | ssm |
| 重大度 | high |
| カテゴリ | secrets |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Security, Effects/Data Exposure |
| リソースタイプ | AwsSsmPatchCompliance |
| リソースグループ | devops |

## 説明

**AWS Systems Manager documents** are inspected for embedded **secrets** within their content. Patterns resembling passwords, access keys, tokens, or private keys in document steps are flagged when values appear hardcoded rather than referenced securely.

## リスク

Hardcoded secrets in SSM documents weaken CIA: - Confidentiality: readers of the document can exfiltrate credentials. - Integrity: stolen keys enable privilege escalation and automation tampering. - Availability: abused credentials can disrupt systems and impede recovery.

## 推奨事項

Avoid embedding secrets. Store them in **Secrets Manager** or **Parameter Store** as `SecureString` (KMS-encrypted) and reference at runtime. Apply **least privilege** to documents and secrets, prefer **short-lived role credentials**, rotate credentials, continuously scan/audit documents, and enforce **separation of duties** for authoring and approval.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-secretsmanager-secret-generatesecretstring.html)

## 技術情報

- Source Metadata：[sources/aws/ssm_document_secrets/metadata.json](../../sources/aws/ssm_document_secrets/metadata.json)
- Source Code：[sources/aws/ssm_document_secrets/check.py](../../sources/aws/ssm_document_secrets/check.py)
- Source Metadata Path：`sources/aws/ssm_document_secrets/metadata.json`
- Source Code Path：`sources/aws/ssm_document_secrets/check.py`

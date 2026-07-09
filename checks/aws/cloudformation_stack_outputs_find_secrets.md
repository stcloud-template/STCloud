# CloudFormation stack outputs do not contain secrets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudformation_stack_outputs_find_secrets` |
| 云平台 | AWS |
| 服务 | cloudformation |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Sensitive Data Identifications/Security, Effects/Data Exposure |
| 资源类型 | AwsCloudFormationStack |
| 资源组 | devops |

## 描述

**CloudFormation stack Outputs** are analyzed for hardcoded secrets-passwords, API keys, tokens-using pattern-based detection across output values. A finding indicates potential secret strings present within `Outputs` of the template or stack.

## 风险

**Secrets in Outputs** are readable to anyone with stack metadata access, enabling credential theft, unauthorized API calls, and lateral movement. Exposure via consoles, exports, or CI logs undermines confidentiality and can lead to privilege escalation and data exfiltration.

## 推荐措施

Remove secrets from `Outputs`. Store credentials in **Secrets Manager** or **Parameter Store** and reference them via dynamic references; set `NoEcho` for sensitive parameters. Apply **least privilege** to view stack metadata, avoid exporting sensitive values, and add automated IaC secret scanning for **defense in depth**.

## 修复步骤


### CLI

```text
aws cloudformation update-stack --stack-name <STACK_NAME> --template-body file://<TEMPLATE_WITHOUT_SENSITIVE_OUTPUTS>.yaml
```

### Native IaC

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Outputs:
  # Critical: remove outputs that expose secrets (passwords/tokens/keys)
  # Keeping only non-sensitive values in Outputs remediates the finding
  SafeInfo:
    Value: "non-sensitive"
```

### Terraform

```hcl
# Critical: the embedded CloudFormation template removes secret outputs
resource "aws_cloudformation_stack" "<example_resource_name>" {
  name          = "<example_resource_name>"
  template_body = <<-YAML
    AWSTemplateFormatVersion: '2010-09-09'
    # Critical: delete Outputs that expose secrets; keep only non-sensitive values
    Outputs:
      SafeInfo:
        Value: "non-sensitive"  # Avoids exposing secrets in stack outputs
  YAML
}
```

### Other

1. In the AWS Console, go to CloudFormation > Stacks and select the stack
2. Click Update > Replace current template
3. Upload or paste the template with any secret-bearing Outputs removed (do not output passwords/tokens/keys)
4. Click Next through the wizard and choose Submit to apply the change set
5. Verify the stack Outputs tab no longer shows sensitive values

## 参考资料

- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
- [https://support.icompaas.com/support/solutions/articles/62000127093-ensure-no-secrets-are-found-in-cloudformation-outputs](https://support.icompaas.com/support/solutions/articles/62000127093-ensure-no-secrets-are-found-in-cloudformation-outputs)
- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html)

## 技术信息

- Source Metadata：[sources/aws/cloudformation_stack_outputs_find_secrets/metadata.json](../../sources/aws/cloudformation_stack_outputs_find_secrets/metadata.json)
- Source Code：[sources/aws/cloudformation_stack_outputs_find_secrets/check.py](../../sources/aws/cloudformation_stack_outputs_find_secrets/check.py)
- Source Metadata Path：`sources/aws/cloudformation_stack_outputs_find_secrets/metadata.json`
- Source Code Path：`sources/aws/cloudformation_stack_outputs_find_secrets/check.py`

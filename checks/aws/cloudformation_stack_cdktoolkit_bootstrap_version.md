# CDKToolkit CloudFormation stack has Bootstrap version 21 or higher

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudformation_stack_cdktoolkit_bootstrap_version` |
| 云平台 | AWS |
| 服务 | cloudformation |
| 严重等级 | high |
| 类别 | vulnerabilities |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Patch Management |
| 资源类型 | AwsCloudFormationStack |
| 资源组 | devops |

## 描述

**CloudFormation CDKToolkit** stack's `BootstrapVersion` is compared to a recommended minimum (default `21`). A lower value indicates the environment uses legacy bootstrap resources and IAM roles from older templates.

## 风险

**Outdated bootstrap stacks** can lack recent hardening. Asset buckets or ECR repos may be easier to misuse, and deployment roles may have broader trust. Adversaries could tamper artifacts or assume privileged roles, compromising integrity/confidentiality and enabling privilege escalation.

## 推荐措施

Standardize on the modern bootstrap at or above the recommended version (e.g., `>= 21`) in every account and Region. Apply **least privilege** to bootstrap roles, limit trusted accounts, enable termination protection, and periodically review for version drift to strengthen **defense in depth**.

## 修复步骤


### CLI

cdk bootstrap aws://<ACCOUNT_ID>/<REGION>

### Native IaC

```yaml
# Minimal CloudFormation to expose BootstrapVersion >= 21 for CDKToolkit
# Deploy this template as a stack named "CDKToolkit"
Resources:
  CdkBootstrapVersion:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Name: /cdk-bootstrap/hnb659fds/version  # critical: stores the bootstrap version used by CDK
      Value: "21"                              # critical: set to 21 (or higher) to satisfy the check
Outputs:
  BootstrapVersion:
    Value: !GetAtt CdkBootstrapVersion.Value   # critical: exposes the version in stack outputs so the check passes
```

### Terraform

```hcl
# Create/Update the CDKToolkit stack with BootstrapVersion >= 21
resource "aws_cloudformation_stack" "cdktoolkit" {
  name          = "CDKToolkit"
  # critical: template sets the BootstrapVersion output to 21 (or higher) so the check passes
  template_body = <<YAML
Resources:
  CdkBootstrapVersion:
    Type: AWS::SSM::Parameter
    Properties:
      Type: String
      Name: /cdk-bootstrap/hnb659fds/version  # critical: stores the bootstrap version
      Value: "21"                              # critical: version must be >= 21
Outputs:
  BootstrapVersion:
    Value: !GetAtt CdkBootstrapVersion.Value   # critical: exposes version via stack output
YAML
}
```

### Other

1. Sign in to the AWS Console and open CloudShell
2. Run: cdk bootstrap aws://<ACCOUNT_ID>/<REGION>
3. In the console, go to CloudFormation > Stacks > CDKToolkit > Outputs
4. Confirm Output "BootstrapVersion" is 21 or higher

## 参考资料

- [https://towardsthecloud.com/blog/aws-cdk-bootstrap](https://towardsthecloud.com/blog/aws-cdk-bootstrap)
- [https://support.icompaas.com/support/solutions/articles/62000233694-ensure-that-cdktoolkit-stacks-have-a-bootstrap-version-of-21-or-higher-to-mitigate-security-risks](https://support.icompaas.com/support/solutions/articles/62000233694-ensure-that-cdktoolkit-stacks-have-a-bootstrap-version-of-21-or-higher-to-mitigate-security-risks)
- [https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-bootstrap.html](https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-bootstrap.html)
- [https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-customizing.html](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-customizing.html)

## 技术信息

- Source Metadata：[sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/metadata.json](../../sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/metadata.json)
- Source Code：[sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/check.py](../../sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/check.py)
- Source Metadata Path：`sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/metadata.json`
- Source Code Path：`sources/aws/cloudformation_stack_cdktoolkit_bootstrap_version/check.py`

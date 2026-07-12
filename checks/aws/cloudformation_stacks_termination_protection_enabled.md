# CloudFormation stack has termination protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudformation_stacks_termination_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudformation |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Destruction |
| リソースタイプ | AwsCloudFormationStack |
| リソースグループ | devops |

## 説明

**AWS CloudFormation root stacks** are evaluated for **termination protection**. The detection identifies whether `termination protection` is enabled to block stack deletions on non-nested stacks.

## リスク

Without **termination protection**, human error or automation can delete entire stacks, causing immediate **availability** loss and potential **data destruction** of managed resources. Attackers with delete rights can more easily trigger outages and hinder recovery.

## 推奨事項

Enable **termination protection** on root stacks for critical workloads. Enforce **least privilege** on who can alter this setting or delete stacks, require **change review** via change sets, and apply **stack policies** plus `DeletionPolicy: Retain` for data stores for defense in depth.

## 修正手順


### CLI

```text
aws cloudformation update-termination-protection --stack-name <STACK_NAME> --enable-termination-protection
```

### Terraform

```hcl
resource "aws_cloudformation_stack" "<example_resource_name>" {
  name                           = "<example_resource_name>"
  template_url                   = "https://s3.amazonaws.com/<bucket>/<template>.json"
  enable_termination_protection  = true # Critical: enables termination protection to prevent stack deletion
}
```

### Other

1. Open the AWS CloudFormation console
2. Select the target stack
3. Choose Stack actions > Edit termination protection
4. Select Enable and Save

## 参考資料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFormation/stack-termination-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudFormation/stack-termination-protection.html)

## 技術情報

- Source Metadata：[sources/aws/cloudformation_stacks_termination_protection_enabled/metadata.json](../../sources/aws/cloudformation_stacks_termination_protection_enabled/metadata.json)
- Source Code：[sources/aws/cloudformation_stacks_termination_protection_enabled/check.py](../../sources/aws/cloudformation_stacks_termination_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudformation_stacks_termination_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudformation_stacks_termination_protection_enabled/check.py`

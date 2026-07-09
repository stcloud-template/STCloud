# Ensure IAM Service Roles prevents against a cross-service confused deputy attack

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_cross_service_confused_deputy_prevention` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | trust-boundaries |
| 资源类型 | AwsIamRole |
| 资源组 | IAM |

## 描述

Ensure IAM Service Roles prevents against a cross-service confused deputy attack

## 风险

Allow attackers to gain unauthorized access to resources

## 推荐措施

To mitigate cross-service confused deputy attacks, it's recommended to use the aws:SourceArn and aws:SourceAccount global condition context keys in your IAM role trust policies. If the role doesn't support these fields, consider implementing alternative security measures, such as defining more restrictive resource-based policies or using service-specific trust policies, to limit the role's permissions and exposure. For detailed guidance, refer to AWS's documentation on preventing cross-service confused deputy issues.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html#cross-service-confused-deputy-prevention)

## 技术信息

- Source Metadata：[sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json](../../sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json)
- Source Code：[sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py](../../sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py)
- Source Metadata Path：`sources/aws/iam_role_cross_service_confused_deputy_prevention/metadata.json`
- Source Code Path：`sources/aws/iam_role_cross_service_confused_deputy_prevention/check.py`

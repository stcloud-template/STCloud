# Ensure IAM inline policies that allow full "cloudtrail:*" privileges are not created

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_inline_policy_no_full_access_to_cloudtrail` |
| 云平台 | AWS |
| 服务 | iam |
| 子服务 | inline_policies |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

Ensure IAM inline policies that allow full "cloudtrail:*" privileges are not created

## 风险

CloudTrail is a critical service and IAM policies should follow least privilege model for this service in particular

## 推荐措施

It is more secure to start with a minimum set of permissions and grant additional permissions as necessary, rather than starting with permissions that are too lenient and then trying to tighten them later. List policies an analyze if permissions are the least possible to conduct business activities.

- 推荐链接：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/metadata.json](../../sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/metadata.json)
- Source Code：[sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/check.py](../../sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/check.py)
- Source Metadata Path：`sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/metadata.json`
- Source Code Path：`sources/aws/iam_inline_policy_no_full_access_to_cloudtrail/check.py`

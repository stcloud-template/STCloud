# Ensure IAM AWS-Managed policies that allow full "*:*" administrative privileges are not attached

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_aws_attached_policy_no_administrative_privileges` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamPolicy |
| 资源组 | IAM |

## 描述

Ensure IAM AWS-Managed policies that allow full "*:*" administrative privileges are not attached

## 风险

IAM policies are the means by which privileges are granted to users, groups, or roles. It is recommended and considered a standard security advice to grant least privilege—that is, granting only the permissions required to perform a task. Determine what users need to do and then craft policies for them that let the users perform only those tasks instead of allowing full administrative privileges. Providing full administrative privileges instead of restricting to the minimum set of permissions that the user is required to do exposes the resources to potentially unwanted actions.

## 推荐措施

It is more secure to start with a minimum set of permissions and grant additional permissions as necessary, rather than starting with permissions that are too lenient and then trying to tighten them later. List policies an analyze if permissions are the least possible to conduct business activities.

- 推荐链接：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47#terraform](https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47](https://docs.ST Cloud.com/checks/aws/iam-policies/iam_47)

## 参考资料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/iam_aws_attached_policy_no_administrative_privileges/metadata.json](../../sources/aws/iam_aws_attached_policy_no_administrative_privileges/metadata.json)
- Source Code：[sources/aws/iam_aws_attached_policy_no_administrative_privileges/check.py](../../sources/aws/iam_aws_attached_policy_no_administrative_privileges/check.py)
- Source Metadata Path：`sources/aws/iam_aws_attached_policy_no_administrative_privileges/metadata.json`
- Source Code Path：`sources/aws/iam_aws_attached_policy_no_administrative_privileges/check.py`

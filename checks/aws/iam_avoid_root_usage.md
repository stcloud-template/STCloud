# Avoid the use of the root accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_avoid_root_usage` |
| 云平台 | AWS |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsIamUser |
| 资源组 | IAM |

## 描述

Avoid the use of the root account

## 风险

The root account has unrestricted access to all resources in the AWS account. It is highly recommended that the use of this account be avoided.

## 推荐措施

Follow the remediation instructions of the Ensure IAM policies are attached only to groups or roles recommendation.

- 推荐链接：[http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/iam_avoid_root_usage/metadata.json](../../sources/aws/iam_avoid_root_usage/metadata.json)
- Source Code：[sources/aws/iam_avoid_root_usage/check.py](../../sources/aws/iam_avoid_root_usage/check.py)
- Source Metadata Path：`sources/aws/iam_avoid_root_usage/metadata.json`
- Source Code Path：`sources/aws/iam_avoid_root_usage/check.py`

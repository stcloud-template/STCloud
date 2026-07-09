# Ensure that CodePipeline projects do not use public GitHub or GitLab repositories as source.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codepipeline_project_repo_private` |
| 云平台 | AWS |
| 服务 | codepipeline |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Other |
| 资源组 | devops |

## 描述

Ensure that CodePipeline projects do not use public GitHub or GitLab repositories as source.

## 风险

Using public Git repositories in CodePipeline projects could expose sensitive deployment configurations and increase the risk of supply chain attacks.

## 推荐措施

Use private Git repositories for CodePipeline sources and ensure proper authentication is configured using AWS CodeStar Connections. Consider using AWS CodeCommit or other private repository solutions for sensitive code.

- 推荐链接：[https://docs.aws.amazon.com/codepipeline/latest/userguide/connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections)

## 修复步骤


### CLI

```text
aws codestar-connections create-connection --provider-type GitHub|GitLab --connection-name <connection-name>
```

## 参考资料

- [https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html)
- [https://docs.aws.amazon.com/codepipeline/latest/userguide/connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections)

## 技术信息

- Source Metadata：[sources/aws/codepipeline_project_repo_private/metadata.json](../../sources/aws/codepipeline_project_repo_private/metadata.json)
- Source Code：[sources/aws/codepipeline_project_repo_private/check.py](../../sources/aws/codepipeline_project_repo_private/check.py)
- Source Metadata Path：`sources/aws/codepipeline_project_repo_private/metadata.json`
- Source Code Path：`sources/aws/codepipeline_project_repo_private/check.py`

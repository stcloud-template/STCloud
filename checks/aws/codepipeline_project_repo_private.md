# Ensure that CodePipeline projects do not use public GitHub or GitLab repositories as source.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `codepipeline_project_repo_private` |
| クラウドプラットフォーム | AWS |
| サービス | codepipeline |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Other |
| リソースグループ | devops |

## 説明

Ensure that CodePipeline projects do not use public GitHub or GitLab repositories as source.

## リスク

Using public Git repositories in CodePipeline projects could expose sensitive deployment configurations and increase the risk of supply chain attacks.

## 推奨事項

Use private Git repositories for CodePipeline sources and ensure proper authentication is configured using AWS CodeStar Connections. Consider using AWS CodeCommit or other private repository solutions for sensitive code.

- 推奨リンク：[https://docs.aws.amazon.com/codepipeline/latest/userguide/connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections)

## 修正手順


### CLI

```text
aws codestar-connections create-connection --provider-type GitHub|GitLab --connection-name <connection-name>
```

## 参考資料

- [https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html)
- [https://docs.aws.amazon.com/codepipeline/latest/userguide/connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections)

## 技術情報

- Source Metadata：[sources/aws/codepipeline_project_repo_private/metadata.json](../../sources/aws/codepipeline_project_repo_private/metadata.json)
- Source Code：[sources/aws/codepipeline_project_repo_private/check.py](../../sources/aws/codepipeline_project_repo_private/check.py)
- Source Metadata Path：`sources/aws/codepipeline_project_repo_private/metadata.json`
- Source Code Path：`sources/aws/codepipeline_project_repo_private/check.py`

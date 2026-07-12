# CodeBuild project does not use a user-controlled buildspec file

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `codebuild_project_user_controlled_buildspec` |
| クラウドプラットフォーム | AWS |
| サービス | codebuild |
| 重大度 | medium |
| カテゴリ | software-supply-chain, ci-cd |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsCodeBuildProject |
| リソースグループ | devops |

## 説明

AWS CodeBuild projects are evaluated for use of a **user-controlled buildspec**, identified when the project references a repository file like `*.yml` or `*.yaml`. Projects using non file-based build instructions are treated as centrally managed.

## リスク

Repository-controlled buildspecs let unreviewed changes run in CI, endangering **integrity** (tampered artifacts), **confidentiality** (secret leakage), and **availability** (resource abuse). Attackers can weaponize PRs to execute code and pivot via the build role.

## 推奨事項

Adopt a **centrally managed buildspec** that contributors cannot modify. - Enforce protected branches and required reviews for build instructions - Apply **least privilege** to the build role and minimize secrets - Separate duties for pipeline admins vs code authors Use vetted, versioned templates for defense in depth.

## 修正手順


### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::Project
    Properties:
      ServiceRole: <example_role_arn>
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: <IMAGE>
      Source:
        Type: CODEPIPELINE
        BuildSpec: |  # Critical: Inline buildspec avoids using a user-controlled file path
          version: 0.2
```

### Terraform

```hcl
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_role_arn>"

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "<IMAGE>"
    type         = "LINUX_CONTAINER"
  }

  source {
    type      = "CODEPIPELINE"
    buildspec = <<EOT
version: 0.2
EOT
    # Critical: Inline buildspec avoids using a user-controlled buildspec file
  }
}
```

### Other

1. In the AWS Console, go to CodeBuild > Projects and open the target project
2. Click Edit
3. In Source, under Buildspec, select Insert build commands (not Use a buildspec file)
4. Paste minimal inline YAML:
   ```
   version: 0.2
   ```
5. Save

## 参考資料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/security.html](https://docs.aws.amazon.com/codebuild/latest/userguide/security.html)
- [https://support.icompaas.com/support/solutions/articles/62000229579-ensure-codebuild-project-with-an-user-controlled-buildspec](https://support.icompaas.com/support/solutions/articles/62000229579-ensure-codebuild-project-with-an-user-controlled-buildspec)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html)

## 技術情報

- Source Metadata：[sources/aws/codebuild_project_user_controlled_buildspec/metadata.json](../../sources/aws/codebuild_project_user_controlled_buildspec/metadata.json)
- Source Code：[sources/aws/codebuild_project_user_controlled_buildspec/check.py](../../sources/aws/codebuild_project_user_controlled_buildspec/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_user_controlled_buildspec/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_user_controlled_buildspec/check.py`

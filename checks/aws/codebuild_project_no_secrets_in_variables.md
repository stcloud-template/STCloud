# CodeBuild project has no sensitive credentials in plaintext environment variables

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `codebuild_project_no_secrets_in_variables` |
| クラウドプラットフォーム | AWS |
| サービス | codebuild |
| 重大度 | critical |
| カテゴリ | secrets, ci-cd |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Credential Access, Effects/Data Exposure, Sensitive Data Identifications/Security |
| リソースタイプ | AwsCodeBuildProject |
| リソースグループ | devops |

## 説明

**AWS CodeBuild projects** are inspected for **plaintext environment variables** (`PLAINTEXT`) that resemble **secrets** (keys, tokens, passwords). Such values indicate sensitive data is stored directly in environment variables instead of being sourced securely.

## リスク

Plaintext secrets in environment variables reduce confidentiality: values can be viewed in consoles/CLI and may leak into build logs or public outputs. Compromised credentials enable unauthorized AWS actions, artifact tampering, and lateral movement, causing data exfiltration and CI/CD supply-chain compromise.

## 推奨事項

Store secrets outside the build and reference them via **AWS Secrets Manager** or **AWS Systems Manager Parameter Store** instead of `PLAINTEXT` variables. - Enforce **least privilege** on the build role - Rotate secrets; prefer short-lived credentials - Avoid logging or exporting secret values and never embed them in artifacts

## 修正手順


### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::Project
    Properties:
      Name: <example_resource_name>
      ServiceRole: <example_resource_arn>
      Source:
        Type: NO_SOURCE
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/standard:5.0
        EnvironmentVariables:
          - Name: <SENSITIVE_VAR_NAME>
            Type: SECRETS_MANAGER  # CRITICAL: store secret in Secrets Manager to avoid PLAINTEXT
            Value: <example_secret_name>  # Secret name or ARN (optionally include json-key)
```

### Terraform

```hcl
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_resource_arn>"

  source {
    type = "NO_SOURCE"
  }

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/standard:5.0"
    type         = "LINUX_CONTAINER"

    environment_variable {
      name  = "<SENSITIVE_VAR_NAME>"
      type  = "SECRETS_MANAGER"  # CRITICAL: use Secrets Manager so value isn't plaintext
      value = "<example_secret_name>"
    }
  }
}
```

### Other

1. In AWS Console, go to CodeBuild > Build projects and open your project
2. Click Edit in the Environment section
3. Under Environment variables, for each sensitive variable with Type = Plaintext, change Type to Secrets Manager (or Parameter store)
4. Select the secret (or parameter) that holds the value, then Save
5. If the secret/parameter does not exist, create it in Secrets Manager or Systems Manager Parameter Store first, then repeat steps 3-4

## 参考資料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)
- [https://www.learnaws.org/2022/11/18/aws-codebuild-secrets-manager/](https://www.learnaws.org/2022/11/18/aws-codebuild-secrets-manager/)
- [https://www.learnaws.org/2023/08/23/codebuild-env-vars/](https://www.learnaws.org/2023/08/23/codebuild-env-vars/)
- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-2](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-2)
- [https://pasmichal.medium.com/how-to-handle-secrets-in-aws-codebuild-6e1b96013712](https://pasmichal.medium.com/how-to-handle-secrets-in-aws-codebuild-6e1b96013712)
- [https://medium.com/@odofing/aws-codepipeline-how-to-securely-store-environment-variables-in-ssm-paramater-store-and-aws-9a96d7083b3c](https://medium.com/@odofing/aws-codepipeline-how-to-securely-store-environment-variables-in-ssm-paramater-store-and-aws-9a96d7083b3c)

## 技術情報

- Source Metadata：[sources/aws/codebuild_project_no_secrets_in_variables/metadata.json](../../sources/aws/codebuild_project_no_secrets_in_variables/metadata.json)
- Source Code：[sources/aws/codebuild_project_no_secrets_in_variables/check.py](../../sources/aws/codebuild_project_no_secrets_in_variables/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_no_secrets_in_variables/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_no_secrets_in_variables/check.py`

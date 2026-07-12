# Internal CodeArtifact package does not allow publishing versions already present in external public sources

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `codeartifact_packages_external_public_publishing_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | codeartifact |
| 重大度 | critical |
| カテゴリ | software-supply-chain |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, TTPs/Initial Access |
| リソースタイプ | Other |
| リソースグループ | devops |

## 説明

**AWS CodeArtifact packages** with an **internal or unknown origin** are evaluated for their **package origin controls**. The check identifies packages where the `upstream` setting allows ingesting versions from external or upstream repositories.

## リスク

Allowing upstream on internal packages enables **dependency confusion**: public repos can supply higher versions to builds, leading to malicious code execution and package tampering. This threatens **integrity**, exposes secrets and data (**confidentiality**), and may disrupt pipelines and services (**availability**).

## 推奨事項

Enforce **Package Origin Controls** so internal packages use `upstream=BLOCK` and only trusted publish paths. Apply **least privilege** with package groups and private namespaces, pin versions, and prefer private endpoints. Add artifact signing and CI isolation, and monitor package events for unexpected source changes.

## 修正手順


### CLI

```text
aws codeartifact put-package-origin-configuration --domain <DOMAIN> --repository <REPOSITORY> --format <FORMAT> --package <PACKAGE_NAME> --restrictions publish=ALLOW,upstream=BLOCK
```

### Other

1. In the AWS Console, go to CodeArtifact > Repositories and select <REPOSITORY>
2. In Packages, open the internal package <PACKAGE_NAME>
3. Under Origin controls, choose Edit
4. Set Upstream to Block (leave Publish as Allow if required)
5. Save

## 参考資料

- [https://noise.getoto.net/2022/07/15/tighten-your-package-security-with-codeartifact-package-origin-control-toolkit/](https://noise.getoto.net/2022/07/15/tighten-your-package-security-with-codeartifact-package-origin-control-toolkit/)
- [https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html](https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html)
- [https://newstar.cloud/blog/improve-the-security-of-your-software-supply-chain-with-amazon-codeartifact-package-group-configuration/](https://newstar.cloud/blog/improve-the-security-of-your-software-supply-chain-with-amazon-codeartifact-package-group-configuration/)
- [https://zego.engineering/dependency-confusion-in-aws-codeartifact-86b9ff68963d](https://zego.engineering/dependency-confusion-in-aws-codeartifact-86b9ff68963d)

## 技術情報

- Source Metadata：[sources/aws/codeartifact_packages_external_public_publishing_disabled/metadata.json](../../sources/aws/codeartifact_packages_external_public_publishing_disabled/metadata.json)
- Source Code：[sources/aws/codeartifact_packages_external_public_publishing_disabled/check.py](../../sources/aws/codeartifact_packages_external_public_publishing_disabled/check.py)
- Source Metadata Path：`sources/aws/codeartifact_packages_external_public_publishing_disabled/metadata.json`
- Source Code Path：`sources/aws/codeartifact_packages_external_public_publishing_disabled/check.py`

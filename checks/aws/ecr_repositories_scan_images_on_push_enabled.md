# [DEPRECATED] ECR repository has image scanning on push enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecr_repositories_scan_images_on_push_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ecr |
| 重大度 | medium |
| カテゴリ | container-security |
| チェックタイプ | Software and Configuration Checks/Vulnerabilities/CVE, Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEcrRepository |
| リソースグループ | container |

## 説明

[DEPRECATED] **Amazon ECR repositories** are evaluated for **image scanning on push**; when configured, new image uploads automatically trigger a vulnerability scan (`scan_on_push`).

## リスク

Without **scan on push**, images with known CVEs can enter registries and reach runtime unnoticed, undermining **integrity** and **confidentiality** through exploitable packages. Attackers may achieve code execution and lateral movement. Delayed detection increases operational risk and extends remediation timelines.

## 推奨事項

Enable **image scanning on push** (`scan_on_push`) for all repositories and use findings as promotion gates. Prefer **continuous/enhanced scanning** for defense in depth, set severity thresholds, and block or quarantine noncompliant images. Integrate results with CI/CD and adopt **shift-left** vulnerability management.

## 修正手順


### CLI

```text
aws ecr put-image-scanning-configuration --repository-name <repo_name> --image-scanning-configuration scanOnPush=true
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ECR::Repository
    Properties:
      ImageScanningConfiguration:
        ScanOnPush: true  # Critical: enables image scanning on push for this repository
```

### Terraform

```hcl
resource "aws_ecr_repository" "<example_resource_name>" {
  name = "<example_resource_name>"

  image_scanning_configuration {
    scan_on_push = true # Critical: enables scanning on image push
  }
}
```

### Other

1. Open the AWS Console and go to Amazon ECR
2. Click Repositories and select the target repository
3. Click Edit
4. Enable the Scan on push toggle
5. Click Save

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECR/scan-on-push.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ECR/scan-on-push.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic-enabling.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic-enabling.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)

## 技術情報

- Source Metadata：[sources/aws/ecr_repositories_scan_images_on_push_enabled/metadata.json](../../sources/aws/ecr_repositories_scan_images_on_push_enabled/metadata.json)
- Source Code：[sources/aws/ecr_repositories_scan_images_on_push_enabled/check.py](../../sources/aws/ecr_repositories_scan_images_on_push_enabled/check.py)
- Source Metadata Path：`sources/aws/ecr_repositories_scan_images_on_push_enabled/metadata.json`
- Source Code Path：`sources/aws/ecr_repositories_scan_images_on_push_enabled/check.py`

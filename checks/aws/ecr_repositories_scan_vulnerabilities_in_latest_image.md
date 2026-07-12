# ECR repository latest image is scanned with no vulnerabilities at or above the configured minimum severity

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecr_repositories_scan_vulnerabilities_in_latest_image` |
| クラウドプラットフォーム | AWS |
| サービス | ecr |
| 重大度 | medium |
| カテゴリ | container-security |
| チェックタイプ | Software and Configuration Checks/Vulnerabilities/CVE, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsEcrRepository |
| リソースグループ | container |

## 説明

**Amazon ECR repositories** are assessed on the most recent pushed image to confirm a vulnerability scan exists, completed successfully, and that no results meet or exceed the configured minimum severity (e.g., `CRITICAL`, `HIGH`, `MEDIUM`).

## リスク

Unscanned or high-severity findings in container images expose workloads to exploitation of known CVEs. Attackers can gain code execution, exfiltrate data, alter services, or disrupt operations, enabling **lateral movement** and supply-chain compromise-impacting **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Enable **continuous scanning** for repositories and enforce deployment gates at your policy threshold (e.g., `MEDIUM`+). Rebuild images with patched components and updated bases, keep images minimal, and apply **least privilege**. Use **image signing** and CI/CD checks so only scanned, compliant images can run.

## 修正手順


### Native IaC

```yaml
# Enable scan on push so the latest image is automatically scanned
Resources:
  EcrRepository:
    Type: AWS::ECR::Repository
    Properties:
      RepositoryName: <example_resource_name>
      ImageScanningConfiguration:
        ScanOnPush: true  # CRITICAL: ensures each pushed image is scanned so the latest has scan results
```

### Terraform

```hcl
# Enable scan on push so the latest image is automatically scanned
resource "aws_ecr_repository" "<example_resource_name>" {
  name = "<example_resource_name>"

  image_scanning_configuration {
    scan_on_push = true  # CRITICAL: ensures each pushed image is scanned so the latest has scan results
  }
}
```

### Other

1. In the AWS Console, go to ECR > Repositories > <example_resource_name>
2. Click Edit and enable Scan on push, then Save
3. Rebuild the container image to remove vulnerabilities and push a new tag to the repository
4. Open the image details and click Scan image (if not auto-scanned)
5. Confirm Findings show 0 vulnerabilities at or above the required severity

## 参考資料

- [https://www.geeksforgeeks.org/devops/how-to-manage-image-security-and-vulnerabilities-in-ecr/](https://www.geeksforgeeks.org/devops/how-to-manage-image-security-and-vulnerabilities-in-ecr/)
- [https://aws.amazon.com/blogs/aws/amazon-inspector-enhances-container-security-by-mapping-amazon-ecr-images-to-running-containers/](https://aws.amazon.com/blogs/aws/amazon-inspector-enhances-container-security-by-mapping-amazon-ecr-images-to-running-containers/)
- [https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html)

## 技術情報

- Source Metadata：[sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/metadata.json](../../sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/metadata.json)
- Source Code：[sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/check.py](../../sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/check.py)
- Source Metadata Path：`sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/metadata.json`
- Source Code Path：`sources/aws/ecr_repositories_scan_vulnerabilities_in_latest_image/check.py`

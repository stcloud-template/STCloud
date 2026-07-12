# ECR registry has image scanning on push enabled for all repositories

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ecr_registry_scan_images_on_push_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ecr |
| 重大度 | medium |
| カテゴリ | container-security |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | container |

## 説明

Amazon ECR registries with repositories are evaluated for image scanning configured as `scan on push` at the registry level, with scan rules that cover all repositories (no restrictive filters), for either **basic** or **enhanced** scanning.

## リスク

Absent or filtered `scan on push` lets **vulnerable images** be pushed and deployed without timely detection, enabling exploitation of known CVEs (RCE, privilege escalation), supply chain compromise, and lateral movement - threatening workload integrity and data confidentiality.

## 推奨事項

Enable registry-wide `scan on push` and ensure rules apply to all repositories (no filters). Prefer **enhanced scanning** for broader coverage, and pair with continuous scans when available. Integrate findings into CI/CD gates and alerts to enforce **defense in depth** and block promotion of risky images.

## 修正手順


### CLI

```text
aws ecr put-registry-scanning-configuration --rules 'scanFrequency=SCAN_ON_PUSH,repositoryFilters=[{filter=string,filterType=WILDCARD}]'
```

### Terraform

```hcl
resource "aws_ecr_registry_scanning_configuration" "<example_resource_name>" {
  scan_type = "ENHANCED"

  rule {
    scan_frequency = "SCAN_ON_PUSH"  # Ensures scan on push
    repository_filter {
      filter      = "*"               # Applies to all repositories
      filter_type = "WILDCARD"
    }
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon ECR
2. In the left menu, click Account settings (or Settings), then find Registry scanning
3. Click Edit
4. Set Scanning type to Enhanced scanning
5. Enable Scan on push
6. Under Repository filters, set Filter type to WILDCARD and Filter to *
7. Click Save

## 参考資料

- [https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)

## 技術情報

- Source Metadata：[sources/aws/ecr_registry_scan_images_on_push_enabled/metadata.json](../../sources/aws/ecr_registry_scan_images_on_push_enabled/metadata.json)
- Source Code：[sources/aws/ecr_registry_scan_images_on_push_enabled/check.py](../../sources/aws/ecr_registry_scan_images_on_push_enabled/check.py)
- Source Metadata Path：`sources/aws/ecr_registry_scan_images_on_push_enabled/metadata.json`
- Source Code Path：`sources/aws/ecr_registry_scan_images_on_push_enabled/check.py`

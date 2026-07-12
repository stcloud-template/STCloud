# Resource Explorer indexes exist

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `resourceexplorer2_indexes_found` |
| クラウドプラットフォーム | AWS |
| サービス | resourceexplorer2 |
| 重大度 | low |
| カテゴリ | forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS Resource Explorer** has user-owned **indexes** present in the account. The assessment determines whether at least one index exists in any enabled Region for resource cataloging and search.

## リスク

Absent indexes reduce asset visibility, creating blind spots where misconfigured or orphaned resources go unnoticed. This degrades **confidentiality** (unseen public exposure), **integrity** (unauthorized changes undetected), and **availability** (slower containment and recovery), prolonging incident response and enabling lateral movement.

## 推奨事項

Create **Resource Explorer indexes** in all active Regions and designate an **aggregator index** for cross-Region search. Apply least-privilege access to views, align with tagging standards, and routinely verify indexing status. This improves inventory accuracy, supports defense-in-depth, and speeds detection and remediation.

## 修正手順


### CLI

```text
aws resource-explorer-2 create-index --region <REGION>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ResourceExplorer2::Index
    Properties:
      Type: LOCAL  # Critical: creates a local index in this Region so the check finds at least one index
```

### Terraform

```hcl
resource "aws_resourceexplorer2_index" "<example_resource_name>" {
  type = "LOCAL"  # Critical: creates a local index so the check passes
}
```

### Other

1. Sign in to the AWS Management Console and open **AWS Resource Explorer**
2. Go to **Settings** > **Indexes**
3. Click **Create indexes**
4. Select the current Region and click **Create indexes**
5. Wait until the index state is ACTIVE

## 参考資料

- [https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-on-region.html](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-on-region.html)

## 技術情報

- Source Metadata：[sources/aws/resourceexplorer2_indexes_found/metadata.json](../../sources/aws/resourceexplorer2_indexes_found/metadata.json)
- Source Code：[sources/aws/resourceexplorer2_indexes_found/check.py](../../sources/aws/resourceexplorer2_indexes_found/check.py)
- Source Metadata Path：`sources/aws/resourceexplorer2_indexes_found/metadata.json`
- Source Code Path：`sources/aws/resourceexplorer2_indexes_found/check.py`

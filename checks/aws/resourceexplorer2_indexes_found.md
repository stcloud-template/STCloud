# Resource Explorer indexes exist

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `resourceexplorer2_indexes_found` |
| 云平台 | AWS |
| 服务 | resourceexplorer2 |
| 严重等级 | low |
| 类别 | forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | Other |
| 资源组 | governance |

## 描述

**AWS Resource Explorer** has user-owned **indexes** present in the account. The assessment determines whether at least one index exists in any enabled Region for resource cataloging and search.

## 风险

Absent indexes reduce asset visibility, creating blind spots where misconfigured or orphaned resources go unnoticed. This degrades **confidentiality** (unseen public exposure), **integrity** (unauthorized changes undetected), and **availability** (slower containment and recovery), prolonging incident response and enabling lateral movement.

## 推荐措施

Create **Resource Explorer indexes** in all active Regions and designate an **aggregator index** for cross-Region search. Apply least-privilege access to views, align with tagging standards, and routinely verify indexing status. This improves inventory accuracy, supports defense-in-depth, and speeds detection and remediation.

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-on-region.html](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-turn-on-region.html)

## 技术信息

- Source Metadata：[sources/aws/resourceexplorer2_indexes_found/metadata.json](../../sources/aws/resourceexplorer2_indexes_found/metadata.json)
- Source Code：[sources/aws/resourceexplorer2_indexes_found/check.py](../../sources/aws/resourceexplorer2_indexes_found/check.py)
- Source Metadata Path：`sources/aws/resourceexplorer2_indexes_found/metadata.json`
- Source Code Path：`sources/aws/resourceexplorer2_indexes_found/check.py`

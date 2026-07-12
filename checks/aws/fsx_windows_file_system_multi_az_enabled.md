# FSx Windows file system is configured for Multi-AZ deployment

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `fsx_windows_file_system_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | fsx |
| 重大度 | low |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | storage |

## 説明

**FSx for Windows File Server** file systems are evaluated for **Multi-AZ deployment**, determined when `SubnetIds` include more than one subnet in different Availability Zones.

## リスク

Using **Single-AZ** creates a **single point of failure**. AZ outages, server failures, or maintenance can cause extended file share downtime, impacting availability. Crash scenarios may leave data inconsistent, threatening **integrity**, and recovery may rely on backups, increasing **RTO/RPO**.

## 推奨事項

Prefer `MULTI_AZ_1` for production to uphold **high availability** and avoid AZ-level single points of failure. Apply **resilience** and **defense in depth**: design to tolerate AZ loss, capacity-plan for failover, and test failover regularly. *If Single-AZ is unavoidable*, limit to noncritical or app-replicated workloads and keep frequent, verified backups.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create FSx for Windows File Server with Multi-AZ
Resources:
  <example_resource_name>:
    Type: AWS::FSx::FileSystem
    Properties:
      FileSystemType: WINDOWS
      StorageCapacity: 32
      SubnetIds:
        - <example_subnet_id_1>  # CRITICAL: two subnets -> Multi-AZ across AZs
        - <example_subnet_id_2>  # CRITICAL: two subnets -> Multi-AZ across AZs
      WindowsConfiguration:
        ThroughputCapacity: 8
        DeploymentType: MULTI_AZ_1  # CRITICAL: enables Multi-AZ deployment
        PreferredSubnetId: <example_subnet_id_1>
```

### Terraform

```hcl
# Terraform: FSx for Windows File Server configured for Multi-AZ
resource "aws_fsx_windows_file_system" "<example_resource_name>" {
  storage_capacity    = 32
  subnet_ids          = ["<example_subnet_id_1>", "<example_subnet_id_2>"] # CRITICAL: two subnets in different AZs
  throughput_capacity = 8
  deployment_type     = "MULTI_AZ_1"                                      # CRITICAL: enables Multi-AZ deployment
  preferred_subnet_id = "<example_subnet_id_1>"
}
```

### Other

1. In AWS Console, go to FSx > Create file system > Amazon FSx for Windows File Server
2. Set Deployment type to Multi-AZ
3. Select two Subnets in different Availability Zones
4. Set minimal required capacity/throughput and Create
5. Migrate data to the new file system and repoint clients to its DNS name
6. Delete the old Single-AZ file system

## 参考資料

- [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dfs-r.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dfs-r.html)
- [https://docs.aws.amazon.com/fsx/latest/APIReference/API_WindowsFileSystemConfiguration.html](https://docs.aws.amazon.com/fsx/latest/APIReference/API_WindowsFileSystemConfiguration.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html)
- [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html)

## 技術情報

- Source Metadata：[sources/aws/fsx_windows_file_system_multi_az_enabled/metadata.json](../../sources/aws/fsx_windows_file_system_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/fsx_windows_file_system_multi_az_enabled/check.py](../../sources/aws/fsx_windows_file_system_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/fsx_windows_file_system_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/fsx_windows_file_system_multi_az_enabled/check.py`

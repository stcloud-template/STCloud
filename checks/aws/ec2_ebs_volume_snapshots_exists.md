# Check if EBS snapshots exists.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_volume_snapshots_exists` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | volume |
| 严重等级 | medium |
| 类别 | forensics-ready |
| 检查类型 | Data Protection |
| 资源类型 | AwsEc2Volume |
| 资源组 | storage |

## 描述

Check if EBS snapshots exists.

## 风险

Ensure that your EBS volumes (available or in-use) have recent snapshots (taken weekly) available for point-in-time recovery for a better, more reliable data backup strategy.

## 推荐措施

Creating point-in-time EBS snapshots periodically will allow you to handle efficiently your data recovery process in the event of a failure, to save your data before shutting down an EC2 instance, to back up data for geographical expansion and to maintain your disaster recovery stack up to date.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

## 修复步骤


### CLI

```text
aws ec2 --region <REGION> create-snapshot --volume-id <VOLUME-ID>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/EBS/ebs-volumes-recent-snapshots.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/EBS/ebs-volumes-recent-snapshots.html)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json](../../sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_snapshots_exists/check.py](../../sources/aws/ec2_ebs_volume_snapshots_exists/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_snapshots_exists/check.py`

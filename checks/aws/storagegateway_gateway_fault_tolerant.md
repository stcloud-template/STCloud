# AWS Storage Gateway gateway is not hosted on EC2

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storagegateway_gateway_fault_tolerant` |
| クラウドプラットフォーム | AWS |
| サービス | storagegateway |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | storage |

## 説明

AWS Storage Gateway hosted on an **EC2 instance** is flagged by assessing each gateway's hosting environment, distinguishing **single-instance EC2** deployments from **non-EC2** platforms that can leverage platform-level high availability.

## リスク

A **single EC2-hosted gateway** concentrates failure risk. Instance or AZ disruption, reboots, or network faults can halt file access, causing downtime and stalled writes. This degrades **availability** and can affect **integrity** via partial operations or cache desynchronization.

## 推奨事項

Design for **high availability**: avoid single-instance gateways for critical workloads. Prefer managed multi-AZ services like **EFS** or **FSx**, or use multiple gateways with client failover and resilient naming. Apply **defense in depth**, validate failover regularly, and monitor health to prevent outages.

## 修正手順


### Other

1. In the AWS Console, go to Storage Gateway and click Create gateway
2. Choose your gateway type, then under Host platform select VMware ESXi, Microsoft Hyper-V, Linux KVM, or Hardware Appliance (do not select Amazon EC2)
3. Download and deploy the VM on your host, power it on, and note its IP
4. In the console, connect to and Activate the new gateway
5. Recreate equivalent resources (shares/volumes/tapes) on the new gateway and update clients to use the new gateway IP/DNS
6. In Storage Gateway > Gateways, delete the old EC2-hosted gateway
7. Verify the new gateway's details show Host platform not equal to Amazon EC2

## 参考資料

- [https://docs.aws.amazon.com/filegateway/latest/files3/resource-vm-setup.html](https://docs.aws.amazon.com/filegateway/latest/files3/resource-vm-setup.html)
- [https://docs.aws.amazon.com/filegateway/latest/files3/disaster-recovery-resiliency.html](https://docs.aws.amazon.com/filegateway/latest/files3/disaster-recovery-resiliency.html)

## 技術情報

- Source Metadata：[sources/aws/storagegateway_gateway_fault_tolerant/metadata.json](../../sources/aws/storagegateway_gateway_fault_tolerant/metadata.json)
- Source Code：[sources/aws/storagegateway_gateway_fault_tolerant/check.py](../../sources/aws/storagegateway_gateway_fault_tolerant/check.py)
- Source Metadata Path：`sources/aws/storagegateway_gateway_fault_tolerant/metadata.json`
- Source Code Path：`sources/aws/storagegateway_gateway_fault_tolerant/check.py`

# AWS Storage Gateway gateway is not hosted on EC2

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storagegateway_gateway_fault_tolerant` |
| 云平台 | AWS |
| 服务 | storagegateway |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | Other |
| 资源组 | storage |

## 描述

AWS Storage Gateway hosted on an **EC2 instance** is flagged by assessing each gateway's hosting environment, distinguishing **single-instance EC2** deployments from **non-EC2** platforms that can leverage platform-level high availability.

## 风险

A **single EC2-hosted gateway** concentrates failure risk. Instance or AZ disruption, reboots, or network faults can halt file access, causing downtime and stalled writes. This degrades **availability** and can affect **integrity** via partial operations or cache desynchronization.

## 推荐措施

Design for **high availability**: avoid single-instance gateways for critical workloads. Prefer managed multi-AZ services like **EFS** or **FSx**, or use multiple gateways with client failover and resilient naming. Apply **defense in depth**, validate failover regularly, and monitor health to prevent outages.

## 修复步骤


### Other

1. In the AWS Console, go to Storage Gateway and click Create gateway
2. Choose your gateway type, then under Host platform select VMware ESXi, Microsoft Hyper-V, Linux KVM, or Hardware Appliance (do not select Amazon EC2)
3. Download and deploy the VM on your host, power it on, and note its IP
4. In the console, connect to and Activate the new gateway
5. Recreate equivalent resources (shares/volumes/tapes) on the new gateway and update clients to use the new gateway IP/DNS
6. In Storage Gateway > Gateways, delete the old EC2-hosted gateway
7. Verify the new gateway's details show Host platform not equal to Amazon EC2

## 参考资料

- [https://docs.aws.amazon.com/filegateway/latest/files3/resource-vm-setup.html](https://docs.aws.amazon.com/filegateway/latest/files3/resource-vm-setup.html)
- [https://docs.aws.amazon.com/filegateway/latest/files3/disaster-recovery-resiliency.html](https://docs.aws.amazon.com/filegateway/latest/files3/disaster-recovery-resiliency.html)

## 技术信息

- Source Metadata：[sources/aws/storagegateway_gateway_fault_tolerant/metadata.json](../../sources/aws/storagegateway_gateway_fault_tolerant/metadata.json)
- Source Code：[sources/aws/storagegateway_gateway_fault_tolerant/check.py](../../sources/aws/storagegateway_gateway_fault_tolerant/check.py)
- Source Metadata Path：`sources/aws/storagegateway_gateway_fault_tolerant/metadata.json`
- Source Code Path：`sources/aws/storagegateway_gateway_fault_tolerant/check.py`

# Ensure ‘Enable Connecting to Serial Ports’ Is Not Enabled for VM Instance

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_serial_ports_in_use` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

Interacting with a serial port is often referred to as the serial console, which is similar to using a terminal window, in that input and output is entirely in text mode and there is no graphical interface or mouse support. If you enable the interactive serial console on an instance, clients can attempt to connect to that instance from any IP address. Therefore interactive serial console support should be disabled.

## リスク

If you enable the interactive serial console on your VM instance, clients can attempt to connect to your instance from any IP address and this allows anybody to access the instance if they know the user name, the SSH key, the project ID, and the instance name and zone.

## 推奨事項

Ensure that "Enable connecting to serial ports" configuration setting is disabled for all your production Google Compute Engine instances. A Google Cloud virtual machine (VM) instance has 4 virtual serial ports. On your VM instances, the operating system (OS), BIOS, and other system-level entities write often output data to the serial ports and can accept input, such as commands or answers, to prompts. Usually, these system-level entities use the first serial port (Port 1) and Serial Port 1 is often referred to as the interactive serial console. This interactive serial console does not support IP-based access restrictions such as IP address whitelists. To adhere to cloud security best practices and reduce the risk of unauthorized access, interactive serial console support should be disabled for all instances used in production.

- 推奨リンク：[https://cloud.google.com/compute](https://cloud.google.com/compute)

## 修正手順


### CLI

```text
gcloud compute instances add-metadata <INSTANCE_NAME> --zone=<ZONE> --metadata=serial-port-enable=false
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_11#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_11#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-interactive-serial-console-support.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-interactive-serial-console-support.html)

## 参考資料

- [https://cloud.google.com/compute](https://cloud.google.com/compute)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_serial_ports_in_use/metadata.json](../../sources/gcp/compute_instance_serial_ports_in_use/metadata.json)
- Source Code：[sources/gcp/compute_instance_serial_ports_in_use/check.py](../../sources/gcp/compute_instance_serial_ports_in_use/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_serial_ports_in_use/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_serial_ports_in_use/check.py`

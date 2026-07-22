# ST Cloud AWS Templates

This repository hosts public AWS onboarding templates for ST Cloud.

Current template baseline: ST Cloud AWS onboarding `5.35.0-stcloud.1`.

- CloudFormation template: `templates/aws/cloudformation/stcloud-scan-role.yml`
- Terraform template: `templates/aws/terraform/`

The CloudFormation raw URL is used by the ST Cloud AWS quick-create link.

The trusted AWS account ID and IAM principal are required inputs. The templates do not hardcode a third-party trust account.

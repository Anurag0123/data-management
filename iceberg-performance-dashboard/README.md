# Iceberg Athena Dashboard

This repository provides code to create a production-ready CloudWatch dashboard to monitor Iceberg table performance and Athena query executions.

## Features
- **Custom Metrics**: Tracks Iceberg table metadata such as partitions and data size.
- **Athena Query Insights**: Displays query logs, execution time, and scanned partitions.

## Structure
- `lambda`: Lambda function to collect Iceberg metadata.
- `terraform`: Terraform code to set up CloudWatch Dashboard and Lambda.
- `cloudwatch-dashboard.json`: Pre-configured dashboard template.

## Deployment
1. Deploy Lambda: Upload `metadata_collector.zip` to AWS Lambda.
2. Apply Terraform: Use `terraform init` and `terraform apply`.
3. Monitor: View metrics and logs in CloudWatch.

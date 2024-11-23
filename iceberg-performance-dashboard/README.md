<<<<<<< HEAD
# Iceberg Athena Dashboard

This repository provides code to create a production-ready CloudWatch dashboard to monitor Iceberg table performance and Athena query executions.

## Features
- **Custom Metrics**: Tracks Iceberg table metadata such as partitions and data size.
- **Athena Query Insights**: Displays query logs, execution time, and scanned partitions.

## Structure
- `dashboard/lambda`: Lambda function to collect Iceberg metadata.
- `dashboard/terraform`: Terraform code to set up CloudWatch Dashboard and Lambda.
- `dashboard/cloudwatch-dashboard.json`: Pre-configured dashboard template.

## Deployment
1. Deploy Lambda: Upload `metadata_collector.zip` to AWS Lambda.
2. Apply Terraform: Use `terraform init` and `terraform apply`.
3. Monitor: View metrics and logs in CloudWatch.

=======
# Data-Oriented Projects Repository

Welcome to the **Data-Oriented Projects** repository! 🎉  

This repository will serve as a collection of diverse data-driven projects, ranging from **data engineering** to **data analysis** and **machine learning**. The aim is to explore real-world datasets, experiment with modern tools and technologies, and solve interesting data challenges.  

Stay tuned for exciting projects and updates!  

## Objectives
- Build scalable data pipelines  
- Explore innovative data transformation and modeling techniques  
- Utilize cloud platforms and frameworks  

### Contributions and collaboration are welcome! 🚀
>>>>>>> 4215dc3872e7957274d56e3c9d289c1689a621fa

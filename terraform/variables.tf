variable "athena_database" {
  description = "Athena database name for querying Iceberg metadata"
  type        = string
}

variable "athena_output_location" {
  description = "S3 bucket for Athena query results"
  type        = string
}

variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}
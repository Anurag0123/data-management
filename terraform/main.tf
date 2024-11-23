provider "aws" {
  region = "us-east-1"
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_exec" {
  name               = "IcebergLambdaExecutionRole"
  assume_role_policy = file("${path.module}/lambda_trust_policy.json")
}

# Lambda Policy Attachment
resource "aws_iam_policy" "lambda_policy" {
  name        = "IcebergLambdaPolicy"
  description = "Policy for accessing Athena and publishing metrics"
  policy      = file("${path.module}/lambda_policy.json")
}

resource "aws_iam_role_policy_attachment" "lambda_attach" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

# Lambda Function
resource "aws_lambda_function" "metadata_collector" {
  filename         = "metadata_collector.zip"
  function_name    = "IcebergMetadataCollector"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "metadata_collector.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = filebase64sha256("metadata_collector.zip")

  environment {
    variables = {
      ATHENA_DATABASE       = var.athena_database
      ATHENA_OUTPUT_LOCATION = var.athena_output_location
    }
  }
}

# CloudWatch Dashboard
resource "aws_cloudwatch_dashboard" "iceberg_dashboard" {
  dashboard_name = "IcebergAthenaDashboard"
  dashboard_body = file("${path.module}/../cloudwatch-dashboard.json")
}
import boto3
import os
from datetime import datetime

# AWS clients
athena = boto3.client('athena')
cloudwatch = boto3.client('cloudwatch')

# Environment variables
namespace = 'IcebergPerformance'
athena_db = os.environ['ATHENA_DATABASE']
output_location = os.environ['ATHENA_OUTPUT_LOCATION']

# Helper function to run Athena queries
def run_athena_query(query):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': athena_db},
        ResultConfiguration={'OutputLocation': output_location}
    )
    query_execution_id = response['QueryExecutionId']
    return query_execution_id

# Wait for Athena query to complete and get results
def get_query_results(query_execution_id):
    while True:
        status = athena.get_query_execution(QueryExecutionId=query_execution_id)['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED']:
            break
    if status == 'FAILED':
        raise Exception("Athena query failed.")
    result = athena.get_query_results(QueryExecutionId=query_execution_id)
    return result['ResultSet']['Rows']

# Publish metrics to CloudWatch
def publish_metric(metric_name, table_name, value, unit):
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions': [{'Name': 'TableName', 'Value': table_name}],
                'Value': float(value),
                'Unit': unit
            }
        ]
    )

def lambda_handler(event, context):
    queries = {
        "FileCount": "SELECT table_name, COUNT(file_path) AS file_count FROM iceberg_metadata.files GROUP BY table_name;",
        "TableSizeGB": "SELECT table_name, ROUND(SUM(file_size) / POWER(1024, 3), 2) AS table_size_gb FROM iceberg_metadata.files GROUP BY table_name;",
        "SnapshotTime": "SELECT table_name, MAX(snapshot_timestamp) AS latest_snapshot_time FROM iceberg_metadata.snapshots GROUP BY table_name;"
    }

    for metric_name, query in queries.items():
        execution_id = run_athena_query(query)
        results = get_query_results(execution_id)[1:]  # Skip header row
        for row in results:
            table_name, value = row['Data'][0]['VarCharValue'], row['Data'][1]['VarCharValue']
            unit = 'Count' if metric_name == 'FileCount' else ('Gigabytes' if metric_name == 'TableSizeGB' else 'Milliseconds')
            publish_metric(metric_name, table_name, value, unit)

    return {"statusCode": 200, "body": "Metrics published successfully"}
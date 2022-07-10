import boto3

client = boto3.client('rds')

response = client.describe_db_clusters(
    DBInstanceIdentifier='database-3',
)
print(response)


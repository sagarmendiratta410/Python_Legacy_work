# Importing boto3 library to make functionality available
import boto3
# Creating a client connection with AWS S3 
s3 = boto3.client('s3')
# Creating a bucket
s3.create_bucket(Bucket='first-us-east-1-bucket')
print("Bucket created succesfully")
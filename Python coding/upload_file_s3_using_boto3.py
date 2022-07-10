# Importing boto3 library
import boto3
# Creating a client connection with AWS S3
s3 = boto3.client('s3')
# Read the file stored on your local machine
with open('~/ATA.txt', 'rb') as data:
# Upload the file ATA.txt within the Myfolder on S3
  s3.upload_fileobj(data, 'first-us-east-1-bucket', '~/ATA.txt')
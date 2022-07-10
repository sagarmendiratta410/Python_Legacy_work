# Importing boto3 library
import boto3
# Creating the connection with the resource
s3 = boto3.resource('s3')
# Declaring the source to be copied
copy_source = {
	'Bucket': 'first-us-east-1-bucket',
	'Key': 'ATA.txt'
}
bucket = s3.Bucket('first-us-east-1-bucket-2')
# Copying the files to another bucket
bucket.copy(copy_source, 'ATA.txt')
import boto3
import os
import zipfile

s3 = boto3.client('s3')

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
zipf = zipfile.ZipFile('ATA.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('ATA', zipf)
zipf.close()

with open('ATA.zip', 'rb') as data:
    s3.upload_fileobj(data, 'first-us-east-1-bucket', 'folder2/ATA.zip')

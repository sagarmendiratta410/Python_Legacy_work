import json
import botocore 
import boto3

client = boto3.client('rds')
import botocore.session 
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache( config = cache_config, client = client)

secret = cache.get_secret_string('MySecret_ata')
y = json.loads(secret)
store = y["password"]
print(store)








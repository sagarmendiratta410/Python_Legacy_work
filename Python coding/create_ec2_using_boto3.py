import boto3
ec2 = boto3.resource('ec2')
# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-013f17f36f8b1fefb',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
 )
print("EC2 Launched succesfully")
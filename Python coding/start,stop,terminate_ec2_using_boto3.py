import boto3
# Creating a client connection with AWS EC2 
ec2 = boto3.client('ec2')
ec2 = boto3.resource('ec2')
response = ec2.stop_instances(
	    InstanceIds=[
        'i-03e3d79d5def39c75',
    ],
)
response = ec2.start_instances(
    InstanceIds=[
        'i-03e3d79d5def39c75',
    ],
)
response = ec2.terminate_instances(
    InstanceIds=[
        'i-03e3d79d5def39c75',
    ],
)
import boto3
ec2 = boto3.resource('ec2')
response = ec2.create_tags(
    Resources=[
        'i-03e3d79d5def39c75',
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Boto3'
        },
    ]
)
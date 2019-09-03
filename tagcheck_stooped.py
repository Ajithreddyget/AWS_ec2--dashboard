import boto3
def get_instances_by_tag_value( tag, value):
        ec2 = boto3.resource('ec2','us-east-2')
        instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:' + tag, 'Values': [value]},{'Name': 'instance-state-name', 'Values': ['stopped']}])
        for instance in instances:
                print(instance.id, instance.instance_type)

get_instances_by_tag_value('BILLING', 'RD')

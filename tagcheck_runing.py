import boto3
icount=[]
region=['eu-north-1','ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-east-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-2','us-west-1']
def get_instances_by_tag_value( tag, value):
        for i in region:
                ec2 = boto3.resource('ec2',i)
                print(i)
                instances = ec2.instances.filter(
                Filters=[{'Name': 'tag:' + tag, 'Values': [value]},{'Name': 'instance-state-name', 'Values': ['running']}])
                instanceid=[]
                for instance in instances:
                        instanceid.append(str(instance.id))
                       
                print(len(instanceid))
                icount.append(len(instanceid))
      

get_instances_by_tag_value('PROJECT','AWS-MIGRATION')
print('The total instance count: ',sum(icount))
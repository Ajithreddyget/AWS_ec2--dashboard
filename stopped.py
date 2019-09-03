import boto3 
import matplotlib.pyplot as plt

region=['eu-north-1','ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-east-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-2','us-west-1']
activecount=[]
for i in region:
        ec2 = boto3.resource('ec2',i)
        print(i)
        instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
        # values can be terminatted and stopped can be included 
        instanceid=[]
        for instance in instances:
            instanceid.append(str(instance.id))
            
        print(len(instanceid))
        activecount.append(len(instanceid))
      
print(activecount)
#plot the graph

fig, ax = plt.subplots(figsize=(13, 10), subplot_kw=dict(aspect="equal"))
plt.pie(activecount, labels=region,autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.show()

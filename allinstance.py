import boto3
import matplotlib.pyplot as plt

region=['eu-north-1','ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-east-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-2','us-west-1']
ec2count=[]
for i in region:
        ec2 = boto3.resource('ec2',i)
        print(i)
        instance = ec2.instances.all()
        #print(instance)
        listidr = []
        for instance in ec2.instances.all():   
                #print(instance.id)
                listidr.append(str(instance.id))
        ec2count.append(len(listidr))
        print(len(listidr))
print(ec2count)
#plotting the graph

fig, ax = plt.subplots(figsize=(13, 10), subplot_kw=dict(aspect="equal"))
plt.pie(ec2count, labels=region,autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.show()
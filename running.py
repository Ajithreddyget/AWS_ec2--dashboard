import boto3 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
region=boto3.client('ec2')
allreg=[region['RegionName'] for region in region.describe_regions()['Regions']]
activecount=[]
for i in allreg:
        ec2 = boto3.resource('ec2',i)
        print(i)
        instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        # values can be terminatted and stopped can be included 
        instanceid=[]
        for instance in instances:
            instanceid.append(str(instance.id))
            
        print(len(instanceid))
        activecount.append(len(instanceid))
      


#plot the graph

#get the index of zero value in a list
zeroindex=[i for i, e in enumerate(activecount) if e == 0]
# Remove the zero value region in a list using enumerate 
regionnonzero = [i for j, i in enumerate(region) if j not in zeroindex]
print(regionnonzero)
#Remove the zero value present index in the count
countnonzero=[i for j, i in enumerate(activecount) if j not in zeroindex]
print(countnonzero)
print("Total running instancce in all Region:",sum(activecount))

#plot the data
raw_data = {'Active_regions': regionnonzero,
        'Number_of running instances': countnonzero}
df = pd.DataFrame(raw_data,columns = ['Number_of running instances','Active_regions'])
fig, ax = plt.subplots(figsize=(13, 10), subplot_kw=dict(aspect="equal"))
plt.pie(countnonzero, labels=regionnonzero,autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.show()
df

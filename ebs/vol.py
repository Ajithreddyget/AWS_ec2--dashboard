import boto3
region=boto3.client('ec2')
allreg=[region['RegionName'] for region in region.describe_regions()['Regions']]
for regions in allreg:
    print(regions)
    ec2 = boto3.resource('ec2',regions)
    vol = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']} or {'Name':'tag:ENVIRONMENT', 'Values':['*']} or {'Name':'tag:BILLING', 'Values':['*']}])
    for volm in vol:
        print (volm.id,volm.size)
        vol = ec2.Volume(id=volm.id)
        name = None
        for tag in vol.tags:
            if tag['Key'] == 'Name':
                name = tag.get('Value')
                print(name)
        

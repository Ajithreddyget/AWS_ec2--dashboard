# AWS_ec2-live-dashboard
This python module can be used for monitoring and alerting for the EC2 resource for the AWS instance.

For what this script?
1. List and plot all running instance in AWS account.(including all regions)
2. List and plot of all running, stopped and terminated instance 
3. Plot graph based on paricular project [If the instance is tagged]


allinstance.py --> will give the all list of instance (running,stopped)
running.py --> will give only running instance 
stopped.py --> will give only stopped instnces
tagcheck_stopped --> will give the list of stopped instance based on tage
tagcheck_running --> will give the list of running instance based on tage

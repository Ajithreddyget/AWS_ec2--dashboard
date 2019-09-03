import boto3

client = boto3.client('ce', region_name='us-east-1')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2018-10-01',
        'End': '2018-10-31'
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)

print(response)
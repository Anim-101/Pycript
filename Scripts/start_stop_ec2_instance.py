import json
import boto3;
import urllib3;

region = ''
instances = ['']
ec2 = boto3.client('ec2', region_name=region)

client = boto3.client
slack_webhook_url = ""


def lambda_handler(event, context):
    instanceState = event['queryStringParameters']['instanceState']
    http = urllib3.PoolManager()
    
    if instanceState == "start":
        response = ec2.start_instances(InstanceIds=instances)
        start_response = http.request("POST", 
                                      slack_webhook_url,
                                      body = json.dumps({"text": ""}),
                                      headers = {"Content-type": "application/json"}
                                    )
    elif instanceState == "stop":
        response = ec2.stop_instances(InstanceIds=instances)
        stop_response = http.request("POST", 
                                      slack_webhook_url,
                                      body = json.dumps({"text": ""}),
                                      headers = {"Content-type": "application/json"}
                                    )
    else:
        response = {
            "error": "You should use instanceState=start or instanceState=stop as parametters!"
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
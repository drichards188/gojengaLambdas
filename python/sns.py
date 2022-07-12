import json
import boto3


def lambda_handler(event, context):
    sns_pub()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def sns_pub():
    message = {
        "data": "thisismydata"
    }
    client = boto3.client('sns')

    # sns target is protected to only owner so doesn't need to be scrubbed
    response = client.publish(
        TargetArn="arn:aws:sns:us-east-2:585068124165:topic1",
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )

    print(response)
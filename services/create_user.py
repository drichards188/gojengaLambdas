import boto3

def lambda_handler(event, context):
    # print("--> Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    print("--> From SNS: " + message)
    dynamo_crt(message)
    return message

def dynamo_crt(message):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    data = message["data"]

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('dynamoTest')

    try:
        response = table.put_item(
            Item={
                'Account': message,
                'Amount': 200,
                'Password': 'thisisthepassword',
            }
        )

    except Exception as e:
        print(e)

    # Print out some data about the table.
    # This will cause a request to be made to DynamoDB and its attribute
    # values will be set based on the response.
    print("insert complete")

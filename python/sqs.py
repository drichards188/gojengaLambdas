import boto3
import json

event: dict = {
  "operation": "process"
}

def lambda_handler(event):

    if event["operation"] == "publish":
        sqs_pub()
    elif event["operation"] == "process":
        sqs_process()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def sqs_pub():
    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='queue1')

    # Create a new message
    response = queue.send_message(MessageBody='hiyafuturedavidsqs1')

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

def sqs_process():
    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='queue1')

    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            if author_name:
                author_text = ' ({0})'.format(author_name)

        # Print out the body and author (if set)
        print('Hello, {0}!{1}'.format(message.body, author_text))

        # Let the queue know that the message is processed
        message.delete()

lambda_handler(event)
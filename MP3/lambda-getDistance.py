import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    # Log the received event to CloudWatch
    logger.info('Received event: ' + json.dumps(event))
    
    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('mp3')  
    
    # Extract slots from the event object
    try:
        from_city = event['sessionState']['intent']['slots']['Source']['value']['interpretedValue']
        to_city = event['sessionState']['intent']['slots']['Destination']['value']['interpretedValue']
    except KeyError as e:
        logger.error(f"KeyError: {str(e)} - Event structure may have changed or slots are missing.")
        raise e
    
    # If both slots are filled, fetch distance
    try:
        response = table.get_item(
            Key={
                'source': from_city,  
                'destination': to_city
            }
        )
    except Exception as e:
        logger.error(f"Error fetching from DynamoDB: {str(e)}")
        raise e
        
    # Prepare message
    if 'Item' in response:
        distance = response['Item'].get('distance', "-1")
        content_message = f"{distance}"
    else:
        content_message = "-1"
    
    # Return a response back to Lex
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled"
            },
            "intent": {
                "name": "getDistance",
                "state": "Fulfilled",
                "confirmationState": "Confirmed"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": content_message
            }
        ]
    }

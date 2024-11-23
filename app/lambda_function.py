
import json

def lambda_handler(event, context):
    print("Event received:", event)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello, AWS Lambda!"})
    }

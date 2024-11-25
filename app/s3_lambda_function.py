import json

def lambda_handler(event, context):
    """
    Lambda function to process S3 ObjectCreated:Put events and print details.
    """
    try:
        # Print the entire event for debugging
        print("Received event:", json.dumps(event, indent=2))

        # Loop through each record in the event
        for record in event['Records']:
            event_name = record['eventName']  # e.g., ObjectCreated:Put
            bucket_name = record['s3']['bucket']['name']  # Bucket name
            object_key = record['s3']['object']['key']  # Object key

            # Print details about the bucket and object
            print(f"Event: {event_name}")
            print(f"Bucket: {bucket_name}")
            print(f"Object Key: {object_key}")

        # Return a success response
        return {"statusCode": 200, "body": "Event processed successfully"}

    except Exception as e:
        # Log any errors
        print(f"Error processing event: {str(e)}")
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

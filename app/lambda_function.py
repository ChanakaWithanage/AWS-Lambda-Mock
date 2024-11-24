import json
from utils import preprocess_text, log_event
from textblob import TextBlob

def lambda_handler(event, context):
    """
    AWS Lambda Handler.
    Analyzes sentiment of a given text passed in the event.
    """
    try:
        log_event("Event received", event)
        print(f"Event received: {event}")

        # Extract text from the event
        text = event.get("text", "")
        if not text:
            raise ValueError("No text provided in the event")

        log_event("Text extracted from event", {"text": text})
        print(f"Text extracted from event: {text}")

        # Preprocess the text using utils
        cleaned_text = preprocess_text(text)
        log_event("Text after preprocessing", {"cleaned_text": cleaned_text})
        print(f"Text after preprocessing: {cleaned_text}")

        # Perform sentiment analysis using TextBlob
        sentiment = TextBlob(cleaned_text).sentiment
        log_event("Sentiment analysis result", {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        })
        print(f"Sentiment analysis result: polarity={sentiment.polarity}, subjectivity={sentiment.subjectivity}")

        # Prepare the response
        response = {
            "original_text": text,
            "cleaned_text": cleaned_text,
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity,
        }

        log_event("Processing complete", response)
        print(f"Processing complete: {response}")
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        log_event("Error occurred", {"error": str(e)})
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
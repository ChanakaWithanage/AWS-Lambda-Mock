import re
import logging
import json

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def preprocess_text(text):
    """
    Preprocess the given text by removing special characters and extra spaces.
    """
    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

def log_event(message, data):
    """
    Log events for debugging or monitoring.
    """
    logging.info(f"{message}: {json.dumps(data)}")
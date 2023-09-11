"""Module providingFunction printing python version."""
import logging
from slack_sdk import WebClient

# test.py
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
client = WebClient()
api_response = client.api_test()

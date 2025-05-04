import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

body ={
    "prompt":"\n\nHuman: Summarize this: 'This laptop is fast but has a short battery life.'\n\nAssistant:",
    "max_tokens_to_sample": 100
}

model_id = "anthropic.claude-v2"

print("Bedrock would be invoked here with:")
print("Model:", model_id)
print("Body:", json.dumps(body, indent=2))
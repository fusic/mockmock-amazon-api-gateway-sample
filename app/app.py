import json

def auth(event, context):
    auth_key = event["pathParameters"]["auth_key"]
    return {"statusCode": 200, "body": auth_key}


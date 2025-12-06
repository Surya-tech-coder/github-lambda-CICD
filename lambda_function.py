import json

def lambda_handler(event, context):
    print("Hello from Lambda! GOOD MORNING and have a nice day")
    
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda! Super Siddharth super and deploy🚀")
    }

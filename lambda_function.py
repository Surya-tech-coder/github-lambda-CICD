import json

def lambda_handler(event, context):
    print("Hello from Lambda! GOOD MORNING")
    
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda! Super Siddharth 🚀")
    }

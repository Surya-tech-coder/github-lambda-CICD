import json
import pandas as pd

def lambda_handler(event, context):
    # Create dummy data for demonstration
    data = {
        'col1': [1, 2], 
        'col2': [3, 4]
    }
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data=data)
    
    # Print the DataFrame to the logs
    print(df)
    print("Done x1.1")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! super')
    }
import json


def lambda_handler(event, _):
    # Introduce Lambda logic
    
    # lambda_version = "stable version v_2023_08"
    lambda_version = "dev version"

    return {
        'statusCode': 200,
        'body': json.dumps({'lambda_version': lambda_version})
    }

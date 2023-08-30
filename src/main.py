import json


def lambda_handler(event, _):
    # Introduce Lambda logic
    ## First lambda version
    lambda_version = "version_prd"

    return {
        'statusCode': 200,
        'body': json.dumps({'lambda_version': lambda_version})
    }

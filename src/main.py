import json


def lambda_handler(event, _):
    # Introduce Lambda logic
    
    lambda_version = "stable version v_2023_08"
    stage = event["stageVariables"]["lambdaAlias"]

    # one comment
    # lambda_version = "dev version runing tests"

    return {
        'statusCode': 200,
        'body': json.dumps({'lambda_version': lambda_version})
    }

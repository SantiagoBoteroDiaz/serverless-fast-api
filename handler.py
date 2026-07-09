import json

def hola_mundo(event, context):
    body = {
        "mensaje": "!Hola vienvenido al imalaya quiere un elado?",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def handler(event, context):
    return {
        "statusCode": 200,
        "body": "Hola mundo"
    }
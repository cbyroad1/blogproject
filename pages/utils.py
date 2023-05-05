from django.conf import settings

import boto3
import json 


def send_email(email, subject, message):
    lambda_client = boto3.client(
        'lambda', 
        region_name=settings.REGION_NAME, 
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )

    function_name = settings.FUNCTION_NAME
    payload = {
    'from_email': email,
    'to_email': settings.MY_EMAIL,
    'subject': subject,
    'message': message
    }

    try: 
        lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload)
        )
        result = "Success"
    except:
        result = "There was an error invoking the Lambda function"

    return result    

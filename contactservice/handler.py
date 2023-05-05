import json
import boto3

def sendEmail(event, context):
    ses_client = boto3.client('ses')

    from_email = event['from_email']
    to_email = event['to_email']
    subject = event['subject']
    message = event['message']

    try: 
        ses_client.send_email(
            Source = from_email, 
            Destination = {
                'ToAddresses': [
                    to_email,
                ]
            },
            Message = {
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': message
                    }
                }
            }
        )
        
        code = 200
        x = "This was a success .... i think"
        print(x)

    except:
        code = 400
        x = "There was an error in the email sending"
        print(x)

    return {
        'statusCode': code,
        'body': json.dumps({'message': x})
    }



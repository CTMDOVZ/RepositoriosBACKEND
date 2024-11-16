import boto3

def lambda_handler(event, context):
    
    id_usuario = event['body']['id_usuario']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    
    response = table.get_item(
        Key={
            'id_usuario': id_usuario
        }
    )

   
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'body': 'Usuario no encontrado'
        }

import boto3

def lambda_handler(event, context):
    
    id_usuario = event['body']['id_usuario']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    
    response = table.delete_item(
        Key={
            'id_usuario': id_usuario
        }
    )

    
    return {
        'statusCode': 200,
        'body': 'Usuario eliminado exitosamente'
    }

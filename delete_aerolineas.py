import boto3

def lambda_handler(event, context):
    
    id_aerolinea = event['body']['id_aerolinea']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Aerolíneas')

    
    response = table.delete_item(
        Key={
            'id_aerolinea': id_aerolinea
        }
    )

    
    return {
        'statusCode': 200,
        'body': 'Aerolínea eliminada exitosamente'
    }

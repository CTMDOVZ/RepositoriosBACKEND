import boto3

def lambda_handler(event, context):
    
    id_vuelo = event['body']['id_vuelo']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vuelos')

    
    response = table.delete_item(
        Key={
            'id_vuelo': id_vuelo
        }
    )

    
    return {
        'statusCode': 200,
        'body': 'Vuelo eliminado exitosamente'
    }

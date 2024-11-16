import boto3

def lambda_handler(event, context):
    
    id_aerolinea = event['body']['id_aerolinea']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Aerolíneas')

   
    response = table.get_item(
        Key={
            'id_aerolinea': id_aerolinea
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
            'body': 'Aerolínea no encontrada'
        }

import boto3

def lambda_handler(event, context):
    
    id_vuelo = event['body']['id_vuelo']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vuelos')

    
    response = table.get_item(
        Key={
            'id_vuelo': id_vuelo
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
            'body': 'Vuelo no encontrado'
        }

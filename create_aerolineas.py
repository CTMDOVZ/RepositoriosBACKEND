import boto3

def lambda_handler(event, context):
    
    id_aerolinea = event['body']['id_aerolinea']
    nombre = event['body']['nombre']
    codigo = event['body']['codigo']
    pais_origen = event['body']['pais_origen']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Aerolíneas')

    
    aerolinea = {
        'id_aerolinea': id_aerolinea,
        'nombre': nombre,
        'codigo': codigo,
        'pais_origen': pais_origen
    }

    
    response = table.put_item(Item=aerolinea)

    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': response
    }

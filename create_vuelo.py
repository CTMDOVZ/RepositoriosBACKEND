import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_vuelo = event['body']['id_vuelo']
    id_aerolinea = event['body']['id_aerolinea']
    codigo_vuelo = event['body']['codigo_vuelo']
    origen = event['body']['origen']
    destino = event['body']['destino']
    fecha_salida = event['body']['fecha_salida']
    fecha_llegada = event['body']['fecha_llegada']
    capacidad = event['body']['capacidad']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vuelos')

    
    vuelo = {
        'id_vuelo': id_vuelo,
        'id_aerolinea': id_aerolinea,
        'codigo_vuelo': codigo_vuelo,
        'origen': origen,
        'destino': destino,
        'fecha_salida': fecha_salida,
        'fecha_llegada': fecha_llegada,
        'capacidad': capacidad
    }

    
    response = table.put_item(Item=vuelo)

    
    return {
        'statusCode': 200,
        'body': response
    }

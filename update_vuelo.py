import boto3

def lambda_handler(event, context):
    
    id_vuelo = event['body']['id_vuelo']

    
    atributos = event['body']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vuelos')

    
    update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in atributos if k != 'id_vuelo'])
    expression_values = {f":{k}": v for k, v in atributos.items() if k != 'id_vuelo'}

    
    response = table.update_item(
        Key={
            'id_vuelo': id_vuelo
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )

    
    return {
        'statusCode': 200,
        'body': 'Vuelo actualizado exitosamente'
    }

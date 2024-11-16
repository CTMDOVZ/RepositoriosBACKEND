import boto3

def lambda_handler(event, context):
    
    id_aerolinea = event['body']['id_aerolinea']

    
    atributos = event['body']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Aerolíneas')

    
    update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in atributos if k != 'id_aerolinea'])
    expression_values = {f":{k}": v for k, v in atributos.items() if k != 'id_aerolinea'}

    
    response = table.update_item(
        Key={
            'id_aerolinea': id_aerolinea
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )

    
    return {
        'statusCode': 200,
        'body': 'Aerolínea actualizada exitosamente'
    }

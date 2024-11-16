import boto3

def lambda_handler(event, context):
    
    id_usuario = event['body']['id_usuario']

    
    atributos = event['body']

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    
    update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in atributos if k != 'id_usuario'])
    expression_values = {f":{k}": v for k, v in atributos.items() if k != 'id_usuario'}

    
    response = table.update_item(
        Key={
            'id_usuario': id_usuario
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )

    
    return {
        'statusCode': 200,
        'body': 'Usuario actualizado exitosamente'
    }

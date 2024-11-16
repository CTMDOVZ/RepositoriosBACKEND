import boto3

def lambda_handler(event, context):
    
    id_usuario = event['body']['id_usuario']
    nombre = event['body']['nombre']
    apellido = event['body']['apellido']
    email = event['body']['email']
    telefono = event['body']['telefono']
    tipo_usuario = event['body']['tipo_usuario']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    
    usuario = {
        'id_usuario': id_usuario,
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono,
        'tipo_usuario': tipo_usuario
    }

    
    response = table.put_item(Item=usuario)

    
    return {
        'statusCode': 200,
        'body': response
    }

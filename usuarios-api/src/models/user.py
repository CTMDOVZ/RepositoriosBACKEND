import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

class User:
    @staticmethod
    def create_user(item):
        table.put_item(Item=item)

    @staticmethod
    def get_user(tenant_id, user_id):
        response = table.get_item(Key={'tenant_id': tenant_id, 'id_usuario': user_id})
        return response.get('Item')

    @staticmethod
    def update_user(tenant_id, user_id, update_data):
        response = table.update_item(
            Key={'tenant_id': tenant_id, 'id_usuario': user_id},
            UpdateExpression="SET " + ", ".join(f"{k}=:{k}" for k in update_data),
            ExpressionAttributeValues={f":{k}": v for k, v in update_data.items()},
            ReturnValues="UPDATED_NEW"
        )
        return response

    @staticmethod
    def delete_user(tenant_id, user_id):
        table.delete_item(Key={'tenant_id': tenant_id, 'id_usuario': user_id})

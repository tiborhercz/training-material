import boto3

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    response = client.put_item(
        TableName='NAMEHERE',
        Item={
            'id': {
                'S': '12341234213',
            },
            'Name': {
                'S': 'This is an example name',
            },
        },
    )

    print(response)

import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    slug = (
        event.get("pathParameters", {}).get("slug")
        if event.get("pathParameters")
        else None
    )
    if not slug:
        return {"statusCode": 400, "body": "Slug missing in path"}

    response = table.get_item(Key={"slug": slug})
    item = response.get("Item")

    if not item:
        return {"statusCode": 404, "body": "Not Found"}

    return {
        "statusCode": 302,
        "headers": {"Location": item["long_url"]},
    }
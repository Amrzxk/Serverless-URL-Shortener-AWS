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
        return {"StatusCode": 400, "body": "Slug missing in path"}

    response = table.get_item(Key={"slug": slug})
    item = response.get("Item")

    if not item:
        return {"StatusCode": 404, "body": "Not Found"}

    return {
        "StatusCode": 302,
        "headers": {"Location": item["url"]},
    }
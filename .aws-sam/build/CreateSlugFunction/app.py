# This file handles POST /api/slug
import json
import os
import secrets
import string
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

ALPHABET = string.ascii_letters + string.digits

def _generate_slug(length: int = 6) -> str:
    """Return a random slug like 'aZ93kp'."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))

def lambda_handler(event, context):
    # Parse and validate the request body
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return {"StatusCode": 400, "body": "Invalid JSON"}
    
    long_url = body.get("url")
    if not long_url:
        return {"StatusCode": 400, "body": '"url" is required'}
    
    slug = body.get("slug") or _generate_slug()

    #Persist the slug and long_url to DynamoDB
    try:
        table.put_item(
            Item={"slug": slug, "long_url": long_url},
            ConditionExpression="attribute_not_exists(slug)",
        )
    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        return {"StatusCode": 400, "body": f"Slug '{slug}' already exists"}
    
    # Build the response

    domain = event["headers"].get("host", "")
    proto = event["headers"].get("x-forwarded-proto", "https")
    short_url = f"{proto}://{domain}/{slug}" if domain else slug
    return {
        "StatusCode": 201,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"slug": slug, "short_url": short_url}),
    }
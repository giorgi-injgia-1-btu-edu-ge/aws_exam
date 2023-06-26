import io
import json
from pprint import pprint
from urllib.request import urlopen, Request
import boto3

s3_client = boto3.client("s3")


def lambda_handler(event, _):
    pprint(event)
    for record in event.get("Records"):
        bucket = record.get("s3").get("bucket").get("name")
        key = record.get("s3").get("object").get("key")

        extension_folder = "unknown"
        if '.' in key:
            extension_folder = key.split(".")[-1]
            s3_client.copy_object(Bucket=bucket,
                                  CopySource={
                                      'Bucket': bucket,
                                      'Key': key
                                  },
                                  Key=f"{extension_folder}/{key}")
            s3_client.delete_object(Bucket=bucket, Key=key)
        else:
            s3_client.copy_object(Bucket=bucket,
                                  CopySource={
                                      'Bucket': bucket,
                                      'Key': key
                                  },
                                  Key=f"{extension_folder}/{key}")
            s3_client.delete_object(Bucket=bucket, Key=key)

    return {"statusCode": 200, "body": json.dumps("Done!")}

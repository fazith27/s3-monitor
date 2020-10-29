import json
import boto3
import time
import re
client = boto3.client('s3')


def monitor(event, context):
    for record in event['Records']:
        key = record['s3']['object']['key']
        source_bucket = record['s3']['bucket']['name']
        if key.endswith('.pdf'):
            timezonestring = str(time.time())
            newfileextension = timezonestring+".pdf"
            newkey = "updatedfile/"+re.sub('.pdf$', newfileextension,key)
            copy_source = source_bucket+"/"+key
            copy_response = client.copy_object(Bucket=source_bucket,CopySource=copy_source,Key=newkey)
            delete_response = client.delete_object(Bucket=source_bucket,Key=key)
            print("Copy Response : ", copy_response)
            print("Delete Response after copying: ", delete_response)
        else:
            response = client.delete_object(Bucket=source_bucket,Key=key)
            print("Delete Response for invalid files: ", response)
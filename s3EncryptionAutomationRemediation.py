# This code encrypts the s3 bucket (Contains only main logic)
import boto3 
import json
import os
import sys 
def handler(event, context):

    #parse event
    s3client = boto3.client('s3') 
    reqParams = event['detail']['requestParameters']
    response = s3Client.put_bucket_encryption(
            Bucket=bucketName,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    },
                ]
          })

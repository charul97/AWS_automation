# This code remediates S3 bucket with public access ON and turns it OFF
import boto3
def handler(event, context):
    
    #parse event
    reqParams = event['detail']['requestParameters']
    bucketName= reqParams['bucketName']
    client=boto3.client('s3')                    #added
    response=client.put_public_access_block(
                    Bucket=bucketName,
                    PublicAccessBlockConfiguration={
                      'BlockPublicAcls': True,
                      'IgnorePublicAcls': True,
                      'BlockPublicPolicy': True,
                      'RestrictPublicBuckets': True
                  },
                )

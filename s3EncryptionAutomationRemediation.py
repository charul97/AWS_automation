# This code encrypts the s3 bucket (Contains only main logic)

def handler(event, context):

    #parse event
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

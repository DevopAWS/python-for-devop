import boto3

client = boto3.client('s3')

#S3.Client.create_bucket

#response = client.create_bucket(
 #   Bucket='suresh-demo-boto3-yt-123',
#)

# response = client.get_bucket_acl(
#     Bucket='suresh-demo-boto3-yt-123',
# )
# print(response)

response = client.delete_bucket(
    Bucket='suresh-demo-boto3-yt-123',
)

print(response)
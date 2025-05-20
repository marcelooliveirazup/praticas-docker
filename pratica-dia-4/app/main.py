import boto3
import os

endpoint_url = os.environ.get("AWS_ENDPOINT_URL", "http://localhost:4566")

s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=endpoint_url
)

bucket_name = "meu-bucket-local"

s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' criado com sucesso.")

response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(f" - {bucket['Name']}")

import boto3
from app.core.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from uuid import uuid4

def upload_file_to_s3(file_obj, filename, folder='uploads'):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_S3_REGION_NAME
    )
    unique_filename = f"{folder}/{uuid4()}_{filename}"
    s3.upload_fileobj(file_obj, AWS_STORAGE_BUCKET_NAME, unique_filename, ExtraArgs={"ACL": "public-read"})
    url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{unique_filename}"
    return url 
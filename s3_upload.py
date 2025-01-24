import boto3
import json
from botocore.exceptions import ClientError
import config

BUCKET_NAME = config.BUCKET_NAME
REGION = config.REGION
LOCAL_FILE = config.LOCAL_FILE

def disable_block_public_access(bucket_name):
    """Disable the Block Public Access settings for a bucket."""
    s3 = boto3.client("s3")
    try:
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": False,
                "IgnorePublicAcls": False,
                "BlockPublicPolicy": False,
                "RestrictPublicBuckets": False,
            },
        )
        print(f"Public access block settings disabled for bucket '{bucket_name}'.")
    except ClientError as e:
        print(f"Error disabling public access block: {e}")


def create_s3_bucket(bucket_name, region):
    """Create an S3 bucket in the specified region."""
    s3 = boto3.client("s3")
    try:
        existing_buckets = s3.list_buckets().get("Buckets", [])
        if any(bucket["Name"] == bucket_name for bucket in existing_buckets):
            print(f"Bucket '{bucket_name}' already exists.")
            return False

        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        print(f"Bucket '{bucket_name}' created successfully.")
        return True
    except ClientError as e:
        print(f"Error creating bucket: {e}")
        return False


def upload_file_to_s3(bucket_name, file_path, object_name):
    """Upload a file to an S3 bucket with the correct MIME type."""
    s3 = boto3.client("s3")
    try:
        s3.upload_file(
            file_path,
            bucket_name,
            object_name,
            ExtraArgs={"ContentType": "text/html"}  
        )
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}' with ContentType='text/html'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")


def configure_bucket_for_static_website(bucket_name):
    """Configure the S3 bucket for static website hosting."""
    s3 = boto3.client("s3")
    try:
        s3.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                "IndexDocument": {"Suffix": "index.html"},
                "ErrorDocument": {"Key": "error.html"},
            },
        )
        print(f"Bucket '{bucket_name}' configured for static website hosting.")

        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                }
            ],
        }
        s3.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(bucket_policy),
        )
        print(f"Bucket policy updated to allow public read access.")
    except ClientError as e:
        print(f"Error configuring bucket: {e}")


def verify_file_content_type(bucket_name, object_name):
    """Verify the ContentType of the uploaded file."""
    s3 = boto3.client("s3")
    try:
        response = s3.head_object(Bucket=bucket_name, Key=object_name)
        content_type = response.get("ContentType", "")
        if content_type == "text/html":
            print(f"Verified: File '{object_name}' has correct ContentType='text/html'.")
        else:
            print(f"Warning: File '{object_name}' has ContentType='{content_type}' instead of 'text/html'.")
    except ClientError as e:
        print(f"Error verifying ContentType: {e}")


def generate_static_website_url(bucket_name, region):
    """Generate the static website URL for the bucket."""
    website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
    print(f"\nYour static website is available at: {website_url}")
    return website_url

def main():
    """Main function to run AWS S3 operations."""
    bucket_created = create_s3_bucket(BUCKET_NAME, REGION)

    disable_block_public_access(BUCKET_NAME)

    if bucket_created or True:
        upload_file_to_s3(BUCKET_NAME, LOCAL_FILE, "index.html")
        verify_file_content_type(BUCKET_NAME, "index.html")

        configure_bucket_for_static_website(BUCKET_NAME)

        generate_static_website_url(BUCKET_NAME, REGION)



main()
print("\n Aws s3  static site done...")
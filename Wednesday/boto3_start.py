import boto3

region = "us-west-2"
s3_client = boto3.client('s3', region_name=region)
location = {'LocationConstraint':region}
s3_client.create_bucket(Bucket="bucket-for-my-boto-stuff",CreateBucketConfiguration=location)
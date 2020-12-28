 # boto3 offers 2 types of API's  a) Resource API (high level) works on object oriented object.delete and the other is b) Client API(Low Level) such as it maps directly like put_objects

import boto3

s3client = boto3.client('s3')
bucket_name = "python-sdk-sample11"
print('Creating new bucket {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)

bucket_list = s3client.list_buckets()
for bucket in bucket_list["Buckets"]:
   if bucket['Name'] == bucket_name:
       print("I just Created a new bucket named:{} at {}".format(bucket['Name'],bucket['CreationDate']))

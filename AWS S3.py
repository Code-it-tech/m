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

object_key = "s3.pdf"
s3client.put_object(Bucket=bucket_name,Key=object_key,Body="Uploading the PDF")
print("Uploaded the PDF: {} succesfully to {}".format(object_key,bucket_name))

# Generate the PRE Signed URL

url = s3client.generate_presigned_url('get_object', {'Bucket': bucket_name,'Key': object_key})
print("Try this URL {}".format(url))

s3resource = boto3.resource('s3')
bucket = s3resource.Bucket(bucket_name)

https://github.com/aws-samples/aws-python-sample/blob/master/s3_sample.py
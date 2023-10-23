import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

# client = boto3.client("s3")
# client.upload_file("path/to/file.txt", "your-bucket", "path/to/key.txt")

# s3.put_object(Bucket='bucket-name', Key='object_name', Body='TEST', StorageClass='COLD')

s3.upload_file('./operating_boto3.py', 'amgudym-test', 'operating_boto3.py')

print(s3.list_objects_v2(Bucket='amgudym-test'))

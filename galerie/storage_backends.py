from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

# Create a custom storage backend 
class MediaStorage(S3Boto3Storage):
    location       = 'media'
    default_acl    = 'public-read'
    file_overwrite = False
    custom_domain  = False
    
    def __init__(self, *args, **kwargs):
        kwargs['bucket_name']   = settings.AWS_STORAGE_BUCKET_NAME
        kwargs['region_name']   = settings.AWS_S3_REGION_NAME
        kwargs['default_acl']   = 'public-read'
        kwargs['file_overwrite'] = False
        super().__init__(*args, **kwargs)

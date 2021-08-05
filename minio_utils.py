from minio import Minio
import os


class MinioConnect:
    def __init__(self, minio_link, access_key, secret_key):
        self.client = Minio(minio_link,
                            access_key=access_key,
                            secret_key=secret_key,
                            secure=False)

    def download(self,bucket_name, file_path, temp_path_to_save):
        response = self.client.get_object(bucket_name, file_path)
        file = open(os.path.join(temp_path_to_save,file_path.split("/")[-1]), "wb")
        file.write(response.data)
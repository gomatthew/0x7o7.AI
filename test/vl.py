import io
import logging
import os
from minio import Minio
from minio.error import S3Error
from minio.deleteobjects import DeleteObject
from sanic.log import logger
import requests
d={'bucket': 'ismartllm', 'fileName': 'office.mp4', 'detectFps': 1, 'cls': [{'id': 0, 'clsDetailList': [{'code': '1002', 'confidenceLevel': 0.5, 'label': '在岗', 'mark': 'DETECT'}]}]}
res=requests.post("http://39.100.77.186:15390/video/detect",json=d)
import json
res = json.loads(res.text)

# f=os.stat(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\test\4.机票-行程单.jpg')
# print(f.st_size)
# with open(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\test\4.机票-行程单.jpg','rb') as f:
#     print(len(f.read()))
client=Minio('39.100.77.186:15584','tjmcc','TjmcPassw0rd1',secure=False)
r=client.list_objects('ismartllm')
with open(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\test\office.mp4','rb') as f:
    c = f.read()
client.put_object('ismartllm','office.mp4',io.BytesIO(c),len(c))
data=client.get_object('ismartllm',res.get('data'))
# minio_instance.client.put_object(bucket_name, file_name, io.BytesIO(video_file.file.read()),
#                                  len(video_file.file.read()))
with open(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\test/office_.mp4','wb') as f:
    f.write(data.data)
class MinioUtils(object):
    _instance = None
    _initialized = False
    _service = None
    _access_key = None
    _secret_key = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MinioUtils, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, service=None, access_key=None, secret_key=None, secure=False):
        if not self._initialized:
            # print(f"service: {service}, access_key: {access_key}, secret_key: {secret_key}")
            # 如果参数不为None，则更新类变量
            if service is not None:
                self._service = service
            if access_key is not None:
                self._access_key = access_key
            if secret_key is not None:
                self._secret_key = secret_key

            self.client = Minio(self._service, access_key=self._access_key, secret_key=self._secret_key, secure=secure)
            self._initialized = True

    def exists_bucket(self, bucket_name):
        """
        判断桶是否存在
        :param bucket_name: 桶名称
        :return:
        """
        return self.client.bucket_exists(bucket_name=bucket_name)

    def create_bucket(self, bucket_name: str, is_policy: bool = True):
        """
        创建桶 + 赋予策略
        :param bucket_name: 桶名
        :param is_policy: 策略
        :return:
        """
        if self.exists_bucket(bucket_name=bucket_name):
            return False
        else:
            self.client.make_bucket(bucket_name=bucket_name)
        if is_policy:
            policy = self.policy % (bucket_name, bucket_name)
            self.client.set_bucket_policy(bucket_name=bucket_name, policy=policy)
        return True

    def get_bucket_list(self):
        """
        列出存储桶
        :return:
        """
        buckets = self.client.list_buckets()
        bucket_list = []
        for bucket in buckets:
            bucket_list.append(
                {"bucket_name": bucket.name, "create_time": bucket.creation_date}
            )
        return bucket_list

    def remove_bucket(self, bucket_name):
        """
        删除桶
        :param bucket_name:
        :return:
        """
        try:
            self.client.remove_bucket(bucket_name=bucket_name)
        except S3Error as e:
            logger.error("[error]:", e)
            return False
        return True

    def bucket_list_files(self, bucket_name, prefix):
        """
        列出存储桶中所有对象
        :param bucket_name: 桶名
        :param prefix: 前缀
        :return:
        """
        try:
            files_list = self.client.list_objects(bucket_name=bucket_name, prefix=prefix, recursive=True)
            for obj in files_list:
                print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
                      obj.etag, obj.size, obj.content_type)
        except S3Error as e:
            logger.error("[error]:", e)

    def download_file(self, bucket_name, file, file_path, stream=1024 * 32):
        """
        从bucket 下载文件 + 写入指定文件
        :return:
        """
        try:
            data = self.client.get_object(bucket_name, file)
            with open(file_path, "wb") as fp:
                for d in data.stream(stream):
                    fp.write(d)
        except S3Error as e:
            logger.error("[error]:", e)

    def get_file(self, bucket_name, file, file_path):
        """
        下载保存文件保存本地
        :param bucket_name:
        :param file:
        :param file_path:
        :return:
        """
        self.client.fget_object(bucket_name, file, file_path)

    def copy_file(self, bucket_name, file, file_path):
        """
        拷贝文件（最大支持5GB）
        :param bucket_name:
        :param file:
        :param file_path:
        :return:
        """
        self.client.copy_object(bucket_name, file, file_path)

    def upload_file(self, bucket_name, file, file_path, content_type=None):
        """
        上传文件 + 写入
        :param bucket_name: 桶名
        :param file: 文件名
        :param file_path: 本地文件路径
        :param content_type: 文件类型
        :return:
        """
        try:
            with open(file_path, "rb") as file_data:
                file_stat = os.stat(file_path)
                self.client.put_object(bucket_name, file, file_data, file_stat.st_size, content_type=content_type)
        except S3Error as e:
            logger.error("[error]:", e)

    def put_file(self, bucket_name, file, file_path):
        """
        上传文件
        :param bucket_name: 桶名
        :param file: 文件名
        :param file_path: 本地文件路径
        :return:
        """
        try:
            self.client.fput_object(bucket_name, file, file_path)
        except S3Error as e:
            logger.error("[error]:", e)

    def stat_object(self, bucket_name, file):
        """
        获取文件元数据
        :param bucket_name:
        :param file:
        :return:
        """
        try:
            data = self.client.stat_object(bucket_name, file)
            print(data.bucket_name)
            print(data.object_name)
            print(data.last_modified)
            print(data.etag)
            print(data.size)
            print(data.metadata)
            print(data.content_type)
        except S3Error as e:
            logger.error("[error]:", e)

    def remove_file(self, bucket_name, file):
        """
        移除单个文件
        :return:
        """
        self.client.remove_object(bucket_name, file)

    def remove_files(self, bucket_name, file_list):
        """
        删除多个文件
        :return:
        """
        delete_object_list = [DeleteObject(file) for file in file_list]
        for del_err in self.client.remove_objects(bucket_name, delete_object_list):
            logging.error("del_err: {}", del_err)

# minio_utils=MinioUtils(service='39.100.77.186:15584', access_key='tjmcc',
#            secret_key='TjmcPassw0rd1')
# res=minio_utils.upload_file('ismartllm', 'office.mp4', r'C:\Users\Supinfo\PycharmProjects\AITEST\test\office.mp4')

# minio_utils.download_file('ismartllm', 'office.mp4', r'/ai/data/llm/temp')
data = {
    "bucket": 'ismartllm',
    "fileName": 'office.mp4',
    "detectFps": 12,
    "cls": [
        {
            "id": 0,
            "clsDetailList": [
                {
                    "code": "1002",
                    "confidenceLevel": 1,
                    "label": '在岗',
                    "mark": "DETECT"
                }
            ]
        }
    ]
}
import requests
res = requests.post("http://39.100.77.186:15390/video/detect",json=data)
print(res)
import oss2

import uuid


def get_uuid():
    """
    Description:   生成uuid作为图片名，保证唯一性
    :return:       根据时间戳生成uuid
    """
    get_timestamp_uuid = uuid.uuid1()
    return get_timestamp_uuid


class OSSUtil:
    """用于阿里云OSS对象存储，上传和下载文件"""

    def __init__(self, ):
        """Constructor for OSS_Util"""
        self._auth = oss2.Auth('LTAI5tAzYAph8E2mi7qiGG28', '1hxt6mViSvbeWMd6D6rAZI3CGWGFL2')
        self._bucket = oss2.Bucket(self._auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'defect-predict')

    def put_object(self, image_path):
        """
        Description:   上传图片
        :param:
            filepath:   本地文件位置
        :return:       文件公网访问url
        """
        # self._bucket.put_object_from_file('images/test.png', '../static/images/rf_result.png')
        # https://defect-predict.oss-cn-hangzhou.aliyuncs.com/ + postfix即可公网访问
        image_name = str(get_uuid()) + ".png"
        self._bucket.put_object_from_file("images/" + image_name, image_path)
        return "https://defect-predict.oss-cn-hangzhou.aliyuncs.com/images/" + image_name


if __name__ == '__main__':
    # for i in range(5):
    #     print(get_uuid())

    _oss_util = OSSUtil()
    print(_oss_util.put_object("../static/images/rf_result.png"))

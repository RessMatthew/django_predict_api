# -*- coding: utf-8 -*-
import oss2

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
# auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
auth = oss2.Auth('LTAI5tAzYAph8E2mi7qiGG28', '1hxt6mViSvbeWMd6D6rAZI3CGWGFL2')
# Endpoint以杭州为例，其它Region请按实际情况填写。
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'defect-predict')


# 上传文件到OSS。
# <yourObjectName>由包含文件后缀，不包含Bucket名称组成的Object完整路径，例如abc/efg/123.jpg。
# <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
bucket.put_object_from_file('images/test.png', '../static/images/rf_result.png')
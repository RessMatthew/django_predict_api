## 使用virtualenv管理虚拟环境

1. 提交方
   1. 将.venv加入.gitignore
   2. 装完库后执行`pip freeze > requiremnets.txt`
2. 使用方
   1. clone项目后，pycharm检测到requiremnets.txt，会建议你创建虚拟环境，默认选择即可
   2. 执行`pip install -r requirements.txt`根据文件中库版本全部自动安装



**安装了新库提交前，记得执行pip freeze > requiremnets.txt**



# API开发

## 创建Django4.1项目

### 创建工程项目——django_predict_api

然后在工程**django_predict_api**文件下，setting.py的配置进行配置

1. 数据库迁移到RessMatthew的服务器mysql
2. 配置了中文，时区，不存储0时区时间等



### 创建app——predict_app

```python
# python manage.py startapp [app名字]
python manage.py startapp predict_app
```



### 注册app

![image-20220910102545856](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220910102545856.png)



## 简单API开发

### 在app文件夹下创建urls.py

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
 ]
```



### 将app的url绑定到工程项目下

```python
#  django_predict_api/urls.py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('predict_app.urls')), #将predict_app的url绑定到工程项目下
]
```



### 在app文件夹urls.py中添加路由与视图的函数映射

> path('api/v1/alarm/', views.get)将view.py中函数名为get()的函数，绑定路由为api/v1/alarm/

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/alarm/', views.get), #get为view.py中的函数名
]
```



### 在app文件夹views.py中实现被映射的函数

example

```python
'''GET接口'''
from django.http import JsonResponse  #接口返回的是json，需要引入的信息
def get(request):
    if request.method == "GET": #获取判断请求方式
        request_dict = request.GET  #获取接口请求发送过来的信息
        query = request_dict["query"] #获取接口请求发送过信息
        '''
        在这里可以写接口在发送请求后的一系列处理方法
        '''
        request_data = {"code":200,"message":"请求成功","test":query}
        return JsonResponse(request_data)
```



```python
'''POST接口'''
from django.http import JsonResponse  #接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt   #post接口需要引入的信息
@csrf_exempt
def post(request):
    if request.method == "GET": #获取判断请求方式
        request_dict = request.body  #获取接口请求发送过来的信息
        query = request_dict["query"] #获取接口请求发送过信息
        '''
        在这里可以写接口在发送请求后的一系列处理方法
        '''
        request_data = {"code":200,"message":"请求成功"}
        return JsonResponse(request_data)
```


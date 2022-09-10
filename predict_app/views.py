from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
# 我的理解是Controller层
def get(request):
    if request.method == "GET":  # 获取判断请求方式
        request_dict = request.GET  # 获取接口请求发送过来的信息
        query = request_dict["query"]  # 获取接口请求发送过信息
        '''
        在这里可以写接口在发送请求后的一系列处理方法
        '''
        request_data = {"code": 200, "message": "请求成功", "test": query}
        return JsonResponse(request_data)

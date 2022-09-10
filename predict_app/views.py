from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse  # 接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt  # post接口需要引入的信息
from service.random_forest import RandomForest

# Create your views here.
# 我的理解是Controller层


'''rf/training/'''


@csrf_exempt
def rf_training(request):
    """
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        # request_dict = request.POST  # 获取接口请求发送过来的信息
        # csv_file = request_dict["csv_file"]  # 获取接口请求发送过信息

        csv_file = request.FILES.get("csv_file")

        _rand_forest = RandomForest()
        _rand_forest.rf_training(csv_file)

        '''
        在这里可以写接口在发送请求后的一系列处理方法
        '''
        request_data = {
            "code": 200,
            "message": "请求成功",
        }
        return JsonResponse(request_data)

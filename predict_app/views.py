from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse  # 接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt  # post接口需要引入的信息
from service.random_forest import RandomForest
from utils.image_util import ImageUtil

# Create your views here.
# 我的理解是Controller层

_rand_forest = RandomForest()
_image_util = ImageUtil()


@csrf_exempt
def rf_training(request):
    """
    api:    rf/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/rf_result.png
        _rand_forest.rf_training(csv_file)

        base64str = _image_util.to_base64("static/images/rf_result.png")


        request_data = {
            "code": 200,
            "message": "请求成功",
            "base64str": str(base64str),
        }
        return JsonResponse(request_data)

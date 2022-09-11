from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse  # 接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt  # post接口需要引入的信息
from service.random_forest import RandomForest
from service.knn import Knn
from utils.image_util import ImageUtil
from utils.constants import CONSTANTS

# Create your views here.
# 我的理解是Controller层

_rand_forest = RandomForest()
_knn = Knn()
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

        base64str = _image_util.to_base64(CONSTANTS.RF_RESULT)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "base64str": str(base64str),
        }
        return JsonResponse(request_data)


@csrf_exempt
def rf_predict(request):
    """
    api:    rf/predict/
    Description:传来ar*.csv文件，用训练的模型来做软件缺陷预测
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/rf_predict.png
        # status_bool为训练模型是否预先生成的标识布尔值
        status_bool, accuracy = _rand_forest.rf_predict(csv_file)
        if status_bool is True:
            base64str = _image_util.to_base64(CONSTANTS.RF_PREDICT)

            request_data = {
                "code": 200,
                "message": "请求成功",
                "accuracy": accuracy,
                "base64str": str(base64str),
            }
        else:
            request_data = {
                "code": 201,
                "message": "未预先生成训练模型",
            }
        return JsonResponse(request_data)


@csrf_exempt
def knn_training(request):
    """
    api:    knn/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/knn_result.png
        _knn.knn_training(csv_file)

        base64str = _image_util.to_base64(CONSTANTS.KNN_RESULT)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "base64str": str(base64str),
        }
        return JsonResponse(request_data)

@csrf_exempt
def knn_predict(request):
    """
    api:    knn/predict/
    Description:传来ar*.csv文件，用训练的模型来做软件缺陷预测
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/rf_predict.png
        # status_bool为训练模型是否预先生成的标识布尔值
        status_bool, accuracy = _knn.knn_predict(csv_file)
        if status_bool is True:
            base64str = _image_util.to_base64(CONSTANTS.KNN_PREDICT)

            request_data = {
                "code": 200,
                "message": "请求成功",
                "accuracy": accuracy,
                "base64str": str(base64str),
            }
        else:
            request_data = {
                "code": 201,
                "message": "未预先生成训练模型",
            }
        return JsonResponse(request_data)

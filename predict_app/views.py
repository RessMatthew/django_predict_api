from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse  # 接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt  # post接口需要引入的信息

from service.dnn import Dnn
from service.ensemble import Ensemble
from service.random_forest import RandomForest
from service.knn import Knn
from service.kmeans import Kmeans
from utils.image_util import ImageUtil
from utils.constants import CONSTANTS

from rest_framework import viewsets

from .serializers import TrainingResultserializer
from .models import TrainingResult
from .models import SQLUtil


class TrainingResultViewSet(viewsets.ModelViewSet):
    queryset = TrainingResult.objects.all().order_by('id')  # 查询结果给queryset
    serializer_class = TrainingResultserializer  # 对结果进序列化


# Create your views here.
# 我的理解是Controller层

_rand_forest = RandomForest()
_knn = Knn()
_kmeans = Kmeans()
_image_util = ImageUtil()
_sql_util = SQLUtil()
_dnn = Dnn()
_ensemble = Ensemble()


@csrf_exempt
def rf_training(request):
    """
    api:    rf/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/rf_result.png
        training_result_dict = _rand_forest.rf_training(csv_file)
        # 持久化
        _sql_util.add_training_result(training_result_dict)
        # base64str = _image_util.to_base64(CONSTANTS.RF_RESULT)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_url": training_result_dict['result_url'],
        }
        return JsonResponse(request_data)


@csrf_exempt
def get_all_result(request):
    """
    api:    get-all-result/
    Description:获得目前所有训练结果
    """
    if request.method == "GET":  # 获取判断请求方式

        all_training_result = serializers.serialize("json", _sql_util.all_training_result())

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_array": all_training_result,
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

        # 预测结果图片，写入static/images/knn_result.png,同时上传oss
        training_result_dict = _knn.knn_training(csv_file)
        # 持久化
        _sql_util.add_training_result(training_result_dict)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_url": training_result_dict['result_url'],
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


@csrf_exempt
def kmeans_training(request):
    """
    api:    kmeans/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/kmeans_result.png,同时上传oss
        training_result_dict = _kmeans.kmeans_training(csv_file)
        # 持久化
        _sql_util.add_training_result(training_result_dict)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_url": training_result_dict['result_url'],
        }
        return JsonResponse(request_data)


@csrf_exempt
def kmeans_predict(request):
    """
    api:    kmeans/predict/
    Description:传来ar*.csv文件，用训练的模型来做软件缺陷预测
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/rf_predict.png
        # status_bool为训练模型是否预先生成的标识布尔值
        status_bool, accuracy = _kmeans.kmeans_predict(csv_file)
        if status_bool is True:
            base64str = _image_util.to_base64(CONSTANTS.KMEANS_PREDICT)

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
def dnn_training(request):
    """
    api:    dnn/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/knn_result.png,同时上传oss
        training_result_dict = _dnn.dnn_training(csv_file)
        # 持久化
        _sql_util.add_training_result(training_result_dict)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_url": training_result_dict['result_url'],
        }
        return JsonResponse(request_data)


@csrf_exempt
def dnn_predict(request):
    """
    api:    dnn/predict/
    Description:传来ar*.csv文件，用训练的模型来做软件缺陷预测
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/dnn.png
        # status_bool为训练模型是否预先生成的标识布尔值
        status_bool, accuracy = _dnn.dnn_predict(csv_file)
        if status_bool is True:
            base64str = _image_util.to_base64(CONSTANTS.DNN_PREDICT)

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
def ensemble_training(request):
    """
    api:    ensemble/training/
    Description:传来ar*.csv文件，训练并预测模型
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/ensemble_result.png,同时上传oss
        training_result_dict = _ensemble.ensemble_training(csv_file)
        # 持久化
        _sql_util.add_training_result(training_result_dict)

        request_data = {
            "code": 200,
            "message": "请求成功",
            "result_url": training_result_dict['result_url'],
        }
        return JsonResponse(request_data)


@csrf_exempt
def ensemble_predict(request):
    """
    api:    ensemble/predict/
    Description:传来ar*.csv文件，用训练的模型来做软件缺陷预测
    """
    if request.method == "POST":  # 获取判断请求方式

        csv_file = request.FILES.get("csv_file")

        # 预测结果图片，写入static/images/dnn.png
        # status_bool为训练模型是否预先生成的标识布尔值
        status_bool, accuracy = _ensemble.ensemble_predict(csv_file)
        if status_bool is True:
            base64str = _image_util.to_base64(CONSTANTS.ENSEMBLE_PREDICT)

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

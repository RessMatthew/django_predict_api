from django.db import models


# Create your models here.
class TrainingResult(models.Model):
    '''训练结果模型类'''
    type = models.CharField(max_length=32)  # 由哪种算法训练：rf,knn,dnn
    filename = models.CharField(max_length=64)  # 数据集名称：ar1.csv
    time = models.CharField(max_length=64)  # 结果生成时间
    auc = models.CharField(max_length=64)  # auc准确率
    macro = models.CharField(max_length=64)  # macro精确率
    macro_recall = models.CharField(max_length=64)  # macro_recall召回率
    weighted = models.CharField(max_length=64)  # F1准确率和召回率的加权调和平均
    result_url = models.CharField(max_length=128)  # roc曲线的图片公网访问url

    def __str__(self):
        return self.result_url


class SQLUtil:
    def add_training_result(self, training_result_dict):
        """
        Description:    将训练结果存储数据库
        :param:
            training_result_dict:   训练结果字典
        """
        training_result = TrainingResult()
        training_result.type = training_result_dict['type']
        training_result.filename = training_result_dict['filename']
        training_result.time = training_result_dict['time']
        training_result.auc = training_result_dict['auc']
        training_result.macro = training_result_dict['macro']
        training_result.macro_recall = training_result_dict['macro_recall']
        training_result.weighted = training_result_dict['weighted']
        training_result.result_url = training_result_dict['result_url']
        training_result.save()

    def all_training_result(self):
        """
        Description:    查询所有训练结果
        :return:        所有训练结果
        """
        return TrainingResult.objects.all()

import os
import time

import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import joblib

from service.random_forest import training_result_dict
from utils.csv_util import CSVUtil
from utils.oss_util import OSSUtil
from utils.plot_util import PlotUtil
from utils.constants import CONSTANTS

class Kmeans:
    '''用于实现k-means模型的训练和预测'''

    _csv_util = CSVUtil()
    _plot_util = PlotUtil()
    _oss_util = OSSUtil()

    def __init__(self, ):
        """Constructor for Kmeans"""

    def kmeans_training(self, csv_file):
        """
        Description:
        Parameters:
            csv_file:csv文件
        """

        ''' ---------------------------------数据处理--------------------------------------- '''
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)
        # 训练集和测试集划分
        X_train = datasets[:120]  # 第0到125个数
        y_train = labels[:120]
        X_test = datasets[90:]  # 第90到最后一个数
        y_test = labels[90:]

        ''' ----------------------------------算法核心-------------------------------------- '''
        #
        clf = KMeans(n_clusters=2)
        clf.fit(X_train, y_train)  # 使用训练集对分类器训练

        ''' ---------------------------------模型持久化-------------------------------------- '''
        joblib.dump(clf, "static/training_model/kmeans.pkl")
        y_predict = clf.predict(X_test)  # 使用分类器对测试集进行预测
        np.savetxt('static/result/kmeans_result.txt', y_predict)

        ''' --------------------------------绘制模型评价图------------------------------------ '''
        # auc准确率，所有判断中有多少判断正确的
        auc = metrics.accuracy_score(y_test, y_predict)
        # macro精确率，预测为正的样本中有多少是对
        macro = metrics.precision_score(y_test, y_predict, average='macro')
        # macro_recall召回率：有多少正样本被预测正确了
        macro_recall = metrics.recall_score(y_test, y_predict, average='macro')
        # weightedF1：准确率和召回率的加权调和平均
        weighted = metrics.f1_score(y_test, y_predict, average='weighted')

        plot = self._plot_util.plot_roc(y_test, y_predict, auc, macro, macro_recall, weighted)
        plot.savefig('static/images/kmeans_result.png')  # 将ROC图片进行保存

        result_url = self._oss_util.put_object('static/images/kmeans_result.png')  # 图片上传OSS

        '''--------------------------------转储训练结果字典-----------------------------------'''
        training_result_dict['type'] = "kmeans"
        training_result_dict['filename'] = csv_file.name
        training_result_dict['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        training_result_dict['auc'] = str(auc)
        training_result_dict['macro'] = macro
        training_result_dict['macro_recall'] = macro_recall
        training_result_dict['weighted'] = weighted
        training_result_dict['result_url'] = result_url
        return training_result_dict

    def kmeans_predict(self, csv_file):
        """
            Description:
            Parameters:
                csv_file:csv文件
            Return:
                1.训练模型已经生成
                    status_bool=Ture,accuracy数据集预测准确率
                2.训练模型没有生成
                    status_bool=False,accuracy=0
        """

        ''' ---------------------------------数据处理--------------------------------------- '''
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)
        X_test = datasets[:]

        # 判断训练模型是否已经生成
        status_bool = os.path.lexists(r'static/training_model/kmeans.pkl')
        accuracy = 0
        if status_bool is True:
            clf0 = joblib.load("static/training_model/kmeans.pkl")
            y_predict = clf0.predict(X_test)  # 使用分类器对测试集进行预测
            np.savetxt('static/result/kmeans_result.txt', y_predict)

            # 画饼图
            plot = self._plot_util.plot_pie(y_predict)
            plot.savefig('static/images/kmeans_predict.png')  # 将ROC图片进行保存

            accuracy = metrics.accuracy_score(labels, y_predict)
            # print(accuracy)
            return status_bool, accuracy
        else:
            return status_bool, accuracy


import os

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import joblib
import matplotlib as mpl

from utils.csv_util import CSVUtil
from utils.plot_util import PlotUtil
from utils.constants import CONSTANTS

class Knn:
    '''用于实现knn模型的训练和预测'''

    _csv_util = CSVUtil()
    _plot_util = PlotUtil()

    def __init__(self, ):
        """Constructor for Knn"""

    def knn_training(self, csv_file):
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
        # 选取最近的12个节点，采用曼哈顿距离，每个节点权重随距离减小
        clf = KNeighborsClassifier(n_neighbors=12,p=1,weights="distance")
        clf.fit(X_train, y_train)  # 使用训练集对分类器训练


        ''' ---------------------------------模型持久化-------------------------------------- '''
        joblib.dump(clf, "static/training_model/knn.pkl")
        y_predict = clf.predict(X_test)  # 使用分类器对测试集进行预测
        np.savetxt('static/result/knn_result.txt', y_predict)

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
        plot.savefig('static/images/knn_result.png')  # 将ROC图片进行保存

    def knn_predict(self, csv_file):
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
        status_bool = os.path.lexists(r'static/training_model/knn.pkl')
        accuracy = 0
        if status_bool is True:
            clf0 = joblib.load("static/training_model/knn.pkl")
            y_predict = clf0.predict(X_test)  # 使用分类器对测试集进行预测
            np.savetxt('static/result/knn_result.txt', y_predict)

            #画饼图
            plot = self._plot_util.plot_pie(y_predict)
            plot.savefig('static/images/knn_predict.png')  # 将ROC图片进行保存

            accuracy = metrics.accuracy_score(labels, y_predict)
            # print(accuracy)
            return status_bool, accuracy
        else:
            return status_bool, accuracy


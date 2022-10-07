"""用随机森林模型得到数据集预测结果"""
# -*- coding: utf-8 -*-

from sklearn import metrics
from mdp_random import data_handle, plot_roc
import joblib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter




def test_random(file_path):
    """
    函数说明：用随机森林模型得到数据集预测结果
    Parameters:
         file_path:数据集路径
    """
    datasets, labels = data_handle(file_path)  # 对数据集进行处理
    X_test = datasets[:]
    clf0 = joblib.load("../static/training_model/ensemble.pkl")
    y_predict = clf0.predict(X_test)  # 使用分类器对测试集进行预测
    np.savetxt('../static/result/ensemble_result.txt', y_predict)
    print(y_predict)
    return y_predict


def plot_pie(y_predict):
    """
    函数说明：绘制画饼状图
    Parameters:
         y_predict:预测结果array
    """
    Counter(y_predict)  # {label:sum(label)}
    Yes = sum(y_predict == 1)
    No = sum(y_predict == 0)
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
    label = ['有缺陷数', '无缺陷数']  # 定义饼图的标签，标签是列表
    explode = [0.01, 0.05]  # 设定各项距离圆心n个半径
    values = [Yes, No]
    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
    plt.title('缺陷数目')
    plt.show()


def get_auc(y_test, y_predict):
    """
    Description:获得预测准确率
    Parameters:
        y_test:真实结果array
        y_predict:预测结果array
    """
    auc = metrics.accuracy_score(y_test, y_predict)
    return auc

def random_predict(file_path):
    """
    Description:预测数据集，输出准确率，并绘制饼状图
    Parameters:
        file_path:数据集路径
    """
    y_predict = test_random(file_path)
    datasets, labels = data_handle(file_path)
    auc = get_auc(np.array(labels), y_predict)
    print("准确率:" + str(auc))
    plot_pie(y_predict)



if __name__ == '__main__':
    random_predict('../static/dataset/SOFTLAB/PC3.csv')


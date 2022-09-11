import joblib
import os
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

from utils.csv_util import CSVUtil
from utils.plot_util import PlotUtil
from utils.constants import CONSTANTS
from utils.oss_util import OSSUtil
import time

training_result_dict = {
    'type': '',
    'filename': '',
    'time': '',
    'auc': '',
    'macro': '',
    'macro_recall': '',
    'weighted': '',
    'result_url': '',
}


class RandomForest:
    """用于实现随机森林模型的训练和预测"""

    _csv_util = CSVUtil()
    _plot_util = PlotUtil()
    _oss_util = OSSUtil()

    def __init__(self, ):
        """Constructor for RandomForest"""

    def rf_training(self, csv_file):
        """
        Description:
        Parameters:
            csv_file:csv文件
        :return:
            training_result_dict:训练结果字典
        """
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)

        """....................................算法核心start...................................."""
        # 训练集和测试集划分
        X_train = datasets[:115]  # 第0到115个数
        y_train = labels[:115]
        X_test = datasets[70:]  # 第70到最后一个数
        y_test = labels[70:]
        # 随机森林分类器
        clf = RandomForestClassifier()
        # n_estimators两百棵决策树,random_state控制随机状态使得结果复现
        clf = RandomForestClassifier(n_estimators=200, random_state=0)
        clf.fit(X_train, y_train)  # 使用训练集对分类器训练
        """.....................................算法核心end....................................."""

        joblib.dump(clf, "static/training_model/random.pkl")
        y_predict = clf.predict(X_test)  # 使用分类器对测试集进行预测
        np.savetxt('static/result/random_result.txt', y_predict)

        # auc准确率，所有判断中有多少判断正确的
        auc = metrics.accuracy_score(y_test, y_predict)
        # macro精确率，预测为正的样本中有多少是对
        macro = metrics.precision_score(y_test, y_predict, average='macro')
        # macro_recall召回率：有多少正样本被预测正确了
        macro_recall = metrics.recall_score(y_test, y_predict, average='macro')
        # weightedF1：准确率和召回率的加权调和平均
        weighted = metrics.f1_score(y_test, y_predict, average='weighted')

        plot = self._plot_util.plot_roc(y_test, y_predict, auc, macro, macro_recall, weighted)
        plot.savefig('static/images/rf_result.png')  # 将ROC图片进行保存

        result_url = self._oss_util.put_object('static/images/rf_result.png')  # 图片上传OSS
        """.....................................转储训练结果字典....................................."""
        training_result_dict['type'] = "rf"
        training_result_dict['filename'] = csv_file.name
        training_result_dict['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        training_result_dict['auc'] = str(auc)
        training_result_dict['macro'] = macro
        training_result_dict['macro_recall'] = macro_recall
        training_result_dict['weighted'] = weighted
        training_result_dict['result_url'] = result_url
        return training_result_dict

    def rf_predict(self, csv_file):
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
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)
        X_test = datasets[:]

        # 判断训练模型是否已经生成
        status_bool = os.path.lexists(r'static/training_model/random.pkl')
        accuracy = 0
        if status_bool is True:
            clf0 = joblib.load("static/training_model/random.pkl")
            y_predict = clf0.predict(X_test)  # 使用分类器对测试集进行预测
            np.savetxt('static/result/random_result.txt', y_predict)

            plot = self._plot_util.plot_pie(y_predict)
            plot.savefig('static/images/rf_predict.png')  # 将ROC图片进行保存

            accuracy = metrics.accuracy_score(labels, y_predict)
            # print(accuracy)
            return status_bool, accuracy
        else:
            return status_bool, accuracy

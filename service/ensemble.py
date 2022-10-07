import os
import time

import joblib
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.neural_network import MLPClassifier
from utils.csv_util import CSVUtil
from utils.oss_util import OSSUtil
from utils.plot_util import PlotUtil
from utils.constants import CONSTANTS

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


class Ensemble:
    _csv_util = CSVUtil()
    _plot_util = PlotUtil()
    _oss_util = OSSUtil()

    def __init__(self, ):
        """Constructor for Ensemble"""

    def ensemble_training(self, csv_file):
        """
        Description:
        Parameters:
            csv_file:csv文件
        """

        ''' ---------------------------------数据处理--------------------------------------- '''
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)
        # 训练集和测试集划分
        # 训练集和测试集划分
        X_train = datasets[:800]  # 第0到700个数
        y_train = labels[:800]
        X_test = datasets[700:]  # 第700到最后一个数
        y_test = labels[700:]

        ''' ----------------------------------算法核心-------------------------------------- '''

        ##这个后续我还需要继续调参
        clf1 = MLPClassifier(hidden_layer_sizes=(200), activation='tanh', solver='adam', alpha=0,
                             batch_size=5, learning_rate='constant', learning_rate_init=0.01, power_t=0.5,
                             max_iter=1000,
                             shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9,
                             nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9,
                             beta_2=0.999, epsilon=1e-08, n_iter_no_change=10)
        clf2 = RandomForestClassifier(n_estimators=200, random_state=0)
        clf3 = KNeighborsClassifier(n_neighbors=12, p=1, weights="distance")
        # 将上面三个基模型集成
        eclf = VotingClassifier(
            estimators=[('dnn', clf1), ('rf', clf2), ('knn', clf3)],
            voting='hard')
        eclf.fit(X_train, y_train)

        ''' ---------------------------------模型持久化-------------------------------------- '''
        joblib.dump(eclf, "static/training_model/ensemble.pkl")
        y_predict = eclf.predict(X_test)
        np.savetxt('static/result/ensemble_result.txt', y_predict)

        ''' --------------------------------绘制模型评价图------------------------------------ '''

        auc = metrics.accuracy_score(y_test, y_predict)
        macro = metrics.precision_score(y_test, y_predict, average='macro')
        macro_recall = metrics.recall_score(y_test, y_predict, average='macro')
        weighted = metrics.f1_score(y_test, y_predict, average='weighted')

        plot = self._plot_util.plot_roc(y_test, y_predict, auc, macro, macro_recall, weighted, "Ensemble-ROC")
        plot.savefig('static/images/ensemble_result.png')  # 将ROC图片进行保存

        result_url = self._oss_util.put_object('static/images/ensemble_result.png')  # 图片上传OSS

        '''--------------------------------转储训练结果字典-----------------------------------'''
        training_result_dict['type'] = "ensemble"
        training_result_dict['filename'] = csv_file.name
        training_result_dict['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        training_result_dict['auc'] = str(auc)
        training_result_dict['macro'] = macro
        training_result_dict['macro_recall'] = macro_recall
        training_result_dict['weighted'] = weighted
        training_result_dict['result_url'] = result_url
        return training_result_dict

    def ensemble_predict(self, csv_file):
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
        status_bool = os.path.lexists(r'static/training_model/ensemble.pkl')
        accuracy = 0
        if status_bool is True:
            clf0 = joblib.load("static/training_model/ensemble.pkl")
            y_predict = clf0.predict(X_test)  # 使用分类器对测试集进行预测
            np.savetxt('static/result/ensemble_result.txt', y_predict)

            # 画饼图
            plot = self._plot_util.plot_pie(y_predict)
            plot.savefig('static/images/ensemble_predict.png')  # 将ROC图片进行保存

            accuracy = metrics.accuracy_score(labels, y_predict)
            # print(accuracy)
            return status_bool, accuracy
        else:
            return status_bool, accuracy

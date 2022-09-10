import joblib
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

from utils.csv_util import CSVUtil
from utils.plot_util import PlotUtil
from utils.constants import CONSTANTS


class RandomForest:
    """用于实现随机森林模型的训练和预测"""

    _csv_util = CSVUtil()
    _plot_util = PlotUtil()

    def __init__(self, ):
        """Constructor for RandomForest"""

    def rf_training(self, csv_file):
        """
        Description:
        Parameters:
            csv_file:csv文件
            arg2:
        """
        datasets, labels = self._csv_util.data_handle(csv_file, CONSTANTS.ARCSVLABEL)

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
        # joblib.dump(clf, "../static/training_model/random.pkl")

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

        self._plot_util.plot_roc(y_test, y_predict, auc, macro, macro_recall, weighted)


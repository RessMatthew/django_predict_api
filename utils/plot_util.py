from matplotlib import pyplot as plt
from sklearn import metrics
import matplotlib as mpl


class PlotUtil:
    """用于绘制图像"""

    def __init__(self, ):
        """Constructor for PlotUtil"""

    def plot_roc(self, test_list, predict_list, auc, macro, macro_recall, weighted):
        """
        Description:        绘制ROC曲线
        Parameters:
            test_list:      测试集标签列表
            predict_list:   预测结果集标签列表
            auc:            预测准确率输出
            macro:          预测宏平均精确率输出
            macro_recall:   预测宏平均召回率输出：召回率
            weighted:       预测平均f1-score输出：F1
        """
        # 创建一个1行2列的画布
        figure, axes = plt.subplots(ncols=1, nrows=2, figsize=(6.5, 6.5), dpi=100)
        # 绘图对象
        ax1 = axes[0]
        ax2 = axes[1]
        # 选择ax1
        plt.sca(ax1)
        false_positive_rate, true_positive_rate, thresholds = metrics.roc_curve(test_list, predict_list)  # 真阳性，假阳性，阈值
        roc_auc = metrics.auc(false_positive_rate, true_positive_rate)  # 计算AUC值，ROC曲线下的面积
        print('AUC=' + str(roc_auc))
        plt.title('AR1-ROC')
        plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC = %0.4f' % roc_auc)
        plt.legend(loc='lower right')
        plt.plot([0, 1], [0, 1], 'r--')
        plt.ylabel('TPR（真阳性率）')  # 正确的肯定，正的预测为正
        plt.xlabel('FPR（伪阳性率）')  # 错误的肯定，负的预测为正

        # 选择ax2
        plt.sca(ax2)
        plt.axis('off')
        plt.title('模型评价指标', y=-0.1)
        # 解决中文乱码和正负号问题
        mpl.rcParams["font.sans-serif"] = ["SimHei"]
        mpl.rcParams["axes.unicode_minus"] = False
        col_labels = ['准确率', '精确率', '召回率', 'f1值']
        row_labels = ['期望', '实际']
        table_vals = [[0.9, 0.8, 0.75, 0.8], [auc, macro, macro_recall, weighted]]
        row_colors = ['red', 'pink', 'green', 'gold']
        table = plt.table(cellText=table_vals, colWidths=[0.18 for x in col_labels],
                          rowLabels=row_labels, colLabels=col_labels,
                          rowColours=row_colors, colColours=row_colors,
                          loc="center")
        table.set_fontsize(14)
        table.scale(1.5, 1.5)
        plt.show()
        # plt.savefig('figures/PC5.png') #将ROC图片进行保存

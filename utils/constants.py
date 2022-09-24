class CONSTANTS:
    """常量类"""

    #  数据集文件路径,这种路径仅用于测试方法，api不能用
    AR1CSV = "../static/dataset/SOFTLAB/ar1.csv"
    AR3CSV = "../static/dataset/SOFTLAB/ar3.csv"
    AR4CSV = "../static/dataset/SOFTLAB/ar4.csv"
    AR5CSV = "../static/dataset/SOFTLAB/ar5.csv"
    AR6CSV = "../static/dataset/SOFTLAB/ar6.csv"

    #  数据集的最后一行标签名：软件缺陷标识
    # ARCSVLABEL = "b'clean'"
    ARCSVLABEL = 'Y'

    # 模型评价和数据集预测图片路径
    RF_RESULT = "static/images/rf_result.png"
    RF_PREDICT = "static/images/rf_predict.png"
    KNN_RESULT = "static/images/knn_result.png"
    KNN_PREDICT = "static/images/knn_predict.png"
    KMEANS_RESULT = "static/images/kmeans_result.png"
    KMEANS_PREDICT = "static/images/kmeans_predict.png"

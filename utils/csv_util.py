import pandas as pd

from utils.constants import CONSTANTS


class CSVUtil:
    """处理csv文件的工具类"""

    def __init__(self):
        """Constructor for csv_util"""

    def data_handle(self, filepath, last_label):
        """
        Description:将csv数据集，读取为数据集特征列表和数据标签列表
        Parameters:
            filename：csv数据集路径
            last_label：csv数据集最后一列表示软件没有缺陷的符号
        Returns:
             list_datasets：数据集特征列表
             category_labels:数据标签列表
        """
        read_data = pd.read_csv(filepath)
        list_datasets = []
        category_labels = []
        for i in range(len(read_data)):
            list_data = []
            for j in range(len(read_data.iloc[i, :]) - 1):
                row_data = read_data.iloc[i, j]  # 读取每个样本的每个数据i以他人为主
                list_data.append(row_data)  # 将每个数据存入列表
            list_datasets.append(list_data)  # 将每个样本的数据存入列表

            row_data_label = read_data.iloc[i, len(read_data.iloc[i, :]) - 1]  # 读取每个样本的类别标签
            if row_data_label == last_label:
                category_labels.append(0)  # 将二分类标签转化为0和1,0代表软件正常，1代表软件缺陷
            else:
                category_labels.append(1)
        return list_datasets, category_labels


if __name__ == '__main__':
    _csv_util = CSVUtil()
    list_datasets, category_labels = _csv_util.data_handle(CONSTANTS.AR1CSV, CONSTANTS.ARCSVLABEL)
    print(list_datasets)

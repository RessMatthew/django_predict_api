import os


def is_exist_file(self, filepath):
    """
    Description:用于测试判断文件是否存在
    :param:
        filepath:文件路径
    :return:
    """
    try:
        return (1)
    except Exception as e:
        print(e)


status_bool = os.path.lexists(r'../static/training_model/random.pkl')
print(status_bool)

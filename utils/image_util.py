import base64


class ImageUtil:
    """用于图片文件的转码处理"""

    def __init__(self, ):
        """Constructor for ImageUtil"""

    def to_base64(self, image_path):
        """
        Description:将图片文件转为base64字符串
        :param:
            image_path:文件路径
        :return:base64编码字符串
        """
        with open(image_path, 'rb') as f:
            image_data = f.read()
            base64_data = base64.b64encode(image_data)  # base64编码
        return base64_data.decode('utf-8')

    def to_png(self, base64_data, image_path):
        """
        Description:将图片文件转为base64字符串
        :param:
            image_path:文件路径
        :return:
        """
        with open(image_path, 'wb') as f:
            png = base64.b64decode(base64_data)  # 解码
            f.write(png)  # 将解码得到的数据写入到图片中


if __name__ == '__main__':
    _image_util = ImageUtil()
    base64 = _image_util.to_base64("../static/images/rf_result.png")
    # a = "5416165849"
    # print(a[2:-2])

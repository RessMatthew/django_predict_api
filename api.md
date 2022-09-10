## 预先需知

接口基于SOFTLAB数据集

![image-20220910155124676](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220910155124676.png)



预览base64编码字符串的一种方式

* 前面加上`data:image/jpeg;base64,`可在浏览器解析

data:image/jpeg;base64,**[base64编码]**



# 接口

### 1. 获取数据集用随机森林算法训练模型得到的测试结果图

#### Request

- Method: **POST**
- URL: `rf/training/`
- Parameters:

```json
csv_file (类型为文件File)
```



#### Response

- success         

base64str为图片的base64编码字符串

```json
{
    "code": 200,
    "message": "请求成功",
    "base64str":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEB......",
}
```



![image-20220910155442407](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220910155442407.png)

### 2. 获取数据集用k-最近邻算法训练模型得到的测试结果图

#### Request

- Method: **POST**
- URL: `knn/training/`
- Parameters:

```json
csv_file (类型为文件File)
```



#### Response

- success         

base64str为图片的base64编码字符串

```json
{
    "code": 200,
    "message": "请求成功",
    "base64str": "iVBORw0KGgoAAAANSUhEUgAAAooAAAOXRFWHRTb2Z0...."
}
```



![Snipaste_2022-09-10_21-27-31](https://aliyun-oss-image.oss-cn-shenzhen.aliyuncs.com/img/202209102128764.png)




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

result_url为图片公网可访问url

```json
{
    "code": 200,
    "message": "请求成功",
    "result_url": "https://defect-predict.oss-cn-hangzhou.aliyuncs.com/images/cc6905d8-31ad-11ed-a318-acde48001122.png"
}
```



![image-20220911164614717](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220911164614717.png)



### 2. 获取用随机森林预测数据集的饼状图

#### Request

- Method: **POST**
- URL: `rf/predict/`
- Parameters:

```json
csv_file (类型为文件File)
```



#### Response

- success  **已生成训练模型**        

base64str为图片的base64编码字符串

```json
{
    "code": 200,
    "message": "请求成功",
    "accuracy": 0.9256198347107438,
    "base64str":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEB......",
}
```

![image-20220910213001182](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220910213001182.png)

- failure  **未生成训练模型**        

base64str为图片的base64编码字符串

```json
{
    "code": 201,
    "message": "未预先生成训练模型"
}
```



![image-20220910212937711](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220910212937711.png)

### 3. 获取数据集用k-最近邻算法训练模型得到的测试结果图

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



### 4. 获取当前数据库中已有训练记录

#### Request

- Method: **GET**
- URL: `get-all-result/`
- Parameters:

```json
无
```



#### Response

- success         

```json
{
    "code": 200,
    "message": "请求成功",
    "result_array": "[{\"model\": \"predict_app.trainingresult\", \"pk\": 1, \"fields\": {\"type\": \"test\", \"filename\": \"test\", \"time\": \"test\", \"auc\": \"test\", \"macro\": \"test\", \"macro_recall\": \"test\", \"weighted\": \"result_url\", \"result_url\": \"\"}}, {\"model\": \"predict_app.trainingresult\", \"pk\": 2, \"fields\": {\"type\": \"test\", \"filename\": \"test\", \"time\": \"test\", \"auc\": \"test\", \"macro\": \"test\", \"macro_recall\": \"test\", \"weighted\": \"test\", \"result_url\": \"test\"}}, {\"model\": \"predict_app.trainingresult\", \"pk\": 3, \"fields\": {\"type\": \"rf\", \"filename\": \"ar1.csv\", \"time\": \"2022-09-11 16:43:24\", \"auc\": \"0.9607843137254902\", \"macro\": \"0.8229166666666666\", \"macro_recall\": \"0.8229166666666666\", \"weighted\": \"0.9607843137254902\", \"result_url\": \"https://defect-predict.oss-cn-hangzhou.aliyuncs.com/images/cc6905d8-31ad-11ed-a318-acde48001122.png\"}}]"
}
```

![](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220911171050488.png)

![image-20220911171111158](https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220911171111158.png)


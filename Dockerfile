# 建立 python3.9 环境
FROM python:3.9

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf

# 设置容器内工作目录
RUN mkdir -p /var/www/html/dpapi
# 将当前目录文件加入到容器工作目录中（. 表示当前宿主机目录）
ADD . /var/www/html/dpapi
# 设置容器内工作目录
WORKDIR /var/www/html/dpapi

# 利用 pip 安装依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000
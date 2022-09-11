# Docker部署

1. 安装Docker

2. 创建镜像

   `docker build -t aier233/django-predict-api .` 

   >  *requirements600多兆，容器内部换了源，但是网卡的原因网速慢，可能需要近十分钟* 

    `docker push aier233/django-predict-api:latest`  push至仓库

    `docker tag oldname:latest newname:latest` 镜像改名

3. 创建容器

    `docker run -d -p 8000:8000 aier233/django-predict-api:latest` 

4. 查看：

     `docker images` 

     `docker ps`  

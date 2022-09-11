#关闭正在运行的进程
PID=$(ps -ef | grep "python manage.py runserver" | grep -v grep | awk '{ print $2 }')
if [ -z "$PID" ]
then
    echo '目前django不在运行中'
else
    echo '关闭django服务'
    kill $PID
fi

echo 'pip换源'
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ > /dev/null

echo '安装虚拟环境'
pip install virtualenv > /dev/null

echo '创建运行环境'
virtualenv venv > /dev/null

echo '激活虚拟环境'
source venv/bin/activate > /dev/null

echo '安装库文件'
pip install -r requirements.txt > /dev/null

echo '运行项目'
nohup python manage.py runserver 0.0.0.0:8000 > log.out 2> error.out &
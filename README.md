# djangoBlog,一个个人博客
### 安装所需要的环境
`pip install -r requirements.txt`

### 创建数据库
`CREATE DATABASE website DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`

### 创建迁移文件，生成数据表结构，运行服务器
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# 部署，修改setting.py中的DEBUG=FALSE,并搜集静态文件
python manage.py collectstatic
```

### 安装uwsgi,并设置相关配置到djangoBlog.ini文件中,安装时不要安装到python的虚拟环境中了
`pip install uwsgi`

### 执行命令行uwsgi
`uwsgi --ini djangoBlog.ini`

### 安装 nginx
`apt install nginx`

### 安装 celery
`pip install celery`
windows安装celery,如果celery==3.1.24+
那么就需要安装下面的四个包
eventlet,monotonic, greenlet, six, dnspython
执行命令`pip install eventlet`,后面的包是依赖包,会自动安装
如果是`MAC`和`Linux`请忽视

### 创建配置文件djangoBlog.conf到 /etc/nginx/conf.d/目录下

### 安装supervisor守护进程
[安装supervisor守护进程](http://www.supervisord.org/){target=_blank}
### 防止uwsgi发生意外挂掉，自动重启
### 创建配置文件djangoBlog.conf到 /etc/nginx/conf.d/目录下
### 安装supervisor守护uwsgi进程，防止uwsgi发生意外挂掉，自动重启
`pip install supervisor`

### 使用supervisord -c supervisor.conf命令来运行
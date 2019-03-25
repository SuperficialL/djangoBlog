# djangoBlog

## 安装所需要的包
```django
pip install -r requirements.txt
```
## 创建数据库
`CREATE DATABASE `website` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`

## 创建迁移文件，生成数据表结构，运行服务器
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```  

## 部署，修改setting.py中的DEBUG=FALSE,并搜集静态文件
`python manage.py collectstatic`

## 安装uwsgi,并设置相关配置到`djangoBlog.ini`文件中,安装时不要安装到python的虚拟环境中了
`pip install uwsgi`

## 执行命令行uwsgi
`uwsgi --ini djangoBlog.ini`

## 安装 nginx
`apt install nginx`
## 创建配置文件djangoBlog.conf到 `/etc/nginx/conf.d/`目录下
 
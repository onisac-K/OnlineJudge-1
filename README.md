# Online Judge
An Online Judge based on Django, Django-Rest-Framework, AngularJS and Docker.

## 初始化
```bash
# 项目目录
mkdir OnlineJudge
cd OnlineJudge

# 使用Python3.5
virtualenv env --no-site-packages --python=python3.5
source env/bin/activate

# 安装相关的包
pip install django
pip install djangorestframework

# 在当前目录`.`创建django项目
django-admin startproject OnlineJudge .
```

### 基本设置
```python
# In `/OnlineJudge/settings.py`
# 语言
LANGUAGE_CODE = 'zh-hans'

# 时区
TIME_ZONE = 'Asia/Shanghai'

# 安装应用
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

### 测试运行
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 创建管理员
```bash
python manage.py createsuperuser
# Username     : root
# Email Address: -
# Password     : shuojroot
```

## 个人博客项目  [myblog:https://www.yyhblog.com](https://www.yyhblog.com)
### 1.项目说明
> 开发环境：django2.2.3+Python3.6.9+Elasticsearh+Docker+Ngnix
> 代码管理工具：git&github
> 环境管理工具：virtualenv&pipenv
---
### 2.项目功能说明
* 支持文字类文章的发布,分享,评论
* 支持markdown文本的编辑及显示
* 支持基于IK分词查询
---
### 3.线下部署
可以使用 Virtualenv、Pipenv、Docker 等在本地运行项目，每种方式都只需运行简单的几条命令就可以了。

> 注意：

> 因为博客全文搜索功能依赖 Elasticsearch 服务，如果使用 Virtualenv 或者 Pipenv 启动项目而不想搭建 Elasticsearch 服务的话，请先设置环境变量 ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no 以关闭实时索引，否则无法创建博客文章。如果关闭实时索引，全文搜索功能将不可用。

> Windows 设置环境变量的方式：set ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no

> Linux 或者 macOS：export ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no

> 使用 Docker 启动则无需设置，因为会自动启动一个包含 Elasticsearch 服务的 Docker 容器。

无论采用何种方式，先克隆代码到本地：
```python
$ git clone 代码地址
Virtualenv
```
#### 1.创建虚拟环境并激活虚拟环境，具体方法可参考：开始进入 django 开发之旅：使用虚拟环境

#### 2.安装项目依赖
```python
$ cd myblog
$ pip install -r requirements.txt
```
#### 3.迁移数据库
```python
$ python manage.py migrate
```
#### 4.创建后台管理员账户
```python
$ python manage.py createsuperuser
```
具体请参阅 创作后台开启，请开始你的表演。

#### 5.运行开发服务器
```python
$ python manage.py runserver
```
#### 6.浏览器访问 http://127.0.0.1:8000/admin_，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：创作后台开启，请开始你的表演。

或者执行 fake 脚本批量生成测试数据：
```python
$ python -m scripts.fake
```
> 批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

#### 7.浏览器访问：http://127.0.0.1:8000，可进入到博客首页
---
**Pipenv**
#### 1.安装 Pipenv（已安装可跳过）
```python
$ pip install pipenv
```
#### 2.安装项目依赖
```python
$ cd myblog
$ pipenv install --dev
```
#### 2.关于如何使用 Pipenv，参阅：开始进入 django 开发之旅 的 Pipenv 创建和管理虚拟环境部分。

#### 3.迁移数据库

#### 在项目根目录运行如下命令迁移数据库：
```python
$ pipenv run python manage.py migrate
```
#### 4.创建后台管理员账户

#### 在项目根目录运行如下命令创建后台管理员账户
```python
$ pipenv run python manage.py createsuperuser
```
#### 5.运行开发服务器

#### 在项目根目录运行如下命令开启开发服务器：
```python
$ pipenv run python manage.py runserver
```
#### 6.浏览器访问 http://127.0.0.1:8000/admin，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：创作后台开启，请开始你的表演。

或者执行 fake 脚本批量生成测试数据：
```python
$ pipenv run python -m scripts.fake
```
批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

#### 7.在浏览器访问：http://127.0.0.1:8000/，可进入到博客首页。

### 4.线上部署

#### 1.安装docker服务,具体安装过程请参照相关说明,安装supervisor进程监控组件
    > 说明：项目中django没有利用容器部署技术,原因是窗口中安装mysqlclient会报错
    > nginx和elasticsearch利用容器技术部署
    
#### 2.从github上面拉取全部项目代码到服务器指定目录

```python
git pull
pipenv install  #安装需要的软件

```
#### 3.执行数据据操作
```python

pipenv run python manage.py makemigrations;
pipenv run python migrate;
```
#### 4.启动django服务
    > 确保gunicorn启动服务的ip为0.0.0.0:8000
    > supervisor的配置项关于添加DJANGO_SECRET_ROOT环境变量
```python
supervisord -c ~/etc/supervisord.conf
supervisorctl -c ~/etc/supervisord.onf
```
    > 检查gunicorn是否启动成功,ps aux|grep gunicorn

#### 5.启动nignx

```python
docker-compose -f nginx.yml build
docker-compose -f nginx.yml up

```
    > 注意：nginx配置文件夹conf.d里面的myblog1.conf,转发的ip为服务器容器的主IP,本服务器为172.18.0.1:8000
    
#### 6.启动Elasticsearch
```python
docker-compose -f elasticsearch.yml build
docker-compose -f elasticsearch.yml up 
```

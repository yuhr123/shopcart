# Flask 脚手架

这东西的目的是开箱即用，免得每次都要重新查官方手册配置环境。

* 将主程序文件、路由、模型做了分离
* ORM 使用 Flask-SQLAlchemy

## 使用方法

开始前先拉取并进入项目目录

**创建虚拟环境**
```shell
$ python3 -m venv .
```

**安装包**
```shell
(shopcart) $ pip install -e .
```

**设置环境变量**
```shell
(shopcart) $ export FLASK_APP=shopcart
(shopcart) $ export FLASK_DEBUG=true
```

**启动程序**
```shell
(shopcart) $ flask run
```
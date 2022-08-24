## Flask

> 2022.8.24
>
> Python Web服务框架，实践代码：[Huyueeer](https://github.com/Huyueeer)/**[flask-tutorial](https://github.com/Huyueeer/flask-tutorial)**

使用Flask构建Python服务，这是一个非常好的案例【1】

### 开发步骤

- 构建python虚拟环境

  ```shell
  python3 -m venv venv
  ```

- 激活虚拟环境

  ```shell
   . venv/bin/activate
  ```

- 安装Flask

  ```shell
  pip install Flask
  ```

- 运行应用

  ```shell
  export FLASK_APP=flaskr
  export FLASK_ENV=development
  flask run
  ```

### 使用定时方法包 flask_apscheduler 

- 安装引用flask_apscheduler

- 需要注意的是，所有的定时方法或者包都需要在`scheduler.start()`之前进行声明；

### 参考链接

1. [博客案例](https://dormousehole.readthedocs.io/en/latest/tutorial/index.html)
2. [Flask APScheduler Docs](https://viniciuschiele.github.io/flask-apscheduler/index.html)
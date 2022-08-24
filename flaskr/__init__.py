import os

from flask import Flask

def create_app(test_config=None):
    # 创建Flask实例
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 数据库初始化
    from . import db
    db.init_app(app)

    # 认证模块
    from . import auth
    app.register_blueprint(auth.bp)

    # 博客模块
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # 简单的路由
    @app.route('/hello')
    def hello():
        return 'Hello'

    return app
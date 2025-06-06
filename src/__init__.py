# -*- coding: utf-8 -*-
"""
    Python 源代码
    @Time : 2025/04/22 10:44
    @Author : 李子
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal

# 初始化扩展（注意：此时尚未绑定app）
db = SQLAlchemy()
login_manager = LoginManager()
principal = Principal()


def create_app():
    """应用工厂函数"""
    from flask import Flask
    app = Flask(__name__)

    # 加载配置
    from .config import Config
    app.config.from_object(Config)

    # 绑定扩展到app
    db.init_app(app)
    login_manager.init_app(app)
    principal.init_app(app)

    # 显式导入所有模型（确保SQLAlchemy识别表结构）
    from .models import (
        User,
        Role,
        UserRole,
        Dataset,
        AudioFile,
        Annotation,
        Attribute,
        AttributeAggregation,
        Task
    )

    # 注册蓝图（假设路由组织在routes模块中）

    # 配置登录管理器（登录视图和回调）

    # 添加上下文处理器

    # 初始化数据库（首次运行时自动创建表）
    with app.app_context():
        db.create_all()
        # 可以在此添加初始数据
        # if not User.query.first():
        #     admin = User(username='admin', email='admin@example.com')
        #     admin.set_password('admin')
        #     db.session.add(admin)
        #     db.session.commit()






    return app

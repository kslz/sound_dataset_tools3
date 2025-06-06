# -*- coding: utf-8 -*-
"""
    配置文件（Flask，数据库等）
    @Time : 2025/04/22 10:48
    @Author : 李子
"""

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                          '../db_file/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'sqla+sqlite:///celery.db'

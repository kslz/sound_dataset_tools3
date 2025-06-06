# -*- coding: utf-8 -*-
"""
    Flask应用程序入口点
    @Time : 2025/04/22 10:44
    @Author : 李子
"""
from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

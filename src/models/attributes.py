# -*- coding: utf-8 -*-
"""
    属性管理表
    定义标注信息的属性，包括属性的键、名称、数据类型等。
    @Time : 2025/04/22 10:50
    @Author : 李子
"""
from src import db
from datetime import datetime


class Attribute(db.Model):
    __tablename__ = 'attributes'

    attribute_id = db.Column(db.Integer, primary_key=True)
    attribute_key = db.Column(db.String(255), nullable=False, unique=True)
    attribute_name = db.Column(db.String(255), nullable=False)
    attribute_description = db.Column(db.Text)
    attribute_data_type = db.Column(db.String(50), nullable=False)
    attribute_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    attribute_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Attribute {self.attribute_key}>'

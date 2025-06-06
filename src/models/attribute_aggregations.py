# -*- coding: utf-8 -*-
"""
    聚合属性表
    记录聚合属性的定义，包括聚合属性的名称、结果字段、源属性以及聚合的优先级规则。
    @Time : 2025/04/22 11:16
    @Author : 李子
"""
from src import db
from datetime import datetime


class AttributeAggregation(db.Model):
    __tablename__ = 'attribute_aggregations'

    aggregation_id = db.Column(db.Integer, primary_key=True)
    aggregation_name = db.Column(db.String(255), nullable=False)
    aggregation_key = db.Column(db.String(255), nullable=False)
    aggregation_priority = db.Column(db.JSON, nullable=False)
    aggregation_logic = db.Column(db.Text)
    aggregation_data_type = db.Column(db.String(50), nullable=False)
    aggregation_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    aggregation_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<AttributeAggregation {self.aggregation_key}>'

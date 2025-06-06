# -*- coding: utf-8 -*-
"""
    数据集表
    记录音频数据集的基本信息。
    @Time : 2025/04/22 10:49
    @Author : 李子
"""
from src import db
from datetime import datetime


class Dataset(db.Model):
    __tablename__ = 'datasets'

    dataset_id = db.Column(db.Integer, primary_key=True)
    dataset_name = db.Column(db.String(255), nullable=False)
    dataset_description = db.Column(db.Text)
    dataset_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    dataset_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系定义
    audio_files = db.relationship('AudioFile', backref='dataset', lazy=True)

    def __repr__(self):
        return f'<Dataset {self.dataset_name}>'

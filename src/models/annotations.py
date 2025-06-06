# -*- coding: utf-8 -*-
"""
    标注信息表
    存储每个音频文件的标注信息，可以灵活扩展字段。
    @Time : 2025/04/22 10:49
    @Author : 李子
"""
from src import db
from datetime import datetime


class Annotation(db.Model):
    __tablename__ = 'annotations'

    annotation_id = db.Column(db.Integer, primary_key=True)
    audio_file_id = db.Column(db.Integer, db.ForeignKey('audio_files.audio_file_id'), nullable=False)
    annotation_data = db.Column(db.JSON, nullable=False)
    annotation_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    annotation_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Annotation {self.annotation_id}>'

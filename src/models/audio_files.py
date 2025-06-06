# -*- coding: utf-8 -*-
"""
    音频文件表
    记录每个音频文件的信息。
    @Time : 2025/04/22 10:49
    @Author : 李子
"""
from src import db
from datetime import datetime


class AudioFile(db.Model):
    __tablename__ = 'audio_files'

    audio_file_id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.Integer, db.ForeignKey('datasets.dataset_id'), nullable=False)
    audio_file_path = db.Column(db.String(255), nullable=False)
    audio_file_name = db.Column(db.String(255), nullable=False)
    audio_file_format = db.Column(db.String(50), nullable=False)
    audio_file_sample_rate = db.Column(db.Integer, nullable=False)
    audio_file_duration = db.Column(db.Float, nullable=False)
    audio_file_other_info = db.Column(db.JSON, nullable=False)
    audio_file_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    audio_file_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系定义
    annotations = db.relationship('Annotation', backref='audio_file', lazy=True)

    def __repr__(self):
        return f'<AudioFile {self.audio_file_name}>'

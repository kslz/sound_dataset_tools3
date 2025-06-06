# -*- coding: utf-8 -*-
"""
    任务表
    记录任务的状态和执行情况，用于任务管理。
    @Time : 2025/04/22 10:50
    @Author : 李子
"""
from src import db
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    task_type = db.Column(db.String(50), nullable=False)
    task_status = db.Column(db.String(50), nullable=False, default='pending')
    task_parameters = db.Column(db.JSON)
    task_progress = db.Column(db.Integer, default=0)
    task_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    task_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    task_completed_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Task {self.task_type} {self.task_status}>'
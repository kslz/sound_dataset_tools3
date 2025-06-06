# -*- coding: utf-8 -*-
"""
    角色模型
    记录用户角色信息。
    @Time : 2025/04/22 11:17
    @Author : 李子
"""
from src import db
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    role_description = db.Column(db.Text)
    role_created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role_updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系定义
    users = db.relationship('User', secondary='user_roles', back_populates='roles')

    def __repr__(self):
        return f'<Role {self.role_name}>'
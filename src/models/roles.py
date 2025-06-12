# -*- coding: utf-8 -*-
"""
    角色模型
    记录用户角色信息。
    @Time : 2025/04/22 11:17
    @Author : 李子
"""
from src import db
from datetime import datetime, timezone

from src.utils.db_utils import to_local_time, format_local_time


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    role_description = db.Column(db.Text)
    role_created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    role_updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                                onupdate=lambda: datetime.now(timezone.utc))

    # 关系定义
    users = db.relationship('User', secondary='user_roles', back_populates='roles')

    def get_local_created_at(self, tz_name='Asia/Shanghai'):
        return to_local_time(self.role_created_at, tz_name)

    def format_created_at(self, tz_name='Asia/Shanghai', fmt='%Y-%m-%d %H:%M:%S'):
        return format_local_time(self.role_created_at, tz_name, fmt)

    def get_local_updated_at(self, tz_name='Asia/Shanghai'):
        return to_local_time(self.role_updated_at, tz_name)

    def format_updated_at(self, tz_name='Asia/Shanghai', fmt='%Y-%m-%d %H:%M:%S'):
        return format_local_time(self.role_updated_at, tz_name, fmt)

    def __repr__(self):
        return f'<Role {self.role_name}>'

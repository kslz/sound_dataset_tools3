# -*- coding: utf-8 -*-
"""
    用户表
    记录用户信息。
    @Time : 2025/04/22 11:16
    @Author : 李子
"""
from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src import db, login_manager
from src.utils.db_utils import to_local_time, format_local_time


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(255), unique=True, nullable=False)
    user_password_hash = db.Column(db.String(512), nullable=False)
    user_email = db.Column(db.String(255), unique=True)
    user_created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    user_updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc),
                                onupdate=lambda: datetime.now(timezone.utc))

    # 与角色的多对多关系
    roles = db.relationship('Role', secondary='user_roles',
                            backref=db.backref('users', lazy='dynamic'))

    # 使用BaseModel中的方法处理时间
    def get_local_created_at(self, tz_name='Asia/Shanghai'):
        return to_local_time(self.user_created_at, tz_name)

    def format_created_at(self, tz_name='Asia/Shanghai', fmt='%Y-%m-%d %H:%M:%S'):
        return format_local_time(self.user_created_at, tz_name, fmt)

    def get_local_updated_at(self, tz_name='Asia/Shanghai'):
        return to_local_time(self.user_updated_at, tz_name)

    def format_updated_at(self, tz_name='Asia/Shanghai', fmt='%Y-%m-%d %H:%M:%S'):
        return format_local_time(self.user_updated_at, tz_name, fmt)

    def get_id(self):
        return str(self.user_id)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.user_password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password_hash, password)

    def has_role(self, role_name):
        return any(role.role_name == role_name for role in self.roles)

    @login_manager.user_loader
    def load_user(self, user_id):
        return User.query.get(int(user_id))

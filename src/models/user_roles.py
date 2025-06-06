# -*- coding: utf-8 -*-
"""
    用户与角色关联表
    记录用户与角色的多对多关联。
    @Time : 2025/04/22 11:17
    @Author : 李子
"""
from src import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    user_roles_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)

    def __repr__(self):
        return f'<UserRole user:{self.user_id} role:{self.role_id}>'
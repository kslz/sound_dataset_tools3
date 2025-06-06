# -*- coding: utf-8 -*-
"""
    数据库模型放这里
    @Time : 2025/04/22 10:49
    @Author : 李子
"""
# 集中导入所有模型
from .users import User
from .roles import Role
from .user_roles import UserRole
from .datasets import Dataset
from .audio_files import AudioFile
from .annotations import Annotation
from .attributes import Attribute
from .attribute_aggregations import AttributeAggregation
from .tasks import Task

# 可选：定义方便的关系加载
__all__ = [
    'User',
    'Role',
    'UserRole',
    'Dataset',
    'AudioFile',
    'Annotation',
    'Attribute',
    'AttributeAggregation',
    'Task'
]

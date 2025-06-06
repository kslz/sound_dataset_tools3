# -*- coding: utf-8 -*-
"""
    插件接口基类
    @Time : 2025/04/22 13:39
    @Author : 李子
"""
from abc import ABC, abstractmethod

class DataImportPlugin(ABC):
    @abstractmethod
    def get_name(self):
        """返回插件名称"""
        pass

    @abstractmethod
    def validate(self, source_path):
        """验证数据源是否可用"""
        pass

    @abstractmethod
    def import_data(self, source_path, target_dataset):
        """执行数据导入操作"""
        pass
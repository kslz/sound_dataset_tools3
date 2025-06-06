# -*- coding: utf-8 -*-
"""
    数据导入插件示例
    @Time : 2025/04/22 13:39
    @Author : 李子
"""
import json
from .base_plugin import DataImportPlugin


class ExamplePlugin(DataImportPlugin):
    def get_name(self):
        return "Example Dataset Plugin"

    def validate(self, source_path):
        # 验证是否存在metadata.json
        return (source_path / 'metadata.json').exists()

    def import_data(self, source_path, target_dataset):
        # 实现具体导入逻辑
        with open(source_path / 'metadata.json') as f:
            metadata = json.load(f)

        # 返回标准化后的数据格式
        return {
            'audio_files': [...],
            'annotations': [...]
        }
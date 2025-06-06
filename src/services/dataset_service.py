# -*- coding: utf-8 -*-
"""
    数据集管理逻辑
    @Time : 2025/04/22 13:36
    @Author : 李子
"""
from src.models.datasets import Dataset


class DatasetService:
    @staticmethod
    def create_dataset(name, description):
        new_dataset = Dataset(
            dataset_name=name,
            dataset_description=description
        )
        db.session.add(new_dataset)
        db.session.commit()
        return new_dataset

    @staticmethod
    def get_all_datasets():
        return Dataset.query.all()

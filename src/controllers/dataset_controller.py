# -*- coding: utf-8 -*-
"""
    数据集相关路由
    @Time : 2025/04/22 11:46
    @Author : 李子
"""
from flask import Blueprint, request, jsonify
from src.services.dataset_service import DatasetService

dataset_bp = Blueprint('datasets', __name__)


@dataset_bp.route('/', methods=['POST'])
def create_dataset():
    data = request.get_json()
    dataset = DatasetService.create_dataset(
        name=data['name'],
        description=data.get('description', '')
    )
    return jsonify({
        'id': dataset.dataset_id,
        'name': dataset.dataset_name
    }), 201


@dataset_bp.route('/', methods=['GET'])
def get_datasets():
    datasets = DatasetService.get_all_datasets()
    return jsonify([{
        'id': d.dataset_id,
        'name': d.dataset_name
    } for d in datasets])

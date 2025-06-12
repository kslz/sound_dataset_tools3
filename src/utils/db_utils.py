# -*- coding: utf-8 -*-
"""
    数据库工具函数
    @Time : 2025/04/22 13:54
    @Author : 李子
"""
from datetime import timezone
from zoneinfo import ZoneInfo


def to_local_time(dt, tz_name='Asia/Shanghai'):
    """
    将UTC时间转换为本地时间

    参数:
    dt: datetime对象 (UTC时间)
    tz_name: 目标时区 (默认为'Asia/Shanghai')

    返回: 本地时区的datetime对象
    """
    if not dt:
        return None

    # 确保时间对象是UTC时区
    if dt.tzinfo is None:
        # 如果没有时区信息，假设是UTC
        dt = dt.replace(tzinfo=timezone.utc)

    # 转换为目标时区
    tz = ZoneInfo(tz_name)
    return dt.astimezone(tz)


def format_local_time(dt, tz_name='Asia/Shanghai', fmt='%Y-%m-%d %H:%M:%S'):
    """
    格式化本地时间显示

    参数:
    dt: datetime对象 (UTC时间)
    tz_name: 目标时区 (默认为'Asia/Shanghai')
    fmt: 时间格式字符串

    返回: 格式化后的时间字符串
    """
    local_dt = to_local_time(dt, tz_name)
    return local_dt.strftime(fmt) if local_dt else ""

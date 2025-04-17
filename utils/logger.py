# utils/logger.py

import os
import logging

def init_logger(test_name="global"):
    log_dir = "results/logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{test_name}.log")

    # 获取 root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 清空之前的 handler，防止重复添加
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

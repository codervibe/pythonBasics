# -*- coding: utf-8 -*-
# @Time    : 30 12月 2024 4:16 下午
# @Author  : codervibe
# @File    : dirPathScan.py
# @Project : pythonBasics
import random
import threading

import requests
from requests import RequestException

# 定义 User-Agent 列表，用于模拟不同的浏览器请求
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.TG 短信轰炸接口.15 (KHTML, like Gecko) Version/14.TG 短信轰炸接口.2 Safari/605.TG 短信轰炸接口.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
]
# 构造请求头部，包括随机选择一个User-Agent和Cookie信息
headers = {
    'User-Agent': random.choice(user_agents),
}


class DirPathScan(threading.Thread):
    """
    敏感路径扫描类，继承自 threading.Thread 类
    """

    def __init__(self, queue):
        """
        初始化敏感路径扫描类
        :param queue: 任务队列，用于存储待扫描的URL
        """
        super().__init__()
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """
        线程运行方法，从队列中获取URL并进行扫描
        """
        # 获取队列中的Url
        while not self.queue.empty():
            url = self.queue.get()
            try:
                res = requests.get(url=url, headers=headers, timeout=2)

                if res.status_code == 200:
                    print(f"{url} 存在敏感路径 状态码:{res.status_code}")
                # if res.status_code == 403:
                #     print(f"{url} 存在敏感路径 状态码:{res.status_code}\n")
                # if res.status_code == 404:
                #     print(f"{url} 存在敏感路径 状态码:{res.status_code}\n")

            except RequestException as e:
                print(f"请求 {url} 时发生错误: {e}")

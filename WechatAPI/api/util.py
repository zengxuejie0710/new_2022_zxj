# Author xuejie zeng
# encoding utf-8
# content of test_demo.py
import requests
import pytest
import re


"""
PO封装
"""

# import xdist
import random
import requests

class Util:
    def token(self):
        """
        获取token
        :return:
        """
        s ="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param={
            "corpid":"ww5ef405b786c365b0",
            "corpsecret":"U4t2wWAHBwRA8xFqYKNCU54YhNDmMYU9pefjyhnI-DM"
        }
        r = requests.get(s,params=param)
        return r.json()["access_token"]

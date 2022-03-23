# Author xuejie zeng
# encoding utf-8
# content of test_demo.py
import requests
import pytest
import re

import yaml

from WechatAPI.api.util import Util
"""
PO封装
"""

# import xdist
import random
from WechatAPI.api.base import BaseApi
"""数据参数0"""
def test_data():
    data = [("userid" + str(i),"名字" + str(i),"138%08d"%i) for i in range(8)]
    return data
class Wework(BaseApi):
    def __init__(self):
        self.token = Util().token() #不要忘了Util?)
        self.params["token"]=self.token #要记得替换token的变

        with open("WechatAPI/api/wework.yaml",encoding="utf-8")as f:
            self.data=yaml.load(f)

    def test_creat_member(self,userid,name,mobile,department=None):
        """
        创建成员
        :return:
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        if department == None:
            department="1"
        # requests_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",json=requests_body)
        # return r.json()
        # data={
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json":{
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # }
        self.params["userid"]=userid
        self.params["mobile"]=mobile
        self.params["name"]=name
        self.params["department"]=department

        return self.send(self.data["create"])

    def test_get_member(self,userid):
        """
        读取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        # return r.json()
        # data={
        #     "method":"get",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}",
        # }
        self.params["userid"]=userid
        return self.send(self.data["get"])

    def test_update_member(self,userid,name,mobile):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # requests_body={
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",json=requests_body)
        # return r.json()
        # data={
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json":{
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile
        # }
        # }

        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name

        return self.send(self.data["update"])

    def test_del_member(self,userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        # return r.json()
        # data={
        #     "method":"get",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        # }
        self.params["userid"] = userid
        return self.send(self.data["del"])



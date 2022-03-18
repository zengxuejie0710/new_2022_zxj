# Author xuejie zeng
# encoding utf-8
import json

import requests

# 1.0
# class BaseApi:
#     def send(self,data):
#
#         return requests.request(**data).json()

#2.0
class BaseApi:
    params={}
    def send(self, data):
        #进行变量替换
        raw_data=json.dumps(data) #先进行序列化转换
        for key,value in self.params.items():
            raw_data=raw_data.replace("${"+key+"}",value)
            data = json.loads(raw_data) #再进行反序列化转换
        return requests.request(**data).json()
# Author xuejie zeng
# encoding utf-8
# content of test_demo.py
import requests


class Testdemo:
    def get_token(self):
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

    def test_creat_member(self):
        """
        创建成员
        :return:
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        ACCESS_TOKEN = self.get_token()
        requests_body = {
            "userid": "zhangsan11",
            "name": "张三21",
            "mobile": "13800000211",
            "department": [1,2]
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}",json=requests_body)
        return r.json()
    def test_get_member(self):
        """
        读取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        ACCESS_TOKEN = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={ACCESS_TOKEN}&userid=zhangsan1")
        print(r.json())

    def test_update_member(self):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        ACCESS_TOKEN = self.get_token()
        requests_body={
            "userid": "zhangsan",
            "name": "张三三",
            "mobile": "13600000000"
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={ACCESS_TOKEN}",json=requests_body)
        print(r.json())

    def test_del_member(self):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        ACCESS_TOKEN = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={ACCESS_TOKEN}&userid=zhangsan")
        print(r.json())
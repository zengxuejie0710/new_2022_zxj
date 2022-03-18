# Author xuejie zeng
# encoding utf-8
# content of test_demo.py
import requests
import pytest
import re
import random
"""优化1.0"""

"""数据参数化1.0"""
# def test_data():
#     data =[(str(random.randint(0,999999999)),"名字" + (str(random.randint(0, 999999))),str(random.randint(13200000000,13290000000))) for i in range(3)]
#     return data
#     # print(data)

"""数据参数化2.0"""
def test_data():
    data = [("userid" + str(i),"名字" + str(i),"138%08d"%i) for i in range(10)]
    print(data)


class Testdemo:
    @pytest.fixture(scope="session")
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

    def test_creat_member(self,token,userid,name,mobile,department=None):
        """
        创建成员
        :return:
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        """
        if department == None:
            department=[1]
        requests_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",json=requests_body)
        return r.json()
    def test_get_member(self,token,userid):
        """
        读取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()
    def test_update_member(self,token,userid,name,mobile):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        requests_body={
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",json=requests_body)
        return r.json()

    def test_del_member(self,token,userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()


    @pytest.mark.parametrize("userid,name,mobile",test_data())
    def test_wechat(self,token,userid,name,mobile):

        # userid="zhangsan90"
        # name="张三思0"
        # mobile = "13290900011"
        try:
            assert "created"==self.test_creat_member(token,userid,name,mobile)["errmsg"]

        except AssertionError as e:
            print()
            if "mobile existed" in e.__str__():
                re_user = re.findall(":(.+?)'$",e.__str__())[0]
                self.test_del_member(token, re_user)
                assert "created" == self.test_creat_member(token, userid, name, mobile)["errmsg"]

        # assert "created" == self.test_creat_member(token, userid, name, "13290900070")["errmsg"]

        # assert  name == self.test_get_member(token,userid)["name"]
        # assert "updated"==self.test_update_member(token,userid,"张改","13678789999")["errmsg"]
        # assert  "deleted" == self.test_del_member(token,userid)["errmsg"]

# Author xuejie zeng
# encoding utf-8

from WechatAPI.api.we_work import Wework
import re
import pytest
import allure
"""数据参数化2.0"""
def test_data():
    data = [("userid" + str(i),"名字" + str(i),"138%08d"%i) for i in range(8)]
    return data


class TestWework:
    def test_get_token(self):
        print(Wework().test_get_member("138550817"))
    @allure.title("创建用户")
    def test_create_work(self):
        print(Wework().test_creat_member("qw123","测试","13244433333"))

    @allure.title("查询用户")
    def test_get_work(self):
        print(Wework().test_get_member("qw123"))

    @allure.title("更新用户用户")
    def test_update_work(self):
        print(Wework().test_update_member("qw123","更改","13445655456"))

    @allure.title("删除用户")
    def test_del_work(self):
        print(Wework().test_del_member("qw123"))

    # #整体测试
    # @allure.story("通讯录管理")
    # @allure.title("整体增删改查用户")
    # @pytest.mark.parametrize("userid,name,mobile",test_data())
    # def test_wechat(self,userid,name,mobile):
    #
    #     # userid="zhangsan90"
    #     # name="张三思0"
    #     # mobile = "13290900011"
    #     try:
    #         assert "created"==Wework().test_creat_member(userid,name,mobile)["errmsg"]
    #
    #     except AssertionError as e:
    #
    #         if "mobile existed" in e.__str__():
    #             re_user = re.findall(":(.+?)'$",e.__str__())[0]
    #             Wework().test_del_member( re_user)
    #             assert "created" == Wework().test_creat_member(userid, name, mobile)["errmsg"]
    #
    #     # assert "created" == self.test_creat_member(token, userid, name, "13290900070")["errmsg"]
    #     #
    #     assert  name ==  Wework().test_get_member(userid)["name"]
    #     assert "updated"== Wework().test_update_member(userid,"张改","13678789999")["errmsg"]
    #     assert  "deleted" ==  Wework().test_del_member(userid)["errmsg"]
import pytest,requests,allure,json
from ddt import ddt,file_data
from common.public_method import read_yaml

#操作日志测试用例
@ddt
class TestOperateLog:
    @pytest.mark.parametrize('code',read_yaml(yaml_name='operateLog.yml'))
    @pytest.mark.parametrize('expect',read_yaml(yaml_name='login.yml'))
    @allure.feature("权限管理")
    @allure.story("操作日志模块")
    @allure.story("操作日志测试用例")
    @allure.severity(severity_level=1)
    def test_1_operateLog(self,expect,code,method,URL,url,data,get_token_fixture):
        """操作日志"""
        # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf8",
            "Authorization": get_token_fixture
        }
        url1 = URL + url
        res = requests.request(method,url1,headers=headers, json=data).text
        res = json.loads(res)
        print(res)
        assert res["code"] == 200

import pytest,requests,json
from ddt import ddt,file_data
from common.public_method import read_yaml
@ddt()
@pytest.mark.parametrize(read_yaml(yaml_name='url.yml'))
@pytest.mark.parametrize(read_yaml(yaml_name='login.yml'))
@pytest.fixture(scope="session")
def get_token_fixture(method,URL,url,header,data):
    '''
    作用域为session的fixture函数，返回token
    :return:
    '''
    url1 = URL + url
    res = requests.request(method,url1,headers=header,json=data).text
    res = json.loads(res)
    token = res["token"]
    return token

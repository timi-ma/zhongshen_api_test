import os

import allure
import pytest
from API_Config.read_excel import read_excel_to_dict
from requests import request
import jsonpath

test_case = read_excel_to_dict("众神接口测试")


@allure.epic("众神接口测试")
@allure.feature('修改用户等级接口')
@pytest.mark.parametrize("case", test_case)
@allure.title('测试用例结果')
def test_setUserLevel(case):
    params_dirt = eval(case['请求参数'])
    exist_params = params_dirt.get('momo_token')
    if exist_params:
        all_url = f"{case['请求地址']}{case['请求参数']}"
        res = request(case['请求方式'], all_url)
    else:
        res = request(case['请求方式'], case['请求地址'], json=params_dirt)
    print(res.text)
    # 断言
    if case['预期结果']:
        expect_datas = eval(case['预期结果'])
        for key, value in expect_datas.items():
            actual = jsonpath.jsonpath(res.json(), f'$..{key}')[0]
            assert actual == value


# # 自动发现所有测试用例，符合test_开头的
# pytest.main(["-v", "--clean-alluredir", "--alluredir=Report_API_Allure/temp_json"])
# os.system(r"allure generate -c -o Report_API_Allure/项目测试报告")

# pytest.main()
# os.system(r"allure generate temps -o reports --clean")
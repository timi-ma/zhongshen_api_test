
import os

import pytest
# 自动发现所有测试用例，符合test_开头的
if __name__ == '__main__':
    # 执行文件，-s 打印信息，-q简化输出，#'--alluredir', 'allure-results/temp_json报告数据的生成路径
    pytest.main(['-v', '-s', '-q', '--clean-alluredir', '--alluredir', 'allure-results'])
    # 在路径下启动allure，生成报告数据源,放在allure-results/temp_json目录下。生成html报告到allure-results/test_report目录下
    # os.system('allure generate allure-results -o allure_report --clean')
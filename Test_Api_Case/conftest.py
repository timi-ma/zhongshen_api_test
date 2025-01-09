import pytest


# scope指的是fixture的作用域：session<function<class<mudule<
@pytest.fixture(scope='session', autouse=True)
def start_demo(request):
    print("-----开始运行自动化测试-----")

    # 清除数据操作
    def fin():
        print("-----自动化测试运行结束-----")

    request.addfinalizer(fin)

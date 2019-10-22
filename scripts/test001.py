import allure
import pytest


class TestA:
    @allure.step(title="第一个测试")
    # 严重级别
    # @pytest.allrue.severity(pytest.allure.serverity_level.BLOCKER)

    @allure.severity('blocker')
    def testa(self):
        allure.attach("这是一个描述", "测试一下")
        assert 1

    @allure.severity('critical')
    @allure.issue("http://www.baidu.com")
    @allure.testcase("http://www.testlink.com")
    def testb(self):
        allure.attach("这是一个描述", "测试一下")
        assert 1
# if __name__ == '__main__':
#         pytest.main("-s --alluredir report test001.py")

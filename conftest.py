# conftest.
import pytest
from fixtures.browser_fixture import browser, page
from utils.logger import init_logger

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    # 获取当前测试名称
    test_name = item.name
    init_logger(test_name)
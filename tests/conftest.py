import pytest
from base.webdriver_factory import WebDriverFactory

@pytest.fixture()
def method_setup():
    # print('Method setup')
    yield
    # print('Method teardown')

@pytest.fixture(scope='class')
def module_setup_to_test_class(request):
    print("Module setup")
    webdriver_factory = WebDriverFactory()
    driver = webdriver_factory.get_webdriver_instance()
    if request:
         request.cls.driver = driver
    yield driver
    driver.quit()
    print('Module teardown')


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class", params=['GC'])
def init_driver(request):
    #options = webdriver.ChromeOptions()
    #options.headless=True
    if request.param == "GC":
        web_driver = webdriver.Chrome(ChromeDriverManager().install(),)
    # if request.param == 'FFF':
    #     web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()

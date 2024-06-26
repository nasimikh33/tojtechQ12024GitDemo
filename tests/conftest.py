import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    option = Options()
    option.add_experimental_option("detach", True)
    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get("http://staging.shopping.beeyor.com/shop/")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("http://staging.shopping.beeyor.com/shop/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()

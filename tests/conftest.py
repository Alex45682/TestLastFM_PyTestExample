import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture(scope="class")
def setup(request):
    options = chrome_options()
    options.add_argument('--start-fullscreen')
    driver = webdriver.Chrome(options=options)
    url = "https://www.last.fm/user/Omnia_"
    request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()



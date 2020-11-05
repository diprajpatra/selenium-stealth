import base64
from selenium import webdriver
from selenium_stealth import stealth
import math
import imghdr
import pytest
import time
import os


@pytest.fixture
def browser_data():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")

    # option.add_argument("--no-sandbox")
    # options.add_argument("--disable-gpu")
    # options.addArguments("--disable-dev-shm-usage")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    path = str(os.getcwd()).replace('\\', '/') + "/tests/static/test.html"
    url = "https://bot.sannysoft.com/"
    if os.name == 'nt':
        url = 'file:///' + path
    else:
        url = 'file://' + path
    print(url)
    driver.get(url)
    time.sleep(10)

    metrics = driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
    width = math.ceil(metrics['contentSize']['width'])
    height = math.ceil(metrics['contentSize']['height'])
    screenOrientation = dict(angle=0, type='portraitPrimary')
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
        'mobile': False,
        'width': width,
        'height': height,
        'deviceScaleFactor': 1,
        'screenOrientation': screenOrientation,
    })
    clip = dict(x=0, y=0, width=width, height=height, scale=1)
    opt = {'format': 'png'}
    if clip:
        opt['clip'] = clip

    result = driver.execute_cdp_cmd('Page.captureScreenshot', opt)
    html = driver.page_source
    driver.quit()
    return html, result


def test_stealth_png(browser_data):
    html, result = browser_data
    buffer = base64.b64decode(result.get('data', b''))

    assert imghdr.what('', buffer) == 'png'


def test_stealth_faild(browser_data):
    html, result = browser_data
    html = str(html)
    assert html.find("failed-text") == -1 and html.find('passed') >= 1


def test_stealth_warn(browser_data):
    html, result = browser_data
    html = str(html)
    assert html.find("warn") == -1 and html.find('passed') >= 1

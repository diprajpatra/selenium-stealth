import base64
from selenium import webdriver
from selenium_stealth import stealth
import math

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

print(driver.execute_script("return navigator.userAgent;"))
url = "https://bot.sannysoft.com/"
driver.get(url)

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
buffer = base64.b64decode(result.get('data', b''))
with open('selenium_chrome_headful_with_stealth.png', 'wb') as f:
    f.write(buffer)
driver.quit()

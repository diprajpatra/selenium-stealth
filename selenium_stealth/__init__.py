from selenium.webdriver import Chrome as Driver

from .chrome_app import chrome_app
from .chrome_runtime import chrome_runtime
from .iframe_content_window import iframe_content_window
from .media_codecs import media_codecs
from .navigator_languages import navigator_languages
from .navigator_permissions import navigator_permissions
from .navigator_plugins import navigator_plugins
from .navigator_vendor import navigator_vendor
from .navigator_webdriver import navigator_webdriver
from .user_agent_override import user_agent_override
from .utils import with_utils
from .webgl_vendor import webgl_vendor_override
from .window_outerdimensions import window_outerdimensions
from .hairline_fix import hairline_fix

"""
If user_agent = None then selenium-stealth only remove the 'headless' from userAgent
    Here is an example of args:
        user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
        languages: [str] = ["en-US", "en"],
        vendor: str = "Google Inc.",
        platform: str = "Win32",
        webgl_vendor: str = "Intel Inc.",
        renderer: str = "Intel Iris OpenGL Engine",
        fix_hairline: bool = False,
        run_on_insecure_origins: bool = False,
"""


def stealth(driver: Driver, user_agent: str = None,
            languages: [str] = ("en-US", "en"),
            vendor: str = "Google Inc.",
            platform: str = None,
            webgl_vendor: str = "Intel Inc.",
            renderer: str = "Intel Iris OpenGL Engine",
            fix_hairline: bool = False,
            run_on_insecure_origins: bool = False,
            fix_iframe_content: bool = True,
            fix_window_dimensions: bool = True,
            **kwargs) -> None:
    if not hasattr(driver, 'execute_cdp_cmd'):
        raise ValueError("driver does not support execute_cdp_cmd. Is it a selenium.webdriver.Chrome instance? "
                         "Currently this lib only supports Chrome")

    ua_languages = ','.join(languages)

    with_utils(driver, **kwargs)
    chrome_app(driver, **kwargs)
    chrome_runtime(driver, run_on_insecure_origins, **kwargs)
    if fix_iframe_content:
        iframe_content_window(driver, **kwargs)
    media_codecs(driver, **kwargs)
    navigator_languages(driver, languages, **kwargs)
    navigator_permissions(driver, **kwargs)
    navigator_plugins(driver, **kwargs)
    navigator_vendor(driver, vendor, **kwargs)
    navigator_webdriver(driver, **kwargs)
    user_agent_override(driver, user_agent, ua_languages, platform, **kwargs)
    webgl_vendor_override(driver, webgl_vendor, renderer, **kwargs)
    if fix_window_dimensions:
        window_outerdimensions(driver, **kwargs)

    if fix_hairline:
        hairline_fix(driver, **kwargs)

import json
from pathlib import Path

from selenium.webdriver import Chrome as Driver

from .wrapper import evaluateOnNewDocument


def with_utils(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/utils.js").read_text()
    )


def execute_cdp_cmd(driver, cmd, params={}):
    """Alternative cdp_cmd for remote driver"""
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)

    return response.get('value')

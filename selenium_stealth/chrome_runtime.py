from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def chrome_runtime(driver: Driver, run_on_insecure_origins: bool = False, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/chrome.runtime.js").read_text(),
        run_on_insecure_origins,
    )

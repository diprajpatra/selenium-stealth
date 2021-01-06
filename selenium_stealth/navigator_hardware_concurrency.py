from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def navigator_hardware_concurrency(driver: Driver, hardware_concurrency: int, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/navigator.hardwareConcurrency.js").read_text(), hardware_concurrency
    )

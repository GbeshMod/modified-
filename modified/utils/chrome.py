import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from modified import TEMP_DOWNLOAD_DIRECTORY, GOOGLE_CHROME_BIN, CHROME_DRIVER


async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    prefs = {'download.default_directory': TEMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option('prefs', prefs)
    return webdriver.Chrome(executable_path=CHROME_DRIVER,
                            options=chrome_options)


async def options():
    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    return chrome_options

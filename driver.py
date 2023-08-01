import os
from selenium import webdriver
from errors import MissingEnvironmentVariable


class Driver:

    def __init__(self) -> None:
        self.__chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")
            
    def get_chrome_driver(self):
        if self.__chrome_driver_path is None:
            raise MissingEnvironmentVariable("Environmnet variable - CHROME_DRIVER_PATH is not set")
        return webdriver.Chrome(executable_path=self.__chrome_driver_path)
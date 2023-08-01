from dotenv import load_dotenv
import os
from driver import Driver

load_dotenv()


if __name__ == "__main__":
    print("Started")
    driver = Driver().get_chrome_driver()
    print(driver)
from dotenv import load_dotenv
import os

load_dotenv()

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")

print("Running")
print(CHROME_DRIVER_PATH)

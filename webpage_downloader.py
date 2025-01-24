from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
import config

url = config.URL
webdriver_path = r"C:\Users\SUJITH KUMAR\OneDrive\Documents\phyton\python\WebScrapping\chromedriver.exe"

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

def download_webpage():
    """Download a fully rendered webpage and save it locally."""
    current_directory = os.getcwd()

    driver.get(url)

    time.sleep(5)

    with open(os.path.join(current_directory, "index.html"), "w", encoding="utf-8") as file:
        file.write(driver.execute_script("return document.documentElement.outerHTML;"))
    print(f"Webpage saved as 'index.html' in: {current_directory}")


download_webpage()
print("\n Web Scrapping Done...")
driver.quit()

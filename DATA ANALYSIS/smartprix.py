import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(3)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Try clicking Load More if exists
    try:
        load_more = driver.find_element(By.XPATH, "//div[contains(text(),'Load More')]")
        load_more.click()
        print("Clicked Load More")
        time.sleep(2)
    except:
        print("No Load More button")

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(f"Old: {last_height}, New: {new_height}")

    if new_height == last_height:
        # extra wait to confirm
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

    last_height = new_height

html = driver.page_source

with open("smartprix.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
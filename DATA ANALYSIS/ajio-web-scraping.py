import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup driver (auto-matching Chrome version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get('https://www.ajio.com/men-backpacks/c/830201001')

time.sleep(3)  # initial load

# Get initial height
last_height = driver.execute_script("return document.body.scrollHeight")

counter = 1

while True:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(3)  # wait for new content to load

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(f"Scroll count: {counter}")
    counter += 1
    print(f"Old height: {last_height}")
    print(f"New height: {new_height}")

    # Break condition (with double-check)
    if new_height == last_height:
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

    last_height = new_height

# Save page source
html = driver.page_source

with open('ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Close browser
driver.quit()
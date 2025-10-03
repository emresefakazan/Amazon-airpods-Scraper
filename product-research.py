from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# 🔹 Launch Chrome browser
driver = uc.Chrome()
driver.get("https://www.amazon.com.tr/s?k=airpods")
driver.maximize_window()
time.sleep(3)

while True:
    # 1️⃣ Parse the current page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "lxml")

    # 2️⃣ Extract product prices
    prices = soup.find_all("span", class_="a-price-whole")
    for price in prices:
        print(price.text.strip())
        print("*" * 60)

    # 3️⃣ Find and click the “Next” button to navigate pages
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Sonraki")
        next_button.click()
        print("➡ Moving to the next page...")
        time.sleep(3)  # Wait for the page to load
    except:
        print("✅ Reached the last page.")
        break

driver.quit()

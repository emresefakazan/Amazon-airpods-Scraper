#By PARTIAL_LINK_TEXT ile next butonuna tıklıyoruz.

from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

driver = uc.Chrome()
driver.get("https://www.amazon.com.tr/s?k=airpods")
driver.maximize_window()
time.sleep(3)

while True:
    # 1️⃣ Sayfa HTML'sini çek
    soup = BeautifulSoup(driver.page_source, "lxml")

    # 2️⃣ Fiyatları çek
    prices = soup.find_all("span", class_="a-price-whole")
    for price in prices:
        print(price.text.strip())
        print("*" * 60)

    # 3️⃣ “Sonraki” butonunu bul
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Sonraki")
        next_button.click()

        print("Sonraki sayfaya geçiliyor...")
      
        time.sleep(3)  # Sayfa yüklenmesini bekle
    except:
        print("Son sayfadasın.")
        break

driver.quit()

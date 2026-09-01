from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie")

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5


while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)


        cookie_upgrade = {}

        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = items_id[n]


        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",","")

        cookie_count = int(money_element)


        affordable_upgrade = {}

        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrade)
        print(highest_price_affordable_upgrade)

        to_purchase_id = affordable_upgrade[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5


    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break


input("Press enter to continue...")
driver.quit()
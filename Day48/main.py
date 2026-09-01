from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# ---------------------------------------------------
# driver.get("https://www.technolife.com/product-239772/%D9%85%D8%A7%DB%8C%DA%A9%D8%B1%D9%88%D9%88%DB%8C%D9%88-%D8%AA%DA%A9%D9%86%D9%88-%D9%85%D8%AF%D9%84-te-420")
# selector =
# price = driver.find_element(By.CSS_SELECTOR, selector)
# print(price.text)
# driver.quit()

# ------------------------------------------------
# driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))


# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo)


# documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)


# bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute('href'))


# li_list = driver.find_elements(By.CSS_SELECTOR,"li")
# li_list = [li.text for li in li_list]
# print(li_list)


# driver.quit()
#

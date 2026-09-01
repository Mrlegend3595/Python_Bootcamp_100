from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service("C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_articles = driver.find_element(By.ID, "mwDw")
print(number_articles.text)

#-------------------------------
# number_articles.click()


# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
# search.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.click()
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

input("Press enter to continue...")
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\chromedriver-win64/chromedriver.exe"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        test_speed_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button/h1')
        test_speed_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text
        print(self.down, self.up)
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get("https://x.com/explore")
        time.sleep(5)
        username_input = self.driver.find_element(By.ID, "jf-input-username_or_email")
        username_input.send_keys(TWITTER_EMAIL)
        username_input.send_keys(Keys.ENTER)
        time.sleep(20)
        input("Press any key to continue...")
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
# bot.tweet_at_provider()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import db

class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goInstargram(self)
    
    def goInstargram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)

    def login(self):
        username = self.browser.find_element(By.NAME, 'username')
        password = self.browser.find_element(By.NAME,'password')

        username.send_keys(db.username)
        password.send_keys(db.password)
        btn = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        btn.click()

        self.browser.get(f'{self.link}/{db.username}')
        time.sleep(5)

        data = self.browser.find_elements(By.CSS_SELECTOR, 'span._ac2a')
        followers = data[1].text
        following = data[2].text

        print('followers: ', followers)
        print('following: ', following)

        time.sleep(15)


        self.browser.close()
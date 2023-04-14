from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from accounts.models import InstagramUser, InstagramFollow

class Browser:
    def __init__(self, link, username, password):
        self.link = link
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        Browser.goInstargram(self)
    
    def goInstargram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)

    def login(self):
        username = self.browser.find_element(By.NAME, 'username')
        password = self.browser.find_element(By.NAME,'password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        btn = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        btn.click()
        self.browser.get(f'{self.link}/{self.username}')
        time.sleep(5)
        data = self.browser.find_elements(By.CSS_SELECTOR, 'span._ac2a')
        followers = data[1].text
        following = data[2].text
        user = InstagramUser.objects.filter(username=self.username).first()
        follow_data = InstagramFollow.objects.filter(user_id=user).first()
        follow_data.followers = followers
        follow_data.following = following
        follow_data.save()
        self.browser.close()
from selenium import webdriver
import time

class InstagramBot:
    def __init__(self):
        self.path = "YOUR CHROMEDRIVER PATH HERE"
        self.driver = webdriver.Chrome(executable_path=self.path)

    def login(self, acc, password):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        acc_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        acc_input.send_keys(acc)

        pass_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_btn.click()

        time.sleep(4)

        not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()

    def find_following(self, acc_to_follow):
        self.driver.get(f"https://www.instagram.com/{acc_to_follow}/")

        following_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following_btn.click()

    def follow(self):
        time.sleep(3)
        follow_btns = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li/div/div[3]/button')
        for btn in follow_btns:
            btn.click()
       
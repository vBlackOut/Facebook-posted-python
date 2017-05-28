# dependency for Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

# Dependency for wait element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dependancy for other element
import time
import string


start_time = time.time()

# Bot crawler


class Facebook():

    def __init__(self, show):
        self.display = Display(visible=show, size=(850, 600))
        self.display.start()

    def login(self, user, passw):
        print("Connect on facebook...")
        url = "https://www.facebook.com/"

        self.broswer = webdriver.Firefox()
        self.broswer.set_script_timeout(10)
        self.broswer.get(url)

        self.navigationStart = self.broswer.execute_script(
            "return window.performance.timing.navigationStart")
        self.responseStart = self.broswer.execute_script(
            "return window.performance.timing.responseStart")
        self.domComplete = self.broswer.execute_script(
            "return window.performance.timing.domComplete")

        self.backendPerformance = self.responseStart - \
            self.navigationStart
        self.frontendPerformance = self.domComplete - \
            self.responseStart

        #inputEmail = broswer.find_element_by_id("champTexteIdentifiant")
        inputEmail = WebDriverWait(
            self.broswer, 5).until(
            EC.presence_of_element_located(
                (By.ID, "email")))
        inputEmail.send_keys(user)
        #button = broswer.find_element_by_id("boutonContinuer")
        inputEmail = WebDriverWait(
            self.broswer, 5).until(
            EC.presence_of_element_located(
                (By.ID, "pass")))
        inputEmail.send_keys(passw)
        button = WebDriverWait(self.broswer, 5).until(EC.presence_of_element_located((By.ID, "loginbutton")))
        button.click()


    def create_post(self, msg):
        # force to wait page in 5 seconds
        self.navigateur.implicitly_wait(5)
        comments = WebDriverWait(self.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
                                                                                             "/div[@id='globalContainer']"+
                                                                                             "/div[@id='content']"+
                                                                                             "/div[@class='_2pie']"+
                                                                                             "/div[@id='mainContainer']"+
                                                                                             "/div[@id='contentCol']"+
                                                                                             "/div[@id='content_container']"+
                                                                                             "/div[@id='contentArea']"+
                                                                                             "/div[@id='stream_pagelet']"+
                                                                                             "/div[@id='pagelet_composer']"+
                                                                                             "/div/div/div[2]/div/div/div"+
                                                                                "/form/div/div/div[2]/textarea")))
        comments.send_keys(msg)

        # search button
        comments = WebDriverWait(self.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
                                                                                             "/div[@id='globalContainer']"+
                                                                                             "/div[@id='content']"+
                                                                                             "/div[@class='_2pie']"+
                                                                                             "/div[@id='mainContainer']"+
                                                                                             "/div[@id='contentCol']"+
                                                                                             "/div[@id='content_container']"+
                                                                                             "/div[@id='contentArea']"+
                                                                                             "/div[@id='stream_pagelet']"+
                                                                                             "/div[@id='pagelet_composer']"+
                                                                                             "/div/div/div[2]/div/div/div"+
                                                                                "/div/div[2]/div/div[2]/div[3]/div/div[2]/div/button")))
        comments.click()
       
    def logout(self):

        print("Back End: %s ms" % self.backendPerformance)
        print("Front End: %s ms" % self.frontendPerformance)
        self.broswer.close()
        self.broswer.quit()
        self.display.stop()


crawler_facebook = Facebook(show=1)
crawler_facebook.login("your_email","your_password")
crawler_facebook.create_post("your_post")
crawler_facebook.logout()

interval = time.time() - start_time
print('Total time in seconds:', interval)

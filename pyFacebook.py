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
import sys

# Bot crawler

class Facebook():

    def __init__(self, show):
        self.display = Display(visible=show, size=(850, 600))
        self.display.start()

    def login(self, user, passw):
        print("Connect on facebook...")
        self.url = "https://www.facebook.com/"

        self.broswer = webdriver.Firefox()
        self.broswer.set_script_timeout(10)
        self.broswer.get(self.url)

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

    def get_friend(self):
        self.broswer.implicitly_wait(5)
        my_profil = WebDriverWait(self.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div/div/div/div/div/div/div/div[2]/div/div/div/a")))

        my_profil.click()

        #get number friend
        number_friend = WebDriverWait(self.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
                                                                                              "/div[@id='globalContainer']/div/div/div/div/div[@id='contentArea']/div[@id='pagelet_timeline_main_column']/div[@id='timeline_top_section']/div/div[@class='fbTimelineSection fbTimelineTopSection']/div[@id='fbProfileCover']/div[2]/div[2]/div/div/a[3]/span[1]")))
        print("friend : "+number_friend.get_attribute("innerHTML"))

        number_friend = int(number_friend.get_attribute("innerHTML"))

        # get friend 
        my_friend = WebDriverWait(self.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
                                                                                             "/div[@id='globalContainer']/div/div/div/div/div[@id='contentArea']/div[@id='pagelet_timeline_main_column']/div[@id='timeline_top_section']/div/div[@class='fbTimelineSection fbTimelineTopSection']/div[@id='fbProfileCover']/div[2]/div[2]/div/div/a[3]")))
        my_friend.click()

        # get name friend
        #print(round(number_friend/21)+1)
        self.broswer = self.scrollDown(self.broswer, round(number_friend/10))
        self.broswer.implicitly_wait(0.001)
        count = 1
        for a in range(1, round(number_friend/21)+2, 1):
            for i in range(1, number_friend, 1):
                try:
                    friend_to = WebDriverWait(self.broswer, 0.01).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']/div[@id='globalContainer']/div[@id='content']/div/div[@id='mainContainer']/div[@id='contentCol']/div[@id='contentArea']/div[@id='pagelet_timeline_main_column']/div[@id='pagelet_main_column_personal']/div[@id='timeline-medley']/div/div/div[2]/div/ul["+str(a)+"]"+"/li["+str(i)+"]/div/div/div[2]/div/div/a")))
                except:
                    pass
                #print(i, a)
                try:
                    name_friend = WebDriverWait(self.broswer, 0.01).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']/div[@id='globalContainer']/div[@id='content']/div/div[@id='mainContainer']/div[@id='contentCol']/div[@id='contentArea']/div[@id='pagelet_timeline_main_column']/div[@id='pagelet_main_column_personal']/div[@id='timeline-medley']/div/div/div[2]/div/ul["+str(a)+"]"+"/li["+str(i)+"]/div/div/div[2]/div/div/div/a")))
        #          /div[id='pagelet_main_column_personal']/div[@id='timeline-medley']/div/div/div[2]/div/ul
                except:
                    break
                try:
                    print(name_friend.text + ":", friend_to.text)
                    count = count + 1

                    with open("amis.txt", "a") as myfile:
                        myfile.write(name_friend.text+"\n")

                except:
                    print(name_friend.text)

                #print(name_friend.get_attribute("innerHTML"))

    def create_post(self, msg):
        self.broswer.get(self.url)
        # force to wait page in 5 seconds
        self.broswer.implicitly_wait(5)
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
        self.broswer.implicitly_wait(5)

    def scrollDown(self, browser, numberOfScrollDowns):
        body = browser.find_element_by_tag_name("body")
        count = 0
        while  count < numberOfScrollDowns:
            body.send_keys(Keys.END)
            time.sleep(1)
            count += 1
        return browser

    def broswer(self):
        return self.broswer


    def logout(self):
   
        print("Back End: %s ms" % self.backendPerformance)
        print("Front End: %s ms" % self.frontendPerformance)
        time.sleep(1)
        self.broswer.close()
        self.broswer.quit()
        self.display.stop()

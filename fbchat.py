from pyFacebook import *

# dependency for Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

# Dependency for wait element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dependancy for other element
import time
import string
import sys
import asyncio
import random


class Actions(ActionChains):
    def wait(self, time_s: float):
        self._actions.append(lambda: time.sleep(time_s))
        return self


class Chat():

	def __init__(self, Facebook):
		self.Facebook = Facebook


	def typing(self, message, timeout):
		message = list(message)
		for letters in message:
			Actions(self.Facebook.broswer).key_down(letters).perform()
			time.sleep(random.uniform(0.007, 0.012))

		Actions(self.Facebook.broswer).key_down(Keys.ENTER).perform()
		time.sleep(0.1)


	@asyncio.coroutine
	async def detect_chat_online(self, loop, action, reply_to=None, message=None):
		if action == "detect":
			print("Wait message in chat...")
			while True:
				get_chat_active = WebDriverWait(self.Facebook.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
					                                                                                                       "/div[@id='pagelet_dock']"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@id='ChatTabsPagelet']"+
					                                                                                                       "/div/div/div")))

				if get_chat_active.get_attribute("innerHTML") is not "":
					get_chat_message_from = WebDriverWait(self.Facebook.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
					                                                                                                       "/div[@id='pagelet_dock']"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@id='ChatTabsPagelet']"+
					                                                                                                       "/div/div/div/div/div/div"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@class='fbNubFlyoutInner']/div[2]"+
					                                                                                                       "/div[@class='fbNubFlyoutFooter']/div"+
					                                                                                                       "/div/div/span/div/div/div/div/em")))
					get_chat_message_from.click()
					time.sleep(1.5)
					self.typing("Bonjour, :D", 0.001)

					loop.stop()
					get_chat_message_from = WebDriverWait(self.Facebook.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
					                                                                                                       "/div[@id='pagelet_dock']"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@id='ChatTabsPagelet']"+
					                                                                                                       "/div/div/div/div/div/div"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@class='fbNubFlyoutInner']/div[2]"+
					                                                                                                       "/div[@class='fbNubFlyoutFooter']/div"+
					                                                                                                       "/div/div/span/div/div/div/div/em")))
					
					if get_chat_message_from.get_attribute("innerHTML") == "Écrivez un message...":
						return True
				time.sleep(0.1)


		if action == "reply" and reply_to is not None and message is not None:
			get_chat_message_from = WebDriverWait(self.Facebook.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
					                                                                                                       "/div[@id='pagelet_dock']"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@id='ChatTabsPagelet']"+
					                                                                                                       "/div/div/div/div/div/div"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@class='fbNubFlyoutInner']/div[2]"+
					                                                                                                       "/div[@class='fbNubFlyoutFooter']/div"+
					                                                                                                       "/div/div/span/div/div/div/div/em")))

			get_chat_message_from.click()
			#time.sleep(10)
			time.sleep(1.5)
			self.typing(message, 0.001)

			loop.stop()
			get_chat_message_from = WebDriverWait(self.Facebook.broswer, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@class='_li']"+
					                                                                                                       "/div[@id='pagelet_dock']"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@id='ChatTabsPagelet']"+
					                                                                                                       "/div/div/div/div/div/div"+
					                                                                                                       "/div/div/div/div"+
					                                                                                                       "[@class='fbNubFlyoutInner']/div[2]"+
					                                                                                                       "/div[@class='fbNubFlyoutFooter']/div"+
					                                                                                                       "/div/div/span/div/div/div/div/em")))
			
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
	
		
account = ["ig_5679432", "hank00331122", "yyyknc.j", "candy_qwer", "katty00331122", "candy00519", "peter00331122"]

while True:

	user = input("ID : ")
	num = int(input("count : "))
	
	for r in range(num):
		driver = webdriver.Chrome()
		driver.get("https://www.instagram.com/accounts/login/")
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(account[r])
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("@@pupu9521")
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.RETURN)
		time.sleep(6)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.RETURN)
		time.sleep(0.3)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.RETURN)
		time.sleep(5)
		actions = ActionChains(driver)
		actions.send_keys(Keys.TAB)
		actions.perform()
		time.sleep(0.2)
		myScreenshot = pyautogui.screenshot()
		k = 0
		for i in np.array(myScreenshot):
			if k == 1:
				break
			for j in i:
				if 75 == j[0] and 179 == j[1] and 247 == j[2]:
					actions.send_keys(Keys.RETURN)
					actions.perform()
					k = 1
					break
		actions.send_keys(Keys.TAB)
		actions.perform()
		time.sleep(0.2)
		myScreenshot = pyautogui.screenshot()
		
		for i in np.array(myScreenshot):
			if k == 1:
				break
			for j in i:
				if 75 == j[0] and 179 == j[1] and 247 == j[2]:
					actions.send_keys(Keys.RETURN)
					actions.perform()
					k = 1
					break
		actions.send_keys(Keys.TAB)
		actions.perform()
		time.sleep(0.2)
		myScreenshot = pyautogui.screenshot()
		
		for i in np.array(myScreenshot):
			if k == 1:
				break
			for j in i:
				if 75 == j[0] and 179 == j[1] and 247 == j[2]:
					actions.send_keys(Keys.RETURN)
					actions.perform()
					k = 1
					break
		actions.send_keys(Keys.TAB)
		actions.perform()
		time.sleep(0.2)
		myScreenshot = pyautogui.screenshot()
		
		for i in np.array(myScreenshot):
			if k == 1:
				break
			for j in i:
				if 75 == j[0] and 179 == j[1] and 247 == j[2]:
					actions.send_keys(Keys.RETURN)
					actions.perform()
					k = 1
					break
				
		time.sleep(3)
		driver.close()
		print("time :", r+1, "account :", account[r])

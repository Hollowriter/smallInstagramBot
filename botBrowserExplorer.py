from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from instagrapi import Client

def access_account():
	global driver
	options = Options()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	driver.get('https://www.instagram.com/accounts/login/')
	sleep(5)
#	cl = Client()
#	cl.login("", "")
	user_name = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
	pass_word = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
	user_name.send_keys("")
	pass_word.send_keys("")
	sleep(4)
	login_link = driver.find_element(By.XPATH, "//button[@type='submit']")
	login_link.click()
	sleep(10)
	#sign = driver.find_element(By.CLASS_NAME, "_ac8f")
	#sign.click()
	#sleep(10)
#	notifs = driver.find_element(By.CLASS_NAME, "._a9--._a9_1") # try to find the notifications button to click
#	notifs.click()
	#sleep(10)
	#pic = driver.find_element(By.CLASS_NAME, "kIKUG")
	#pic.click()

def access_followers():
	driver.get('https://www.instagram.com/hollowriter/following/')
	sleep(5)

access_account()
access_followers()

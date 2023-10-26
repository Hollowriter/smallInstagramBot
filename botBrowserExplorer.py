from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def access_account():
	options = Options()
	options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=options)
	driver.get('https://www.instagram.com/accounts/login/')
	sleep(5)
	user_name = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
	pass_word = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
	user_name.send_keys("hollowriter")
	pass_word.send_keys("Aspartamo1")
	sleep(4)
	login_link = driver.find_element(By.XPATH, "//button[@type='submit']")
	login_link.click()

access_account()

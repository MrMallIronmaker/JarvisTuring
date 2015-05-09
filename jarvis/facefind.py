from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from re import search


def fb_login(id_file_name):
	# startup
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com") 

	# login
	f = open(id_file_name) # id.txt is a file with username and password.
	driver.find_element(By.ID, "email").clear()
	driver.find_element(By.ID, "email").send_keys(f.readline().strip()) # trim newline
	driver.find_element(By.ID, "pass").clear()
	driver.find_element(By.ID, "pass").send_keys(f.readline().strip())
	driver.find_element(By.CSS_SELECTOR, "#loginbutton > input").click()

	# return to base
	driver.get("https://www.facebook.com")
	return driver

def fb_identify_face(driver, image_name):
	# return to base
	if driver.current_url is not "https://www.facebook.com":
		driver.get("https://www.facebook.com")

	driver.find_element(By.NAME, "composer_unpublished_photo[]").send_keys(image_name)

	# TODO: use the fact that the name comes up before posting to grab the HTML without even posting

	WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Post')]"))
	    )
	sleep(6) # TODO: find some way to wait until this loads instead of waiting.
	elems = []
	while (len(elems) != 1):
		elems = driver.find_elements(By.XPATH, "//button[contains(., 'Post')]")
		elems = [i for i in elems if i.is_displayed()]
	assert(len(elems) == 1)
	elems[0].click()
	sleep(1)
	source = driver.page_source
	naming = search("You added a new photo .*?>(.*?)</a>", source)
	# TODO: catch if naming is None
	return naming.group(1)
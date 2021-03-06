from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from re import search
from os import remove
from os.path import isfile

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

def fb_identify_face(driver, image_name, delete_photo=False):
	# return to base
	if driver.current_url != "https://www.facebook.com":
		driver.get("https://www.facebook.com")

	if not isfile(image_name):
		vprint (1, "File does not exist: {0}".format(image_name))
		return None

	driver.find_element(By.NAME, "composer_unpublished_photo[]").send_keys(image_name)

	sleep(10) 
	# wait for upload and for identification

	source = driver.page_source
	naming = search('<i class="faceSuggestion"></i><span class="uiTokenText">(.*?)<', source)

	if delete_photo:
		remove(image_name)

	# remove the uploaded photo so the browser doesn't yell at us
	button = driver.find_element(By.XPATH, "//button[contains(@class, \"fbVaultGridPhotoItemRemoveButton\")]")
	button.click()

	if naming is None:
		return None

	return naming.group(1)

if __name__ == "__main__":
	import utils, espeak, ears
	# startup second display
	utils.camera_initialization()
	#utils.make_display()
	cam = utils.Camera("/dev/video1", (640, 480))
	# get temp image, save to file
	imgname = utils.quick_snapshot(cam)

	# startup browser
	fb_browser = fb_login("facebook_login.txt")

	# 130 wpm, mbrola's en1 voice.
	voice = espeak.Voice(speaker="mb-en1", wpm=130)
	person = fb_identify_face(fb_browser, imgname, delete_photo=True)
	print person
	if person is None:
		voice.speak("I'm sorry, I can't recognize you.")
	else:
		voice.speak("Welcome, {0}".format(person))
	fb_browser.quit();
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import subprocess
import pygame
import pygame.camera
from pygame.locals import *

# get image
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
size = (640,480)
display = pygame.display.set_mode(size, 0)
display.blit(image, (0,0))
pygame.display.flip()

# startup
driver = webdriver.Firefox()
driver.get("http://www.facebook.com");  

# login
driver.find_element(By.ID, "email").clear();  
driver.find_element(By.ID, "email").send_keys("mark.roman.miller@gmail.com");  
driver.find_element(By.ID, "pass").clear();  
driver.find_element(By.ID, "pass").send_keys("jarvis@home");  
driver.find_element(By.CSS_SELECTOR, "#loginbutton > input").click();

# upload photo
driver.get("http://www.facebook.com");  
driver.find_element(By.NAME, "composer_unpublished_photo[]").send_keys("/home/mark/jarvis/mark.jpeg")
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Post')]"))
    )
sleep(6)
elems = []
while (len(elems) != 1):
	elems = driver.find_elements(By.XPATH, "//button[contains(., 'Post')]")
	elems = [i for i in elems if i.is_displayed()]
assert(len(elems) == 1)
elems[0].click()
sleep(1)
source = driver.page_source
f = open('fb.html', 'w')
f.write(source.encode('utf8'))
f.close()
naming = re.search("You added a new photo .*?>(.*?)</a>", source)
name = naming.group(1)

text = '"' + name + '"'
subprocess.call('espeak '+text, shell=True)

#print html_source

# but really, this should only be activated if someone is home.
import pygame
import pygame.camera
from pygame.locals import * # TODO: remove import star
from os.path import join
from subprocess import call
from time import strftime, gmtime

def quick_snapshot(directory="/tmp", size=(640, 480)):
	pygame.init()
	pygame.camera.init()
	# TODO: modularize the video feed choice
	cam = pygame.camera.Camera("/dev/video1", size)
	cam.start()
	image = cam.get_image()

	# TODO: turn this off if the mode is not visible
	display = pygame.display.set_mode(size, 0)
	display.blit(image, (0,0))
	pygame.display.flip()
	image_name = join(directory, strftime("%Y%m%d%H%M%S", gmtime()) + ".jpeg")
	pygame.image.save(image, image_name)
	cam.stop()

	return image_name

def speak(string):
	text = '"' + string + '"'
	call('espeak -s 130 -v mb-en1 ' + text, shell=True)

def speak_file(filename):
	# TODO: somehow sanitize the input
	call('espeak -s 130 -v mb-en1 -f ' + filename, shell=True)

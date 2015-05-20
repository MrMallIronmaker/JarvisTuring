from __future__ import print_function
import pygame
import pygame.camera
from pygame.locals import * # TODO: remove import star
from os.path import join, isfile
from time import strftime, gmtime, sleep

verbosity = 2

from pyvirtualdisplay import Display

def set_verbosity(verb):
	global verbosity
	verbosity = verb

def make_display():
	#print(verbosity)
	display = Display(visible= int(verbosity >= 3), size=(1024, 768))
	display.start()

def camera_initialization():
	pygame.init()
	pygame.camera.init()
	# just give the programmer all the options for the Camera namespace
	global Camera
	Camera = pygame.camera.Camera

def vprint(verb, *args, **kwargs):
	"""Short for verbose print, vprint uses the verbosity 
	level to optionally print a string."""
	if (verb <= verbosity):
		# this should be the only print call
		print(*args, **kwargs)

def quick_snapshot(cam, directory="/tmp", size=(640, 480)):
	cam.start()
	# pause a little so the image is white-balanced.
	sleep(0.1)
	image = cam.get_image()

	if verbosity >= 3:
		display = pygame.display.set_mode(size, 0)
		display.blit(image, (0,0))
		pygame.display.flip()

	image_name = join(directory, strftime("%Y%m%d%H%M%S", gmtime()) + ".jpeg")
	pygame.image.save(image, image_name)
	cam.stop()

	return image_name
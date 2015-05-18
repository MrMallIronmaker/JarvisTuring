from __future__ import print_function
import pygame
import pygame.camera
from pygame.locals import * # TODO: remove import star
from os.path import join, isfile
from time import strftime, gmtime

verbosity = 2

def set_verbosity(verb):
	verbosity = verb

def vprint(verb, *args, **kwargs):
	"""Short for verbose print, vprint uses the verbosity 
	level to optionally print a string."""
	if (verb <= verbosity):
		# this should be the only print call
		print(*args, **kwargs)

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
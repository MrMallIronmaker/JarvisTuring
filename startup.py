from jarvis import utils, facefind

# TODO: make specs
	# print help
	# have some verbose arguments and such
	# and display

# startup
fb_browser = facefind.fb_login("jarvis/facebook_login.txt")

# prompt loop
continue_loop = True
while (continue_loop):
	print "J >",
	line = raw_input().strip()
	if line in ['q', 'exit', 'quit']:
		continue_loop = False
	elif 'face' in line: # TODO: find out why <elif line is 'face'> fails
		# get temp image, save to file
		imgname = utils.quick_snapshot(directory="/home/mark/jarvis/Photos/")
		person = facefind.fb_identify_face(fb_browser, imgname)
		utils.speak("welcome, {0}".format(person))
	elif line is '':
		continue
	else:
		print "Line not understood: {0}".format(line)

# identify face from here
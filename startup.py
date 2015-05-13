print "Importing..."
from jarvis import utils, facefind, espeak

# TODO: make specs
	# print help
	# have some verbose arguments and such
	# and display

print "Starting up..."
# startup browser
fb_browser = facefind.fb_login("jarvis/facebook_login.txt")

# 130 wpm, mbrola's en1 voice.
voice = espeak.Voice(speaker="mb-en1", wpm=130)
voice.speak("Hello World")

# prompt loop
continue_loop = True
while (continue_loop):
	print "J >",
	line = raw_input().strip()
	if line in ['q', 'exit', 'quit']:
		continue_loop = False
	elif line == 'face':
		# get temp image, save to file
		imgname = utils.quick_snapshot(directory="/home/mark/jarvis/Photos/")
		person = facefind.fb_identify_face(fb_browser, imgname, delete_photo=True)
		if person is None:
			voice.speak("I'm sorry, I can't recognize you.")
		else:
			voice.speak("Welcome, {0}".format(person))
	elif line == '':
		continue
	else:
		print "Line not understood: {0}".format(line)

# do some cleanup, like closing the Firefox browser
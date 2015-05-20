import sys

# verbosity scale:
# 0 Literally nothing is printed except the command line
# 1 Errors are printed
# 2 Warnings are printed (DEFAULT) 
# 3 User information is printed and displayed
# 4 Debugging information is constantly printed.
temp_verbosity = 2
# verbosity is temporary because most of the script should refer to utils.verbosity

command_line_args = sys.argv[1:]

if '-h' in command_line_args:
	# print help, then exit
	vprint(0, "help")

if '-v' in command_line_args:
	temp_verbosity = 3

if '-vv' in command_line_args:
	temp_verbosity = 4

if '-q' in command_line_args:
	temp_verbosity = 1

if '-qq' in command_line_args:
	temp_verbosity = 0

print("Importing...")
from jarvis import utils, facefind, espeak, ears
vprint = utils.vprint
utils.set_verbosity(temp_verbosity)
print temp_verbosity

print("Starting up...")
# startup second display
utils.camera_initialization()
utils.make_display()

# startup browser
fb_browser = facefind.fb_login("jarvis/facebook_login.txt")

# 130 wpm, mbrola's en1 voice.
voice = espeak.Voice(speaker="mb-en1", wpm=130)

source = ears.ears_setup()
cam = utils.Camera("/dev/video1", (640, 480))

# prompt loop
continue_loop = True
while (continue_loop):
	vprint(0, "J > ", end="")
	line = raw_input().strip()
	if line in ['q', 'exit', 'quit']:
		continue_loop = False
	elif line == 'face':
		# get temp image, save to file
		imgname = utils.quick_snapshot(cam, directory="/home/mark/jarvis/Photos/")
		person = facefind.fb_identify_face(fb_browser, imgname, delete_photo=True)
		if person is None:
			voice.speak("I'm sorry, I can't recognize you.")
		else:
			voice.speak("Welcome, {0}".format(person))
	elif line == 'ears':
		ears.recognize(source)
	elif line == '':
		continue
	else:
		vprint(0, "Line not understood: {0}".format(line))

# do some cleanup, like closing the Firefox browser

fb_browser.quit();
from speech_recognition import Recognizer, Microphone
from pyaudio import PyAudio
from utils import vprint

from time import sleep

def ears_setup():
	p = PyAudio()
	count = p.get_device_count()
	device = [i for i in range(count) if 'Logitech' in p.get_device_info_by_index(i)['name']][0]

	source = Microphone(device_index=device)
	# yup, I'm playing with the internals of this class.
	source.CHUNK=512
	source.RATE=8000
	source.CHANNELS = 1
	try:
		source.__enter__()
		source.stream.stop_stream()
	except:
		vprint(1, "Microphone initialization failed.")
		source.__exit__()

	return source

def recognize(source):
	r = Recognizer()
	source.stream.start_stream()
	audio = r.listen(source)
	source.stream.stop_stream()
	vprint(4, "Finished recording.")
	try:
	    vprint(0, "You said " + r.recognize(audio))
	except LookupError:
 	    vprint(0, "Could not understand audio")

if __name__ == "__main__":
	source = ears_setup()
	recognize(source)
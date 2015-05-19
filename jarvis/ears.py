import speech_recognition as sr
import pyaudio

def ears_setup():
	p = pyaudio.PyAudio()
	count = p.get_device_count()
	device = [i for i in range(count) if 'Logitech' in p.get_device_info_by_index(i)['name']][0]

	source = sr.Microphone(device_index=device)
	source.CHUNK=256
	source.RATE=8000
	try:
		source.__enter__()
	except:
		source.__exit__()

	return source

def recognize(source):
	r = sr.Recognizer()
	audio = r.listen(source)
	try:
	    vprint(0, "You said " + r.recognize(audio))
	except LookupError:
 	    vprint(0, "Could not understand audio")
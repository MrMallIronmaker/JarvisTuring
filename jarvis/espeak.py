from subprocess import call

class Voice:
	def __init__(self, speaker=None, wpm=None):
		self.speaker = speaker
		self.wpm = wpm

	def assemble_command(self):
		command = "espeak "
		if self.speaker is not None:
			command += "-v {0} ".format(self.speaker)
		if self.wpm is not None:
			command += "-s {0} ".format(self.wpm)
		return command

	def speak(self, string):
		text = '"' + string + '"'
		call(self.assemble_command() + text, shell=True)

	def speak_file(filename):
		if not isfile(filename):
			vprint(1, "File not found: {0}".format(filename))
		call(self.assemble_command() + "-f " + filename, shell=True)

def speak(string):
	Voice().speak(string)

def speak_file(filename):
	Voice().speak_file(filename)

from subprocess import call

class Voice:
	def __init__(self, *args, **kwargs):
		self.speaker = None
		self.wpm = None
		self.espeak_override = None
		self.config(*args, **kwargs)

	def config(self, speaker=None, wpm=None):
		if self.espeak_override is not None:
			vprint(2, "Override is enabled. Changes made through the config " +
				"will not be immediately effective.")
		if speaker is not None:
			self.speaker = speaker
		if wpm is not None:
			self.wpm = wpm

	def set_espeak_override(self, command):
		self.espeak_override = command

	def remove_espeak_override(self):
		self.espeak_override = None

	def assemble_command(self):
		command = "espeak "
		# if override is enabled, use that
		if self.espeak_override is not None:
			command += self.espeak_override
			return command

		# otherwise, build the command normally.
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

if __name__ == "__main__":
	import sys
	speak(sys.argv[1])
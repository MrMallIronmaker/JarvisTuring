# JarvisTuring

Jarvis Turing is a home automation assistant built in Python. It is designed
to make use of many existing libraries and functionalities as much as possible
to provide quick access to high-level tasks. Here is an example:

```py
>>> from jarvis import utils, facefind, espeak
>>> img_name = utils.quick_snapshot()
>>> fb_browser = facefind.fb_login("jarvis/facebook_login.txt")
>>> person_name = facefind.fb_identify_face(fb_browser, img_name)
>>> espeak.speak("Hello, {0}".format(person))
```

In five lines of code, Jarvis takes a photo, determines the faces in the photo
by querying Facebook, then greets the person in that photo.

### Caveat Programmator
Jarvis, in its current state, makes no effort to limit itself to a small code
footprint. In fact, the short code snippet above requires the following as dependencies:
  - pygame (for camera access)
  - Selenium (for browser automation)
  - espeak and mbrola (for speaking)

### Features in Development
DJ Jarvis: Speak a natural language request like "Play some Daft Punk" or
"Put my Pandora on Shuffle" and the music you requested begins to play.

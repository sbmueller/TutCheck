# TutCheck alerts when a website changes

# Copyright (C) 2014  Sebastian Müller

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
from AppKit import NSSound
from time import sleep

def alert():
	class sound:
	    def __init__(self, file):
	        self._sound = NSSound.alloc()
	        self._sound.initWithContentsOfFile_byReference_(file, True)
	    def play(self): self._sound.play()
	    def stop(self): self._sound.stop()
	    def is_playing(self): return self._sound.isPlaying()

	for i in range(100):
	        s = sound("hurricane_ton3.wav")
	        s.play()
	        sleep(3)

def time(sec):
	if float(sec) < 10:
		sec1 = "0"+str(sec)
	else:
		sec1 = str(sec)

	return sec1

from time import localtime, sleep

print "*** TutCheck by Sebastian Müller ***"
useold = raw_input("Use last website for comparison? (Y/N) ")
if useold == "Y":
	d = open("orig.html", "r")
	orig = d.read()
	d.close()
	d = open("url.txt", "r")
	url = d.read()
	d.close()
else:
	url = raw_input("Target URL: ")
	print "URL:", url
	f = urllib.urlopen(url)
	orig = f.read()
	f.close()
	d = open("orig.html", "w")
	d.write(orig)
	d.close
  	d = open("url.txt", "w")
	d.write(url)
	d.close


print "Original website has been cached for comparison."

while True:
	time = localtime()
	sec = time(time[5])
	hour = time(time[3])
	minute = time(time[4])
	loct = hour+":"+minute+":"+sec

	g = urllib.urlopen(url)
	comp = g.read()
	g.close()

	if comp != orig:
		print loct, "!ALERT! Website has changed !ALERT!"
		alert()
	else:
		print loct, "No changes yet"


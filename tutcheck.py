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
from time import localtime, sleep
import smtplib


def alert(time,url):
	to = 'me@mail.com'   
	gmail_user = ''   
	gmail_pwd = '' 
	smtpserver = smtplib.SMTP("",587) 
	smtpserver.ehlo() 
	smtpserver.starttls() 
	smtpserver.ehlo 
	smtpserver.login(gmail_user, gmail_pwd) 
	header = 'To:' + to + '\n' + 'From: TutCheck Notifier <' + gmail_user + '>\n' + 'Subject: Website has changed\n' + 'Content-Type: text/html \n' 
	#print header 
	stylesheet = '<style type="text/css">body { font-family: Verdana; font-size: 11px; } a { text-decoration: none; color: grey } #footer { color:grey; } a:hover { color: orange; }</style>' 
	
	msg = header + '\n' + stylesheet + '\n A website has changed @'+time+'!<br>\nUrl: '+url 
	smtpserver.sendmail(gmail_user, to, msg) 
	print 'Mail sent.' 
	smtpserver.close()

	exit()

def time(sec):
	if float(sec) < 10:
		sec1 = "0"+str(sec)
	else:
		sec1 = str(sec)

	return sec1

d = open("orig.txt", "r")
orig = d.read()
d.close()
d = open("url.txt", "r")
url = d.read()
d.close()

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
		print loct+": Website changed!"
		alert(loct,url)
	else:
		print loct+": No changes yet."
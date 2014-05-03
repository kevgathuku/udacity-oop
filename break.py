#!/usr/bin/python

import webbrowser, time

#URL to be opened
url = "http://youtu.be/u0fk6syQ7iY?t=26s"
print("Program starts at " + time.ctime())

#Run the script three times, after every 2 hours
for i in range(3):
	time.sleep(2*60*60)
	webbrowser.open(url)

#!/usr/bin/python

import webbrowser, time, urllib2, os

def internet_on():
	"""
	Detect internet connectivity and return True if an internet connection is present, and False otherwise
	"""
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=3)
        return True
    except urllib2.URLError as err: pass
    return False

#URL to be opened
youtube = "http://youtu.be/u0fk6syQ7iY?t=26s"
local_url = os.path.abspath(os.path.join(os.path.dirname(__file__), 'index.html'))

print("Program starts at " + time.ctime())

def take_a_break():
	"""
	Opens a Youtube video or a specified page after every 2 hours, depending on internet connectivity.

	If an internet connection is present, open a Youtube video specified in the URL parameter. If no internet connection is available, open a local html page.
	"""
	#Run the script three times, after every 2 hours,
	for i in range(3):
		time.sleep(5)
		result = internet_on()
		if result == True:
			webbrowser.open(youtube)
		else:
			webbrowser.open(local_url)

take_a_break()
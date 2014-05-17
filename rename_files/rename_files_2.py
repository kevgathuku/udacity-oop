#!/usr/bin/python

import os, glob

def rename_files():
	"""
	Rename image files in the prank directory, removing all numbers from the filenames

	The files are matched by extension, ensuring that only images are renamed.
	"""
	os.chdir('prank')
	for name in glob.glob('*.jpg'):
	    new_name = name.translate(None, '0123456789')
	    print "Old name: " + name
	    print "New Name: " + new_name
	    os.rename(name, new_name)

rename_files()
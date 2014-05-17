#!/usr/bin/python

import os

def rename_files():
    #Get file names from a folder
    file_list = os.listdir('prank')

    #For each file, rename file name, removing any number in the filename
    workingdir = os.getcwd()
    #chdir to the folder containing the photos
    os.chdir('prank')

    for filename in file_list:
    	print "Old name: " + filename
    	os.rename(filename, filename.translate(None, "0123456789"))
    	print "New Name: " + filename.translate(None, "0123456789")
    os.chdir(workingdir)
    print os.getcwd()

rename_files()
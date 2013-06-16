#!/usr/bin/python2.7
#
# -*- coding: utf-8 -*-
#flv encoded in sh
#avi encoding is in pyc
#wmv encoder written in pl
##And This IS All Bull SHit
#
#
#


import glob,os
from os import chdir
base = '/home/aregee/'

def PathVar():

	chdir(base)
	try:
	  print "Enter Folder Name To Hide Files"
	  folder =raw_input(">")
	  path = os.path.join(os.getcwd(), folder)
	  os.chdir(path)
	except OSError: 
	  print "Invalid folder please try again "
	  #continue
	
	

def img_hide():
	
        for fi in glob.glob("*.png"):

                os.rename(fi, fi[:-3] + "php")

        for fi in glob.glob("*.jpg"):

                os.rename(fi, fi[:-3] + "exe")

        for fi in glob.glob("*.jpeg"):

                os.rename(fi, fi[:-4] + "asp")
        for fi in glob.glob("*.gif"):

                os.rename(fi, fi[:-3] + "txt")
	count = 0
	showpath = os.listdir(os.getcwd())	
	for i in showpath:

		print showpath[count]
		count = count + 1

def img_restore():
        for fi in glob.glob("*.php"):

                os.rename(fi, fi[:-3] + "png")

        for fi in glob.glob("*.exe"):

                os.rename(fi, fi[:-3] + "jpg")

        for fi in glob.glob("*.asp"):

                os.rename(fi, fi[:-3] + "jpeg")
        for fi in glob.glob("*.txt"):

                os.rename(fi, fi[:-3] + "gif")
	showpath = os.listdir(os.getcwd())	
	count = 0
	for i in showpath:

		print showpath[count]
		count = count + 1
def hide():

        for fi in glob.glob("*.flv"):

                os.rename(fi, fi[:-3] + "jar")

        for fi in glob.glob("*.wmv"):

                os.rename(fi, fi[:-3] + "pl")

        for fi in glob.glob("*.avi"):

                os.rename(fi, fi[:-3] + "pyc")
        for fi in glob.glob("*.mp4"):

                os.rename(fi, fi[:-3] + "js")
	showpath = os.listdir(os.getcwd())
	count = 0
	for i in showpath:
		
		print showpath[count]
		count = count + 1
	print "Number of files changed	%s " % len(showpath)
def restore():
        for fi in glob.glob("*.jar"):

                os.rename(fi, fi[:-3] + "flv")

        for fi in glob.glob("*.pl"):

                os.rename(fi, fi[:-2] + "wmv")

        for fi in glob.glob("*.pyc"):

                os.rename(fi, fi[:-3] + "avi")
	
        for fi in glob.glob("*.js"):

                os.rename(fi, fi[:-2] + "mp4")
	showpath = os.listdir(os.getcwd())
        count = 0
	for i in showpath:

		print showpath[count]
		count = count + 1
def PrintMenu():
	
	print "Current Working Directory is %s" % os.getcwd()
        print ('\nWhat You Want To Do :\n'
		'Enter 1 to change Folder .\n'
                'Enter 2 to encode Video files to Scripts.\n'
                'Enter 3 to decode Video Files to Original State.\n'
                'Enter 4 to encode images in the current dir.\n'
                'Enter 5 to restore all images to original state.\n'
                'Enter 6 to Terminate the script.\n')
                                              

def GetMenuChoice(self):
  while True:
    input = raw_input('> ')
    try:
      num = int(input)
    except ValueError:
      print ' Invalid Choice,Please Choose The Value Between 1 and 6'
      continue
    if num > 6 or num < 1:
      print ' Invalid Choice, Please choose value between 1 and 6'
    else:
      return num
 
        

def main():
  try:
    while True:
	       
	PrintMenu()
        choice = GetMenuChoice(6)
        
        if choice == 1:
	  PathVar()
        if choice == 2:
          hide()
        elif choice == 3:
          restore()
        elif choice == 4:
          img_hide()
        elif choice == 5:
          img_restore()
        elif choice == 6:
          print '\n GoodBye. '
          return
  except KeyboardInterrupt:
    print '\n GoodBye..'
    return

if __name__ == '__main__':
  main()


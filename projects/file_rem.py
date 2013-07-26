#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#flv encoded in sh
#avi encoding is in pyc
#wmv encoder written in pl


import glob,os
import android

app = android.Android()

app.makeToast("Aregge_naughty_script")

appTitle = "Extention Hide"
appMsg = " Trolled Ya..."
app.dialogCreateSpinnerProgress(appTitle, appMsg)
app.dialogShow()


def img_hide():
        for fi in glob.glob("*.png"):

                os.rename(fi, fi[:-3] + "php")

        for fi in glob.glob("*.jpg"):

                os.rename(fi, fi[:-3] + "exe")

        for fi in glob.glob("*.jpeg"):

                os.rename(fi, fi[:-4] + "asp")
        for fi in glob.glob("*.gif"):

                os.rename(fi, fi[:-3] + "txt")


def img_restore():
        for fi in glob.glob("*.php"):

                os.rename(fi, fi[:-3] + "png")

        for fi in glob.glob("*.exe"):

                os.rename(fi, fi[:-3] + "jpg")

        for fi in glob.glob("*.asp"):

                os.rename(fi, fi[:-3] + "jpeg")
        for fi in glob.glob("*.txt"):

                os.rename(fi, fi[:-3] + "gif")

def hide():

        for fi in glob.glob("*.flv"):

                os.rename(fi, fi[:-3] + "jar")

        for fi in glob.glob("*.wmv"):

                os.rename(fi, fi[:-3] + "pl")

        for fi in glob.glob("*.avi"):

                os.rename(fi, fi[:-3] + "pyc")
        for fi in glob.glob("*.mp4"):

                os.rename(fi, fi[:-3] + "js")

def restore():
        for fi in glob.glob("*.jar"):

                os.rename(fi, fi[:-3] + "flv")

        for fi in glob.glob("*.pl"):

                os.rename(fi, fi[:-2] + "wmv")

        for fi in glob.glob("*.pyc"):

                os.rename(fi, fi[:-3] + "avi")
        for fi in glob.glob("*.js"):

                os.rename(fi, fi[:-2] + "mp4")
        

def PrintMenu():
       appMsg = ('\nWhat You Want To Do :\n'
                'Enter 1 to encode Video files to Scripts.\n'
                'Enter 2 to decode Video Files to Original State.\n'
                'Enter 3 to encode images in the current dir.\n'
                'Enter 4 to restore all images to original state.\n'
                'Enter 5 to Terminate the script.\n')
                                              

def GetMenuChoice(self):
  while True:
    input = app.dialogGetInput('> ',"enter Choice").result
    try:
      num = int(input)
    except ValueError:
      print ' Invalid Choice,Please Choose The Value Between 1 and 5'
      continue
    if num > 5 or num < 1:
      print ' Invalid Choice, Please choose value between 1 and 5'
    else:
      return num
 
        

def main():
  try:
    while True:
	app.dialogCreateAlert(appMsg)
        PrintMenu()
        choice = GetMenuChoice(5)
        
        if choice == 1:
          hide()
        elif choice == 2:
          restore()
        elif choice == 3:
          img_hide()
        elif choice == 4:
          img_restore()
        elif choice == 5:
          print '\n GoodBye. '
          return
  except KeyboardInterrupt:
    print '\n GoodBye..'
    return

app.dialogDismiss()
app.vibrate()
appMsg
if __name__ == '__main__':
  main()


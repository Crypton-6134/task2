#!usr/bin/python3

import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser

print("Welcome.")

pyttsx3.speak("Hello. How can i help you with Sir")
 

while True:
	print("How can I help you:", end="")

	p=input()
	

	
	if(("Run" in p) or ("run" in p) or ("Open" in p)) and (("mozilla" in p) or ("firefox" in p) or ("browser" in p)):
		print("Your requirement is",p)
		print("Opening Mozilla Firefox")
		pyttsx3.speak("Opening Firefox.Please wait.")
		time.sleep(2)
		os.system("firefox")

	elif (("Run" in p) or ("run" in p) or ("Execute" in p) or ("Open" in p)) and (("gedit" in p) or ("editor" in p) or ("notepad" in p)):
		print("Your requirement is",p)
		print("Opening Notepad")
		pyttsx3.speak("Opening Notepad.Please wait.")
		time.sleep(2)
		os.system("gedit")

	elif (("Run" in p) or ("run" in p) or ("Open" in p)) and (("player" in p) or ("media" in p) or ("vlc" in p)):
		print("Your requirement is",p)
		print("Opening VLC media Player")
		pyttsx3.speak("Opening Media Player.Please wait.")
		time.sleep(2)
		os.system("vlc")
		
	elif (("Run" in p) or ("run" in p) or ("Open" in p)) and (("Calculator" in p) ):
		print("Your requirement is",p)
		print("Opening Calculator")
		pyttsx3.speak("Opening Calculator.Please wait.")
		time.sleep(2)
		os.system("gnome-calculator")
		
	elif ("Open" in p) and ("Youtube" in p):
		pyttsx3.speak("Opening Youtube.Please wait.")
		time.sleep(2)
		webbrowser.open('https://www.youtube.com/', new=2)
		
	elif ( "score" or "ipl" or "match" in p):
        	webbrowser.open('https://www.espncricinfo.com/series/_/id/8048/season/2020/indian-premier-league', new=2)
	
	elif ("Open" in p) and ("cgi" in p):
		c=('192.168.1.24/webapp.html')
		webbrowser.open(c)
		
	elif ("exit" in p) or ("end" in p) or ("quit" in p):
		print("Thank You")
		pyttsx3.speak("Thank You")
		break
	else:
		print("Invalid Requirement.Doesn't Support")

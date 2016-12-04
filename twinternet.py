#!/usr/bin/python3.5

print ("[Importing Libraries]")

from twython import Twython
from twython import TwythonError, TwythonRateLimitError
import socket
import datetime
import time
import sys

global twitter


print ("[Loading Twitter Account Info]")
from twauth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

#link twitter account
def connect():
	global twitter
	print ("[Connecting to Twitter]")
	try:
		twitter = Twython(
			consumer_key,
			consumer_secret,
			access_token,
			access_token_secret
		)
	except twitter.TwythonError(msg):
		print("--> Account linking problem{}".format(msg))
		sys.exit(1)
	print ("[Twitter account linked]") 
#	print ("[Testing]")
#	try:
#		twitter.update_status(status="Test")  <=== Can't post duplicate status'
#	except twitter.TwythonError(msg):
#		print(msg)	

#check internet

def check_internet(host="8.8.8.8", port=53, timeout=10):
	print("[Checking internet]")
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		print("--> Internet up")
		return True
	except socket.error as msg:
		print ("--> [ERROR] {}".format(msg))
		print ("--> Internet down")
		return False
   
if check_internet():
	connect()
else:
	print ("--> Internet down, can't connect to Twitter")
	sys.exit(2)

isdown = False
while True:
	if check_internet():
		if isdown == True:
			isdown = False
			now = datetime.datetime.now() 
			message = "--> Internet was down from " + down_time.strftime('%x %X') + " until " + now.strftime('%x %X')
			print(message)
			print("[TWEETING]")
#			connect()
			try:
				twitter.update_status(status=message)
			except twitter.TwythonError(msg):
				print(msg)
			except twitter.TwythonRateLimitError(msg):
				print(msg)
	else:
		if isdown == False:
			down_time=datetime.datetime.now()
			print ("--> Wasn't down but is now")
			isdown = True
#			twitter = None
		else:
			print ("--> Was down, still is")
			pass
	
	now = datetime.datetime.now()
	message = "--> Resting " + now.strftime('%x %X')
	print(message)
	time.sleep(600)

#!/usr/bin/env python3
import os, pysnap, getpass, snapdb, csv, time, snapsend
from sys import exit
os.system("clear")

def adduser(command):
	user = command.split(' ')
	if len(user) > 2:
		print("too many arguments")
		return
	friend = s.add_friend(user[1])
	if friend["logged"] == True:
		print("User successfully added")
		return
	else:
		print("User doesnt exist or there was a mistake")
		return

def randadd():
	f = open("snapchatdb.csv","rt")
	file = csv.reader(f)
	c = open("location.txt","r")
	print("You can find all possible locations in the database\ntype all for all possible locations\n")
	loc = input("Location: ")
	num = int(input("Quantity: "))
	number = 0
	start_time = time.time()
	if loc == "all":
		for row in file:
			number += 1
			s.add_friend(row[1])
			print(row[1])
			if number >= num:
				return
	elif loc in c.read().split('\n'):
		for row in file:
			if loc == row[2]:
				number += 1
				s.add_friend(row[1])
				print(row[1])
				if number >= num:
					break
	else:
		f.close()
		c.close()
		print("Name not found, returning to menu")
		return
	print("Done...")
	f.close()
	c.close()
	print(time.time()-start_time)

def help():
	print("""This is the help menu
		 for searching in the snapchat database type 'db'
		 for adding users type 'add USERNAME'
		 for adding man people type 'bigadd'
		 for sending a snap type 'sendsnap'
		 for sending snaps to your story type 'sendstory'
		 for receiving snaps type 'receive'""")
def main():
	print("---Snapchat Add user script---")
	print("L0gin")
	username = input("Username: ")
	password = getpass.getpass("Password: ")
	global s
	s = pysnap.Snapchat()
	test = s.login(username, password)
	if test["logged"]==False:
		print("Login Failed")
		exit()
	else:
		print("Login successful")
	while True:
		print("-help for help")
		command = input(">> ")
		if command == "-help":
			help()
		elif command == "db":
			snapdb.main()
		elif "add" in command:
			adduser(command)
		elif command == "bigadd":
			randadd()
		elif command == "sendsnap":
			snapsend.send(username, password)
		elif command == "sendstory":
			snapsend.sendtostory(username, password)
		elif command == "receive":
			snapsend.receive(username, password)	
		elif command == "exit":
			exit()
		else:
			pass
if __name__ == "__main__":
	main() 

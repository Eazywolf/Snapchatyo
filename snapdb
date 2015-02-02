#!/usr/bin/env python3
import csv, os, sys
def printall(): #prints all names in the database
	f = open("snapchatdb.csv", "rt")
	try:
		file = csv.reader(f)
		for row in file:
			print(row)
	finally:
		f.close()

def name(): #searches for a name in the database
	print("Type 'exit' for quitting")
	while True:
		name = input("Name: ")
		if name == "exit":
			return
		yo = False
		try:
			f = open("snapchatdb.csv","rt")
			file = csv.reader(f)
			for row in file:
				if row[1] == name: #if the name exists the program prints number and location
					print("[+]Name found\n")
					info = "\nName: "+row[1]+"\nCountry code: "+row[0]+"\nLocation: "+row[2]
					print(info)
					f.close()
					yo = True
					break
		except:
			pass
		if yo == False:
			print("[-]Name not found\n")
			print("Maybe: ")
			f = open("snapchatdb.csv","rt")
			file = csv.reader(f)
			for row in file:
				if name in row[1]:
					print(row[1])
			f.close()
			
def location():
	while True:
		print("Type 'exit' for quitting")
		print("Type 'show' for showing all possible locations")
		loc = input("Location: ")
		yolo = False
		if loc == "show":
			locations = open("location.txt","r")
			for location in locations.readlines():
				print(location)
		elif loc == "exit":
			return
		else:
			f = open("snapchatdb.csv","rt")
			file = csv.reader(f)
			print(loc)
			number = 0
			for row in file:
				if row[2] == loc:
					print("\nCountry code: "+row[0]+"\nName: "+row[1]) 
					yolo = True
					number += 1
			if yolo == False:
				print("[-]Name not found")
			else:
				print("\n\n",number,"accounts in",loc,"\n\n")
def main():
	while True:
		os.system("clear")
		print("---Snapchatdatabase---\n")
		print("[1]print all")
		print("[2]search for a name")
		print("[3]search for location")
		print("print 'exit' for quitting")
		choise = input(">> ")
		if choise == "exit":
			break
		elif choise == '1':
			printall()
		elif choise == '2':
			name()
		elif choise == "3":
			location()
		else:
			print("[-]Impossible choise")

if __name__ == "__main__":
	main()

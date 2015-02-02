#!/usr/bin/env python3
import os, pysnap
def send(username, password):
	s = pysnap.Snapchat()
	s.login(username, password)
	while True:
		print("Type 'exit' to return")
		uploadfile = input("File you want to upload> ")
		if uploadfile == "exit":
			return
		if os.path.isfile(uploadfile):
			upl = s.upload(uploadfile)
			name = input("Who do u want to send it to> ")
			if name == "exit":
				return
			s.send(upl, name)
		else:
			print("File does not exist")

def sendtostory(username, password):
	s = pysnap.Snapchat()
	s.login(username, password)
	while True:
		uploadfile = input("File you want to upload> ")
		if uploadfile == "exit":
			return
		if os.path.isfile(uploadfile):
			upl = s.upload(uploadfile)
			s.send_to_story(upl, time = 10)
		else:
                        print("File does not exist")

def receive(username, password):
	s = pysnap.Snapchat()
	s.login(username, password)
	snap = s.get_snaps()
	try:
		os.system("mkdir snaps")
		path = ("snaps")
		filename = "{1}_{2}.{3}".format(snap['sender'], snap['id'],get_file_extension(snap['media_type']))
		abspath = os.path.abspath(os.path.join(path, filename))
		data = s.get_blob(snap['id'])
		if data is None:
			return
		with open(abspath, 'wb') as f:
			f.write(data)
			if not quiet:
				print('Saved: {0}'.format(abspath))
		return
	except:
		return

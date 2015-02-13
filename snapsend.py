#!/usr/bin/env python3
from __future__ import print_function
import os
from pysnap import get_file_extension, Snapchat
import sys
from zipfile import is_zipfile, ZipFile
from docopt import docopt
def send(username, password):
	s = Snapchat()
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
	s = Snapchat()
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


def process_snap(s, snap, path, quiet=False):
	filename = '{0}_{1}.{2}'.format(snap['sender'], snap['id'],get_file_extension(snap['media_type']))
	abspath = os.path.abspath(os.path.join(path, filename))
	if os.path.isfile(abspath):
		return
	data = s.get_blob(snap['id'])
	if data is None:
		return
	with open(abspath, 'wb') as f:
		f.write(data)
		if not quiet:
			print('Saved: {0}'.format(abspath))
	if is_zipfile(abspath):
		zipped_snap = ZipFile(abspath)
		unzip_dir = os.path.join(path, '{0}_{1}'.format(snap['sender'],snap['id']))
		zipped_snap.extractall(unzip_dir)
		if not quiet:
			print('Unzipped {0} to {1}'.format(filename, unzip_dir))
def receive(username, password):
	path = "pictures"
	quiet = True
	if not os.path.isdir(path):
		print('No such directory: {0}'.format(path))
		sys.exit(1)
	s = Snapchat()
	if not s.login(username, password).get('logged'):
		print('Invalid username or password')
		sys.exit(1)

	for snap in s.get_snaps():
		process_snap(s, snap, path, quiet)

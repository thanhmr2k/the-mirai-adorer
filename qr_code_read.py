import pyqrcode
import string
import os
from time import time, ctime

while (True):
	fname = '.png'
	s = str(input("URL: "))
	t = str(ctime(time()))
	t = t.replace(':',"'")
	fname = '[' + t + ']' + fname
	print("Processing...")
	url = pyqrcode.create(s, encoding='utf-8')
	url.png(fname, scale = 10)
	print("Done!")
	os.startfile(fname)

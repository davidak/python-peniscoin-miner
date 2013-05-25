#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string
from datetime import datetime
import hashlib
import os

def mine():
	start = datetime.now()
	#key = hashlib.sha256('penis'.encode('utf-8')).hexdigest()
	key = 'f6952d6eef555ddd87aca66e56b91530222d6e318414816f3ba7cf5bf694bf0f'
	word = ''
	i = 0
	while word != key:
		word = hashlib.sha256(''.join(random.choice(string.ascii_lowercase) for x in range(5)).encode('utf-8')).hexdigest()
		#print(str(i) + ' ' + word)
		i += 1
		if (i % 10000) == 0: # every 10.000 run
			try: # ZeroDivision error workaround
				now = datetime.now()
				timediff = now - start
				seconds = timediff.seconds # seconds the programm run
				hashes =  '{0:.{1}f}'.format(i / seconds, 0) # Hash/s
				os.system('cls' if os.name=='nt' else 'clear') # Unix and Windows clear screen
				print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + str(hashes) + ' Hash/s runs ' + str(seconds) + ' seconds')
			except:
				print('Error: computing performance data failed')
		#if (i > 1000000):
		#	word = hashlib.sha256('penis'.encode('utf-8')).hexdigest()
		#	print(word)
	
	end = datetime.now()
	timediff = end - start
	seconds = timediff.seconds # seconds the programm finally run
	os.system('cls' if os.name=='nt' else 'clear') # Unix and Windows clear screen
	print('generated 1 Peniscoin in ' + str(seconds) + ' seconds. averange speed was ' + str(hashes) + ' Hash/s\n')

mine()
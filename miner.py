#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from datetime import datetime
import os

def mine():
	start = datetime.now()
	word = ''
	i = 0
	while word is not 'penis':
		word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(5))
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
	
	end = datetime.now()
	timediff = end - start
	seconds = timediff.seconds # seconds the programm finally run
	os.system('cls' if os.name=='nt' else 'clear') # Unix and Windows clear screen
	print('generated 1 Peniscoin in ' + str(seconds) + ' seconds. averange speed was ' + str(hashes) + ' Hash/s\n')

mine()
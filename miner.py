#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string
import time
import hashlib
import os

def mine():
	start = time.clock()
	key = 'f6952d6eef555ddd87aca66e56b91530222d6e318414816f3ba7cf5bf694bf0f'
	word = ''
	coins = 0
	i = 0
	while True:
		while word != key:
			word = hashlib.sha256(''.join(random.choice(string.ascii_lowercase) for x in range(5)).encode('utf-8')).hexdigest()
			#print(str(i) + ' ' + word)
			i += 1
			if (i % 10000) == 0: # every 10.000 run
				now = time.clock()
				seconds = now - start # seconds the programm run
				hashes =  int(i / seconds) # hashes / seconds
				if hashes > 1000000:
					hashes = '{0:.2f} GHash/s'.format(hashes / 1000000)
				elif hashes > 1000:
					hashes = '{0:.2f} MHash/s'.format(hashes / 1000)
				else:
					hashes = '{0} Hash/s'.format(hashes)

				os.system('cls' if os.name=='nt' else 'clear') # Unix and Windows clear screen
				print(time.strftime('%Y-%m-%d %H:%M:%S ') + hashes + ' ' + str(coins) + ' Peniscoins mined in ' + '{0:.{1}f}'.format(seconds, 3) + ' seconds')

			#if (i > 1000000): # test succesfull generation
			#	word = hashlib.sha256('penis'.encode('utf-8')).hexdigest()
		
		coins += 1
		print('Congratulations! You generated 1 Peniscoin.')
		word = ''
		time.sleep(3)

mine()
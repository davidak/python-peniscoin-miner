#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
import string
import time
import hashlib
import pickle
import os
from version import __version__

class Miner(object):
	"""
	Peniscoin-Miner
	"""
	def __init__(self):
		# read balance and last hash from wallet.dat
		for i in range(10):
			try:
				self.load_wallet()
			except IOError: # if wallet.dat don't exists
				self.create_wallet()

	def __str__(self):
		return self.hashes + ', ' + self.seconds + ' Sekunden'

	def save_wallet(self, coins, last_hash):
		with open('wallet.dat', 'wb') as f:
			pickle.dump(coins, f)
			pickle.dump(last_hash, f)

	def load_wallet(self):
		with open('wallet.dat', 'rb') as f:
			self.coins = pickle.load(f)
			self.last_hash = pickle.load(f)

	def create_wallet(self):
		self.save_wallet(0, 'f6952d6eef555ddd87aca66e56b91530222d6e318414816f3ba7cf5bf694bf0f')

	def mine(self):
		self.start = time.clock()
		self.i = 0
		while True:
			self.current_hash = hashlib.sha256(''.join(random.choice(string.ascii_lowercase) for x in range(5)).encode('utf-8')).hexdigest()

			self.i += 1

			if (self.i % 10000) == 0: # every 10.000 run
				self.now = time.clock()
				self.seconds = self.now - self.start # seconds the programm run
				self.hashes =  int(self.i / self.seconds) # hashes / seconds
				if self.hashes > 1000000:
					self.hashes = '{0:.2f} GHash/s'.format(self.hashes / 1000000)
				elif self.hashes > 1000:
					self.hashes = '{0:.2f} MHash/s'.format(self.hashes / 1000)
				else:
					self.hashes = '{0} Hash/s'.format(self.hashes)

				os.system('cls' if os.name=='nt' else 'clear') # Unix and Windows clear screen
				print(time.strftime('%Y-%m-%d %H:%M:%S ') + self.hashes + ' ' + str(self.coins) + ' Peniscoins mined in ' + '{0:.{1}f}'.format(self.seconds, 3) + ' seconds')

			#if (self.i % 1000000) == 0: # test succesfull generation
			#	self.current_hash = hashlib.sha256('penis'.encode('utf-8')).hexdigest()

			if self.current_hash == self.last_hash:
				self.coins += 1
				self.save_wallet(self.coins, self.current_hash)


if __name__ == '__main__':
	print("Peniscoin-Miner Version " + __version__)
	m = Miner()
	m.mine()

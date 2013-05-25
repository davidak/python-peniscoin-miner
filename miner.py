#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string


def mine():
	word = ''
	i = 0
	while word is not 'penis':
		word = ''.join(random.choice(string.ascii_lowercase) for x in range(5))
		print(str(i) + ' ' + word)
		i += 1
	print("generated 1 peniscoin")

mine()
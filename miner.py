#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string

word = ''

while word is not 'penis':
	word = ''.join(random.choice(string.ascii_lowercase) for x in range(5))

print("generated 1 peniscoin")
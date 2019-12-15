#!/usr/bin/python
# -*- coding: utf8 -*-
import random
import sys
for arg in sys.argv: 1
aide = """
Usage: python genpass.py <number of characters>

Example usage:
    python genpass.py 8
"""
while True:
	try:
		int(arg)
		break
	except ValueError:
		print(aide)
		sys.exit(1)
lettre = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!?+-_:;[]%#$&@")
n = 0
mdp = random.choice(lettre)
arg = int(arg)-1
while n < int(arg):
	mdp = mdp+random.choice(lettre)
	n = n+1
print (mdp)

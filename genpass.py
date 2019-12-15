#!/usr/bin/python
# -*- coding: utf8 -*-
import random
longueur = input("Longueur du mot de passe ? ")
longueur = longueur-1
lettre = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!?+-_:;[]%#$&@")
n = 0
mdp = random.choice(lettre)
while n < longueur:
	mdp = mdp+random.choice(lettre)
	n = n+1
print (mdp)

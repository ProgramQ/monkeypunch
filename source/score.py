from random import randint

# Variables
super_bonus = randint(0,500)
upgrade_percent = None # to be used with shop/upgrade system
multiplier = 1 # for each consegutive monkey punch. Max at 30
total = 0

while True:
	if multiplier >= 30:
		multiplier = 30

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import random
from io import open

file_en = open("curses_en.txt", encoding="utf-8").readlines()
file_de = open("curses_de.txt", encoding="utf-8").readlines()

def curse(lang="en"):
	if lang=="de":
		return random.choice(file_de).strip()
	else:
		return random.choice(file_en).strip()

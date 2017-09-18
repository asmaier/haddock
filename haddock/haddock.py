#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import os
import random
from io import open

curses_en = os.path.join(os.path.dirname(__file__), "curses_en.txt")
curses_de = os.path.join(os.path.dirname(__file__), "curses_de.txt")
curses_fr = os.path.join(os.path.dirname(__file__), "curses_fr.txt")

file_en = open(curses_en, encoding="utf-8").readlines()
file_de = open(curses_de, encoding="utf-8").readlines()
file_fr = open(curses_fr, encoding="utf-8").readlines()

def curse(lang="en"):

	if lang=="de":
		return random.choice(file_de).strip()
	elif lang=="fr":
		return random.choice(file_fr).strip()		
	else:
		return random.choice(file_en).strip()

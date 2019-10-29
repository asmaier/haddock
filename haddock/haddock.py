#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
from io import open

def curse(lang="en"):
    if lang not in curses:
        try:
            filename = os.path.join(os.path.dirname(__file__), 'curses_%s.txt' % lang)
            with open(filename, encoding='utf-8') as f:
                curses[lang] = [c.strip() for c in f]
        except IOError:
            lang = 'en'
    return random.choice(curses[lang])

curses = {}
_ = curse('en')

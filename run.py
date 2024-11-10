#!/usr/bin/python3

import epubcolorise
import traceback

b = epubcolorise.EpubColorise('./epubs/frankenstein.epub', './out/frankcolor.epub')
#b.options.bgcolor = "#eee8d5"
b.options.embolden = False
b.write();

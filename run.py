#!/usr/bin/python3

import epubcolorise
import traceback

try:
    b = epubcolorise.EpubColorise('./epubs/frankenstein.epub', './out/frankcolor.epub')
    b.options.bgcolor = "#002b36"
    b.write();
except Exception as e:
    traceback.print_tb(e.__traceback__, limit=99999)
#    print(e)

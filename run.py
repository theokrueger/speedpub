#!/usr/bin/python3

import epubcolorise
import traceback

b = epubcolorise.EpubColorise('./pg23950-images-3.epub', './out/pg23950-images-3.epub')
b.options.bgcolor = "#eee8d5"
b.write();

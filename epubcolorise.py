# epub-colorise.py
# Parse an epub and colorize text
import sys
import pathlib
import copy

import ebooklib
from ebooklib import epub

import coloriser

class EpubColorise:
    # inpath: string | path to an epub file
    # outpath: string | path to output to (including output name)
    def __init__(self, inpath, outpath):
        self.options = coloriser.ColoriseOptions()
        print(f"Loading epub from {inpath}")

        # create output directory if not exist
        try:
            self.outpath = pathlib.Path(outpath)
            self.outpath.parents[0].mkdir(parents=True, exist_ok=True)
        except:
            print(f"Unable to create output path for target output {outpath}")
            sys.exit(1)

        # load eupb
        try:
            self.book = epub.read_epub(inpath)
        except:
            print(f"File {inpath} does not exit");
            sys.exit(1)

    # write the colorised epub to the output path
    def write(self):
        print("write() is a stub")



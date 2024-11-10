# epub-colorise.py
# Parse an epub and colorize text
import sys
import pathlib
import copy

import ebooklib
from ebooklib import epub

import coloriser

# XHTML files to always ignore
XHTML_TO_IGNORE = {}


# Colorise an epub!
class EpubColorise:
    # inpath: string | path to an epub file
    # outpath: string | path to output to (including output name)
    def __init__(self, inpath, outpath):
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
            print(f"File {inpath} does not exist")
            sys.exit(1)

        # set our metadata
        self.lang = self.book.get_metadata('DC', 'language')[0][0]
        self.title = self.book.get_metadata('DC', 'title')[0][0]
        self.options = coloriser.ColoriseOptions(self.lang)
        print(f"Finished loading '{self.title}' in language '{self.lang}'")

    # write the colorised epub to the output path
    def write(self):
        # add color
        print(f"Performing full colorisation for {self.title}")
        clr = coloriser.Coloriser(self.options)
        # iterate over xhtml
        for xhtml in self.book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            if not XHTML_TO_IGNORE.get(xhtml.get_name()):
                print(f"Colorising {xhtml.get_name()}")
                xhtml.set_content(
                    str.encode(clr.colorise_xhtml(xhtml.get_content())))

        # write final product
        print(f"Writing to {self.outpath}")
        epub.write_epub(self.outpath, self.book)

#!/usr/bin/python3
# convert some text into coloured HTML
import sys
from enum import Enum
from bs4 import BeautifulSoup, NavigableString
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re


# Hardcoded punctuation alginments
class Alignments(Enum):
    Left = -1
    Right = 1


ALIGNMENT_LOOKUP = {
    "!": Alignments.Left,
    ".": Alignments.Left,
    "?": Alignments.Left,
    ",": Alignments.Left,
    ">": Alignments.Left,
    "]": Alignments.Left,
    "}": Alignments.Left,
    ")": Alignments.Left,
    ":": Alignments.Left,
    ";": Alignments.Left,
    "%": Alignments.Left,
    "”": Alignments.Left,
    "“": Alignments.Right,
    "<": Alignments.Right,
    "[": Alignments.Right,
    "{": Alignments.Right,
    "(": Alignments.Right,
    "#": Alignments.Right,
    "@": Alignments.Right,
    "$": Alignments.Right,
}


# Our distilled prats of speech
# value is the HTML tag it uses
class POS(Enum):
    Untagged = 'ut'  # obvious
    Interjection = 'ij'  # ummmm
    Noun = 'nn'  # obvious
    Verb = 'vb'  # obvious
    Adjective = 'aj'  # obvious
    Adverb = 'av'  # obvious
    Preposition = 'pr'  # after/in/on/around
    Article = 'ar'  # Includes particles
    Conjunction = 'cj'  # and/or/but
    Pronoun = 'pn'  # style as a noun probably
    Modal = 'ml'  # will/can/might/do


# Lookup table to convert the NLTK POS tags to our POS tags
DEFAULT_COLORS = {
    POS.Untagged: '#002b36',
    POS.Interjection: '#002b36',
    POS.Noun: '#b58900',
    POS.Verb: '#cb4b16',
    POS.Adjective: '#d33682',
    POS.Adverb: '#d33682',
    POS.Preposition: '#002b36',
    POS.Article: '#002b36',
    POS.Conjunction: '#002b36',
    POS.Pronoun: '#002b36',
    POS.Modal: '#002b36',
}

NLTK_TAG_LOOKUP = {
    "CC": POS.Conjunction,
    "CD": POS.Untagged,
    "DT": POS.Article,
    "EX": POS.Untagged,  # TODO
    "FW": POS.Untagged,
    "IN": POS.Preposition,
    "JJ": POS.Adjective,
    "JJR": POS.Adjective,
    "JJS": POS.Adjective,
    "LS": POS.Untagged,
    "MD": POS.Modal,
    "NN": POS.Noun,
    "NNS": POS.Noun,
    "NNP": POS.Noun,
    "NNPS": POS.Noun,
    "PDT": POS.Article,
    "POS": POS.Adjective,
    "PRP": POS.Pronoun,
    "PRP$": POS.Pronoun,
    "RB": POS.Adverb,
    "RBR": POS.Adverb,
    "RBS": POS.Adverb,
    "RP": POS.Article,
    "TO": POS.Article,  # TODO
    "UH": POS.Interjection,
    "VB": POS.Verb,
    "VBD": POS.Verb,
    "VBG": POS.Verb,
    "VBN": POS.Verb,
    "VBP": POS.Verb,
    "VBZ": POS.Verb,
    "WDT": POS.Article,
    "WP": POS.Pronoun,
    "WP$": POS.Pronoun,
    "WRB": POS.Adverb,
}


# Options passed to the colorise function
class ColoriseOptions:

    # create a new instnace of ColoriseOptions
    # lang: string | language identifier
    def __init__(self, lang):
        # set defaults
        #self.globalstyle = "colorised-style.css"
        self.lang = lang
        self.bgcolor = "transparent"
        self.enablecolors = True
        self.colors = DEFAULT_COLORS
        self.embolden = True

    # get the style information for the selected colors
    # return: string | css style information
    def get_style(self):
        s = f"""
        body {{
          background-color: {self.bgcolor};
          color: {self.colors.get(POS.Untagged)};
        }}
        """
        if self.enablecolors:
            for k in self.colors:
                s += f"{k.value} {{ color: {self.colors.get(k)}; }}\n"

        return s

    # get a color association for a POS
    # pos: POS enum | Part of speech to get color association for
    # return: string  | css color (i.e. "#123456" or "red")
    def get_color(self, pos):
        # ensure preconditions
        if not isinstance(pos, POS):
            print(f"supplied argument to get_color '{pos}' is incorrect!")
            sys.exit(1)

        return self.colors.get(pos)

    # set a color association for a POS
    # pos: POS enum | Part of speech to set color association for
    # col: string | css color (i.e. "#123456" or "red")
    def set_color(self, pos, col):
        # ensure preconditions
        if not (isinstance(pos, POS) and type(col) == string):
            print(
                f"supplied arguments to set_color '{pos}' and '{col}' are incorrect!"
            )
            sys.exit(1)

        self.colors[pos] = col


# Colorise text based on ColoriseOptions
class Coloriser:

    # opts: ColoriseOptions | self explanatory
    def __init__(self, opts):
        self.opts = opts

    # text: string | raw text, UTF-8
    # return: string | colorised text
    def colorise_text(self, text):
        return 'hi'

    # xhtml: bytes | xhtml text
    # return: string | colorised text
    def colorise_xhtml(self, xhtml):
        soup = BeautifulSoup(xhtml, 'html.parser')

        self.colorise_soup_recurse(soup, soup.html.body)

        # add style to top
        style_tag = soup.new_tag('style')
        style_tag.string = self.opts.get_style()
        soup.html.body.insert(0, style_tag)

        return str(soup)

    # soup: BeautifulSoup
    # node: A node in soup
    def colorise_soup_recurse(self, soup, node):
        i = 0
        for child in node.children:
            if type(child) == NavigableString:
                # NLTK tag the content
                words = nltk.word_tokenize(child)
                tagged = nltk.pos_tag(words)  # [(word, tag), ...]

                # Fix punctuation alignments
                new_tagged = []
                pfx = ""
                for (word, tag) in tagged:
                    merge = ALIGNMENT_LOOKUP.get(word)
                    if merge == Alignments.Left:
                        if len(new_tagged) == 0:
                            continue
                        (prevwd, prevtg) = new_tagged.pop()
                        prevwd = prevwd + word
                        new_tagged.append((prevwd, prevtg))
                        continue

                    if merge == Alignments.Right:
                        pfx = pfx + word
                        continue

                    word = pfx + word
                    new_tagged.append((word, tag))
                    pfx = ""

                # Apply coloring
                new_node = soup.new_tag(node.name)
                for (word, tag) in new_tagged:

                    tag = NLTK_TAG_LOOKUP.get(tag)
                    if tag == None:
                        tag = POS.Untagged

                    new_child = soup.new_tag(tag.value)
                    # apply bold if needed
                    if self.opts.embolden:
                        half = max(int(len(word) / 2 + 0.5), min(len(word), 3))
                        bolded = soup.new_tag('b')
                        bolded.string = word[:half]
                        new_child.string = word[half:]
                        new_child.insert(0, bolded)
                    else:
                        new_child.string = word
                    new_node.append(new_child)

                node.contents[i].replace_with(new_node)

            else:
                self.colorise_soup_recurse(soup, child)
            i = i + 1

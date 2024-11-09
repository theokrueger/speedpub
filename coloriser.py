#!/usr/bin/python3
# convert some text into coloured HTML
import sys
from enum import Enum


# Our distilled prats of speech
class POS(Enum):
    Untagged = 0  # obvious
    Interjection = 1  # ummmm
    Noun = 2  # obvious
    Verb = 3  # obvious
    Adjective = 4  # obvious
    Adverb = 5  # obvious
    Preposition = 6  # after/in/on/around
    Article = 7  # Includes particles
    Conjunction = 8  # and/or/but
    Pronoun = 9  # style as a noun probably
    Modal = 10  # will/can/might/do


# Options passed to the colorise function
class ColoriseOptions:

    # create a new instnace of ColoriseOptions
    def __init__(self):
        # set defaults
        self.colors = {
            POS.Untagged: '#eee8d5',
            POS.Interjection: '#eee8d5',
            POS.Noun: '#b58900',
            POS.Verb: '#cb4b16',
            POS.Adjective: '#d33682',
            POS.Adverb: '#d33682',
            POS.Preposition: '#eee8d5',
            POS.Article: '#eee8d5',
            POS.Conjunction: '#eee8d5',
            POS.Pronoun: '#eee8d5',
            POS.Modal: '#eee8d5',
        }
        self.embolden = True

    # get a color association for a POS
    # pos: POS enum | Part of speech to get color association for
    # return: string  | hexadecimal color (i.e. "#123456")
    def get_color(self, pos):
        # ensure preconditions
        if not isinstance(pos, POS):
            print(f"supplied argument to get_color '{pos}' is incorrect!")
            sys.exit(1)

        return self.colors.get(pos)

    # set a color association for a POS
    # pos: POS enum | Part of speech to set color association for
    # col: string | colour to set POS to (i.e. "#123456")
    def set_color(self, pos, col):
        # ensure preconditions
        if not (isinstance(pos, POS) and type(col) == string
                and col[0:1] == '#'):
            print(
                f"supplied arguments to set_color '{pos}' and '{col}' are incorrect!"
            )
            sys.exit(1)

        self.colors[pos] = col


# from pathlib import Path
# from enum import Enum

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize

# stop_words = set(stopwords.words('english'))

# COLOUR_LOOKUP = {
#     'c0': '#eee8d5',
#     'c1': '#b58900',
#     'c2': '#cb4b16',
#     'c3': '#dc322f',
#     'c4': '#d33682',
#     'c5': '#6c71c4',
#     'c6': '#268bd2',
#     'c7': '#2aa198',
#     'c8': '#859900',
# }

# TAG_LOOKUP = {
#     "CC": POS.Conjunction,
#     "CD": POS.Untagged,
#     "DT": POS.Article,
#     "EX": POS.Untagged,  # TODO
#     "FW": POS.Untagged,
#     "IN": POS.Preposition,
#     "JJ": POS.Adjective,
#     "JJR": POS.Adjective,
#     "JJS": POS.Adjective,
#     "LS": POS.Untagged,
#     "MD": POS.Modal,
#     "NN": POS.Noun,
#     "NNS": POS.Noun,
#     "NNP": POS.Noun,
#     "NNPS": POS.Noun,
#     "PDT": POS.Article,
#     "POS": POS.Adjective,
#     "PRP": POS.Pronoun,
#     "PRP$": POS.Pronoun,
#     "RB": POS.Adverb,
#     "RBR": POS.Adverb,
#     "RBS": POS.Adverb,
#     "RP": POS.Article,
#     "TO": POS.Article,  # TODO
#     "UH": POS.Interjection,
#     "VB": POS.Verb,
#     "VBD": POS.Verb,
#     "VBG": POS.Verb,
#     "VBN": POS.Verb,
#     "VBP": POS.Verb,
#     "VBZ": POS.Verb,
#     "WDT": POS.Article,
#     "WP": POS.Pronoun,
#     "WP$": POS.Pronoun,
#     "WRB": POS.Adverb,
# }

# # setup
# txt = Path('sample.txt').read_text()
# out = """
# <!DOCTYPE html>
# <html>
# <head>
# <title>Page Title</title>
# """

# # add style
# out += """
# <style>
# body {
#    background-color: #002b36;
# }
# """
# for k in COLOUR_LOOKUP:
#     out += f"{k} {{ color: {COLOUR_LOOKUP.get(k)}; }}\n"

# out += "</style></head><body>"

# # add content
# tokenized = sent_tokenize(txt)
# for i in tokenized:
#     # Set up NLTK and tag words
#     wordsList = nltk.word_tokenize(i)
#     tagged = nltk.pos_tag(wordsList)  # [(word, tag), ...]

#     for (word, tag) in tagged:
#         tag = TAG_LOOKUP.get(tag)
#         half = int(len(word) / 2)
#         word = f"<b>{word[:half]}</b>{word[half:]}"
#         if tag == None:
#             tag = POS.Untagged
#         out += f" <{tag.value}>{word}</{tag.value}>"

# out += "</body></html>"
# print(out)

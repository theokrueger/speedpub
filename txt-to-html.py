#!/usr/bin/python3
# convert some text into coloured HTML
from pathlib import Path
from enum import Enum

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))


class POS(Enum):
    Untagged = 'c0'  # obvious
    Interjection = 'c0'  # ummmm
    Noun = 'c1'  # obvious
    Verb = 'c2'  # obvious
    Adjective = 'c4'  # obvious
    Adverb = 'c4'  # obvious
    Preposition = 'c0'  # after/in/on/around
    Article = 'c0'  # Includes particles
    Conjunction = 'c0'  # and/or/but
    Pronoun = 'c0'  # style as a noun probably
    Modal = 'c0'  # will/can/might/do


COLOUR_LOOKUP = {
    'c0': '#eee8d5',
    'c1': '#b58900',
    'c2': '#cb4b16',
    'c3': '#dc322f',
    'c4': '#d33682',
    'c5': '#6c71c4',
    'c6': '#268bd2',
    'c7': '#2aa198',
    'c8': '#859900',
}

TAG_LOOKUP = {
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

# setup
txt = Path('sample.txt').read_text()
out = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
"""

# add style
out += """
<style>
body {
   background-color: #002b36;
}
"""
for k in COLOUR_LOOKUP:
    out += f"{k} {{ color: {COLOUR_LOOKUP.get(k)}; }}\n"

out += "</style></head><body>"

# add content
tokenized = sent_tokenize(txt)
for i in tokenized:
    # Set up NLTK and tag words
    wordsList = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(wordsList)  # [(word, tag), ...]

    for (word, tag) in tagged:
        tag = TAG_LOOKUP.get(tag)
        half = int(len(word) / 2)
        word = f"<b>{word[:half]}</b>{word[half:]}"
        if tag == None:
            tag = POS.Untagged
        out += f" <{tag.value}>{word}</{tag.value}>"

out += "</body></html>"
print(out)

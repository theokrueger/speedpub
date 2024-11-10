## Read faster. Learn quicker. Understand deeper. SpeedPUB. 
SpeedPUB provides syntax highlighting to written language. 

![Banner](https://media.githubusercontent.com/media/theokrueger/speedpub/refs/heads/master/marketing/banner.png)

## TL:DR
SpeedPUB is a tool that leverages an NLP neural network model to colour words based off their purpose in a text. SpeedPUB will improve your reading speed and comprehension in both English and Chinese (so far!).

## What?
SpeedPUB uses cutting-edge Natural Language Processing Neural Networks to determine the _purpose_ of words in a sentence, and highlights them according to their function. 

SpeedPUB also has the ability to *bold* portions of words to enable advanced speed-reading techniques.

The optional GUI provides an easy-to-use interface for creating highlighted EPUBs, and allows in-depth customization of highlight colours.

## How?
Written in Python, SpeedPUB performs the following pipeline:
- Deserialise EPUB with [EBookLib](https://pypi.org/project/EbookLib/)
- Parse EPUB XHTML content with [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- Determine Parts of Speech using [NLTK](https://www.nltk.org/) and [HanLP](https://hanlp.hankcs.com/docs/index.html)
- Package back into EPUB

The optional GUI is written using [tkinter](https://docs.python.org/3/library/tkinter.html)

## Installation steps
- Install the pip packagest as listed in `requirements.txt`
- Mark `gooey.py` as executable, and run it!

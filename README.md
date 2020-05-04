# Introduction

This is a script I made for myself to turn a csv file of Chinese characters into Anki flash cards, with English translations and pinyin.

Requires the package [genanki](https://github.com/kerrickstaley/genanki) to create the Anki deck.

English translations and pinyin are from [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict)

# First time running
Run `python build_db.py`, which will load the CC-CEDICT dictionary into a dictionary stored as a pickle file for Python to read in on subsequent runs.

# Usage
Create a csv file with the Chinese characters you want to translate, one word per row, with no title. By default, the script looks for a `words.csv` but you can change this. 

Run `python main.py`.

This will then create a `deck.apkg` file which you can put into Anki. The note template can also be modified, including custom CSS.

The translated words are then pickled and stored in a `.cache.pickle` file, so subsequent runs of the script will only translate additional words added to the csv file.

(Note that this code is brittle and if you end up deleting earlier words in the csv file, the script won't parse future words correctly. The easiest way to start all over is to just delete the `.cache.pickle` file, and the script will automatically rebuild the Anki deck from scratch.)
# Introduction

This is a script I made for myself to turn a csv file of Chinese characters into Anki flash cards.

Requires [genanki](https://github.com/kerrickstaley/genanki).

Pinyin are from [Glosbe](https://glosbe.com/transliteration).

English translations are from [MyMemory](https://mymemory.translated.net/doc/spec.php) by Translated Labs.

# Usage
Create a csv file with the Chinese characters you want to translate, one word per row, with no title. By default, the script looks for a `words.csv` but you can change this. 

Running `main.py` will create a `deck.apkg` file which you can put into Anki. The note template can also be modified, including custom CSS.

The translated words are then pickled and stored in a `.cache.pickle` file, so subsequent runs of the script will only translate additional words added to the csv file.
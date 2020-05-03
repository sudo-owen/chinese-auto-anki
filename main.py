# libraries
import genanki
import pickle
import requests
import csv
from time import sleep

model = genanki.Model(
  100,
  'Basic Chinese',
  fields = [
    {'name': 'Question'},
    {'name': 'Answer'}
  ],
  templates = [{
    'name': 'Card',
    'qfmt': '{{Question}}',
    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'
  }],
  css = """
  .card {
    font-size: 50px;
    text-align: center;
  }
  """
)

deck = genanki.Deck(
  17,
  'Chinese Characters'
)

# load up previously defined words
try:
  with open(".cache.pickle", "rb") as file:
    note_list = pickle.load(file)
    index = len(note_list)
except FileNotFoundError:
  note_list = []
  index = 0

# load up list of words
with open("words.csv", "r") as file:
  reader = csv.reader(file)
  words = list(reader)
  new_words = words[index:]

# hard-coded variables :P
glosbe_1 = 'https://glosbe.com/transliteration/api?from=Han&dest=Latin&text='
glosbe_2 = '&format=json'
mymemory_1 = 'https://api.mymemory.translated.net/get?q='
mymemory_2 = '&langpair=zh|en'
delay = 0.025
deck_name = 'deck.apkg'

# ping the APIs for pinyin and english defn
for w in new_words:
  sleep(delay)
  r = requests.get(glosbe_1 + w[0] + glosbe_2).json()
  w.append(r['text'])
  sleep(delay)
  r = requests.get(mymemory_1 + w[0] + mymemory_2).json()
  w[1] = w[1] + ' ' + r['responseData']['translatedText']
  note_list.append(genanki.Note(
    model = model,
    fields = [w[0], w[1]]
  ))
  print("Adding: " + w[0] + '(' + w[1] + ')')
print("Added: " + str(len(new_words)) + " new words to " + deck_name)

# add all of the new cards to the deck
for n in note_list:
  deck.add_note(n)

# create new deck
genanki.Package(deck).write_to_file(deck_name)

# store new card list
with open(".cache.pickle", "wb") as file:
  pickle.dump(note_list, file)

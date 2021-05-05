from google_trans_new import google_translator
import random
translator = google_translator()

prepositions = [
    'an',
    'unter',
    'vor',
    'über',
    'hinter',
    'neben',
    'in',
    'auf'
]

subjects = [
    'die Lampe',
    'das Buch',
    'das Geld',
    'das Essen',
    'der Schlüssel',
    'der Löffel',
    'die Gabel', 
    'das Messer',
    'das Kissen',
    'das Papier'
]

objects = [
    'der Tisch',
    'das Regal',
    'der Fernseher',
    'das Fenster',
    'das Zimmer',
    'das Pult',
    'das Bett',
    'der Boden',
    'der Herd',
    'die Couch',
    'der Stuhl'
]

print(f"{random.choice(subjects)} | {random.choice(prepositions)} | {random.choice(objects)}")
line = input()
translation = translator.translate(line, lang_tgt='en', lang_src='de')
inverse_translation = translator.translate(translation, lang_tgt='de', lang_src='en')
translation_of_the_inverse = translator.translate(inverse_translation, lang_tgt='en', lang_src='de')
print(f"INPUT: {line} | DE: {inverse_translation}")
print(f"EN: {translation} | EN: {translation_of_the_inverse}")
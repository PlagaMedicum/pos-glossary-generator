from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext) )
print(word_tokenize(mytext))


import nltk
from nltk.tokenize import PunktSentenceTokenizer

document = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'
sentences = nltk.sent_tokenize(document)   
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))

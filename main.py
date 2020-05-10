import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import treebank
from nltk.data import load

import re

from tkinter import *

root = Tk()

txt = StringVar()
txt.set("why do we all must to wear those ridiculous ties?! Freeman, STAP!")
res = StringVar()

def pos_tag_sentence(sent):
    return nltk.pos_tag(nltk.word_tokenize(sent))

#t = treebank.parsed_sents('wsj_0001.mrg')

tagdict = load('help/tagsets/upenn_tagset.pickle')

def tag_text():
    sentences = nltk.sent_tokenize(txt.get())
    out = str()
    for sent in sentences:
        out += "--- Sentence: {}\n".format(sent)
        postgs = pos_tag_sentence(sent)
        i = 0
        pos = 0
        while i < len(postgs):
            pt = postgs[i]
            print(pt)
            if re.search(r"[A-Za-z]+", pt[0]) != None:
                pos += 1
                out += "{}. {} -- {}({})\n".format(pos, pt[0], pt[1], tagdict[pt[1]][0])
            i += 1
    res.set(out)

root.title("Sentence analyzer")
root.geometry("700x600")

entry = Entry(width=70, textvariable=txt)
entry.place(relx=.5, rely=.1, anchor="c")

button = Button(text="Tag text", command=tag_text)
button.place(relx=.5, rely=.2, anchor="c")

resultlabel = Label(textvariable=res, justify=LEFT)
resultlabel.place(relx=.5, rely=.3, anchor="n")

root.mainloop()

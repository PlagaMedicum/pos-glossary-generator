import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.data import load

import re

from tkinter import *

root = Tk()

txt = StringVar()
txt.set("why do we all must to wear those ridiculous ties?! Freeman, STAP!")
res = StringVar()

def pos_tag_sentence(sent):
    postgs = nltk.pos_tag(nltk.word_tokenize(sent))
    rtgs = list()
    i = 0
    while i < len(postgs):
        pt = postgs[i]
        if re.search(r"[A-Za-z]+", pt[0]) != None:
            rtgs.append(pt)
        i += 1
    return rtgs

tagdict = load('help/tagsets/upenn_tagset.pickle')

def tag_text():
    sentences = nltk.sent_tokenize(txt.get())
    out = str()
    for sent in sentences:
        out += "--- Sentence: {}\n".format(sent)
        tsent = pos_tag_sentence(sent)
        i = 0
        while i < len(tsent):
            pt = tsent[i]
            out += "{}. {} -- {}({})\n".format(i + 1, pt[0], pt[1], tagdict[pt[1]][0])
            i += 1
    res.set(out)

helpmsg = str()
for key in tagdict.keys():
    helpmsg += "* {} -- {}\nExamples: {}\n".format(key, tagdict[key][0], tagdict[key][1])

def help_window():
    children = Toplevel(root)
    children.title('Help')


    text = Text(children, height=20, width=100)
    scroll = Scrollbar(children)
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=Y)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    text.insert(END, helpmsg)

root.title("Sentence analyzer")
root.geometry("700x600")

entry = Entry(width=70, textvariable=txt)
entry.place(relx=.5, rely=.1, anchor="c")

button = Button(text="Tag text", command=tag_text)
button.place(relx=.5, rely=.2, anchor="c")

resultlabel = Label(textvariable=res, justify=LEFT)
resultlabel.place(relx=.5, rely=.3, anchor="n")

help = Button(text="Help", command=lambda: help_window())
help.place(relx=.5, rely=.8, anchor="c")

root.mainloop()

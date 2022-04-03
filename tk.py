#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:46:52 2022

@author: alexanderel-hajj
"""

from tkinter import *
import tkinter
from wonderwords import RandomWord
r = RandomWord()
word = r.word(word_min_length=5, word_max_length=5).upper()



window = Tk()

GREEN = "#96de45"

wordInput = Entry(window)
wordInput.grid(row = 999, column = 0, padx = 0, pady = 0, columnspan = 3)


wordGuessButton = Button(window, text = "Guess")
wordGuessButton.grid(row = 999, column = 3, columnspan = 2)





greeting = tkinter.Label(text="Welcome to Wordle+")
greeting.pack()





window.mainloop()
tkinter._test()


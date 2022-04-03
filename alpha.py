#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:01:41 2022

@author: alexanderel-hajj
"""

from termcolor import colored

 
def check_letter(letter_guess: str, guess_word: str, word: str) -> str:
    
    print(f"what is the word guessed? : {guess_word}")
    print(f"what is the letter entered? : {letter_guess}")
    index_of_letter_guess = [p for p, c in enumerate(guess_word) if c == letter_guess]
    print(f"index of letter in guessed word: {index_of_letter_guess}")
    
    print(f"final word: {word}")
    index_of_letter_word = [p for p, c in enumerate(word) if c == letter_guess]
    print(f"index of letter in final word: {index_of_letter_word}")
    
    ## check if letter is in both words
    if len(index_of_letter_guess) == 1 and len(index_of_letter_word) == 1:
        print("letter is in word and guess word once")
        
        # check if have same index
        if index_of_letter_guess[0] == index_of_letter_word[0]:
            print("index of letter matches guess word and final word")
            print("guess word first letter should be green")
            letter = colored(letter_guess, 'green')
            
        elif index_of_letter_guess[0] != index_of_letter_word[0]:
            print("first letter in guess matches first letter in word")
            letter = colored(letter_guess, 'yellow')
            
    else:
        print("letter is not in final word")
        print("return letter with no color")
        letter = letter_guess
            
    return letter



word = "CRANE"

guess_list = []

while True:
    print("Input a word")
    guess_1 = input().upper()
    if len(guess_1) != 5:
        print("length of word not 5. Please try again")
    else:
        print("Correct word length")
        # split word
        print("split final word")
        word_split = list(word)
        print(word_split)
        
        print("split guessed word")
        guess_1_split = list(guess_1)
        print(guess_1_split)
        
        print("WORD GUESSED: LETTER IS IN CORRECT PLACE")
        
        for index, letter in enumerate(guess_1_split):
            print(f"letter_{index}: {letter}")
            
            letter_return = check_letter(letter, guess_1, word)
            print(f"returned letter: {letter_return}")
            guess_list.append(letter_return)
        break





    

l=check_letter("R", "RAILS", "CRANE")
print(l)













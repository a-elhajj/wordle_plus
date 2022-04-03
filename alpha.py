#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:01:41 2022

@author: alexanderel-hajj
"""

from termcolor import colored, cprint
from colorama import Fore, Style, init
import enchant
d = enchant.Dict("en_US")

# init()

# word = "SISSY"
print("WORD TO GUESS")
word = input().upper()


def check_letter(letter_guess: str, index: int, guess_word: int, 
                 word: str) -> str:
    
    # print(f"what is the word guessed? : {guess_word}")
    # print(f"what is the letter entered? : {letter_guess}")
    index_of_letter_guess = [p for p, c in enumerate(guess_word) if c == letter_guess]
    # print(f"index of letter in guessed word: {index_of_letter_guess}")
    
    # print(f"final word: {word}")
    index_of_letter_word = [p for p, c in enumerate(word) if c == letter_guess]
    # print(f"index of letter in final word: {index_of_letter_word}")
    
    
    if letter_guess in word:
        if index in index_of_letter_word:
            letter = colored(letter_guess, 'green')
            # print(letter)
        elif index not in index_of_letter_word:
            letter = colored(letter_guess, 'yellow')
            # print(letter)
        else:
            letter = colored(letter_guess, 'grey')
            # print(letter)
    else:
        letter = colored(letter_guess, 'grey')
        # print(letter)
    return letter


def input_word():
    """
    Input word and check if it has length=5

    Returns
    -------
    guess_1 : string
        Word user has guessed.

    """
    print("GUESSED WORD")
    guess_1 = input().upper()
    if d.check(guess_1):
        if len(guess_1) != 5:
            print("length of word not 5. Please try again")
            return input_word()
        else:
            print("Correct word length")
            return guess_1
    else:
        print("Word is not english. Please try again")
        return input_word()

def guess_correct(guess, word):
    # print(guess_1_split)
    print("GUESS WORD MATCHES FINAL WORD")
    
    final_word = colored(word, 'green')
    # n+=1
    # print(f"GOT WORD IN {n} GUESS")
    return final_word


def check_letters(guess_split, guess, word):
    guess_list = []
    for index, letter in enumerate(guess_split):
        # print(f"letter_{index}: {letter}")
        
        letter_return = check_letter(letter, index, guess, word)
        
        # print(f"returned letter: {letter_return}")
        guess_list.append(letter_return)
        # print(f"guess_list: {guess_list}")
    final_word = ''.join(guess_list)
    # n+=1
    return final_word

def guess_word(word, n):
    # guess_dict[n] = input_word()
    guess_1 = input_word()
    guess_1_split = list(guess_1)
    if guess_1 != word:
        final_word = check_letters(guess_1_split, guess_1, word)
        n+=1
        print(final_word)
        print(f"GUESS: {n}")
        if n >= 6:
            exit()
        return guess_word(word, n)
    else:
        final_word = guess_correct(guess_1, word)
        n+=1
        print(f"final_word: {final_word}")
        print(f"word: {word}")
        print(f"FINAL GUESS: {n}")
        return final_word, n

guess_dict = {}
prior_guess = []
n=0
while True:
    # guess_1 = input_word()
    # print(guess_1)
    if n == 0:
        final_word, n = guess_word(word, n)
        print('yes')
        break
    else:
        print('no')
        break










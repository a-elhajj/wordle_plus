#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 11:01:41 2022

@author: alexanderel-hajj
"""

from termcolor import colored
import enchant
from wonderwords import RandomWord
r = RandomWord()
print("###################################")
print("Welcome to Wordle+")
print("###################################")

print("Play with 4, 5, or 6 letter words!")
def enter_number():
    try:
        print("Enter in a number between 4 and 6")
        num_letters = int(input())
        if num_letters in (4,5,6):
            return num_letters 
        else:
            print("Try again!")
            enter_number()
    except ValueError:
        print("Must be a number!!")
        return enter_number()
    
num_letter = enter_number()
print(f"You are now playing {num_letter}-letter Wordle")
print("Remember you have six guesses!")

word = r.word(word_min_length = num_letter, 
              word_max_length = num_letter).upper()
d = enchant.Dict("en_US")


def check_letter(letter_guess: str, index: int, guess_word: int, 
                 word: str) -> str:
    
    index_of_letter_word = [p for p, c in enumerate(word) if c == letter_guess]    
    
    if letter_guess in word:
        if index in index_of_letter_word:
            letter = colored(letter_guess, 'green')
        elif index not in index_of_letter_word:
            letter = colored(letter_guess, 'yellow')
        else:
            letter = colored(letter_guess, 'grey')
    else:
        letter = colored(letter_guess, 'grey')
    return letter


def input_word():
    """
    Input word and check if it has length=5

    Returns
    -------
    guess_1 : string
        Word user has guessed.

    """
    print("Guess the word!")
    guess_1 = input().upper()
    if d.check(guess_1):
        if len(guess_1) != 5:
            print("Length of word not 5. Please try again")
            return input_word()
        else:
            return guess_1
    else:
        print("Word is not english. Please try again")
        return input_word()

def guess_correct(guess, word):    
    final_word = colored(word, 'green')
    return final_word


def check_letters(guess_split, guess, word):
    guess_list = []
    for index, letter in enumerate(guess_split):
        letter_return = check_letter(letter, index, guess, word)
        
        guess_list.append(letter_return)
    final_word = ''.join(guess_list)
    return final_word

def guess_word(word, n):
    guess_1 = input_word()
    guess_1_split = list(guess_1)
    if guess_1 != word:
        final_word = check_letters(guess_1_split, guess_1, word)
        n+=1
        print(f"Guess {n}: {final_word}")
        if n >= 6:
            exit()
        return guess_word(word, n)
    else:
        final_word = guess_correct(guess_1, word)
        n+=1
        print(f"Guess {n}: {final_word}")
        print("Congrats! You guessed the right word!")
        return final_word, n

guess_dict = {}
prior_guess = []
n=0
while True:
    if n == 0:
        final_word, n = guess_word(word, n)
        break
    else:
        break
